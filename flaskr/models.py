import os
import base64
from flask import url_for
from flask_login import UserMixin
from libgravatar import Gravatar
from flaskr import db, login_manager
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timedelta


class PaginatedApiMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = query.paginate(page, per_page, False)
        data = {
            "items": [item.to_dict() for item in resources.items],
            "_meta": {
                "page": page,
                "per_page": per_page,
                "total_pages": resources.pages,
                "total_items": resources.total
            },
            "_links": {
                "self": url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                "next": url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                "prev": url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
        }

        return data


class User(PaginatedApiMixin, UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, index=True, nullable=False)
    email = db.Column(db.String(120), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(130))
    contacts = db.relationship("Contact", backref="author", lazy="dynamic")
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self):
        g = Gravatar(self.email)
        return g.get_image(default="identicon")

    def to_dict(self, include_email=False):
        data = {
            "id": self.id,
            "username": self.username,
            "contacts_count": self.contacts.count(),
            "_links": {
                "self": url_for("api.get_user", id=self.id),
                "avatar": self.avatar()
            }
        }

        if include_email:
            data["email"] = self.email

        return data

    def from_dict(self, data, new_user=False):
        for field in ["username", "email"]:
            if field in data:
                setattr(self, field, data[field])

        if new_user and "password" in data:
            self.set_password(data["password"])

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()

        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token

        self.token = base64.b64encode(os.urandom(24)).decode("utf-8")
        self.token_expiration = now + timedelta(seconds=expires_in)

        db.session.add(self)

        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()

        if user is None or user.token_expiration < datetime.utcnow():
            return None

        return user

    def __repr__(self):
        return f"""
            User:
                Id: {self.id},
                Username: {self.username},
                Email: {self.email},
                Contacts: {Contact.query.filter_by(user_id=self.id).all()}
        """


class Contact(db.Model):
    __tablename__ = "contact"
    id = db.Column(db.Integer, primary_key=True)
    contact_name = db.Column(db.String(40), nullable=False)
    contact_phonenumber = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"""
            Contact:
                Id: {self.id},
                ContactName: {self.contact_name},
                ContactPhonenumber: {self.contact_phonenumber}
                UserId: {self.user_id}
        """


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
