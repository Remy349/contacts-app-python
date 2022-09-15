from flask_login import UserMixin
from libgravatar import Gravatar
from flaskr import db, login_manager
from werkzeug.security import check_password_hash, generate_password_hash


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, index=True, nullable=False)
    email = db.Column(db.String(120), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(130))
    contacts = db.relationship("Contact", backref="author", lazy="dynamic")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self):
        g = Gravatar(self.email)
        return g.get_image(default="identicon")

    def __repr__(self):
        return f"""
            User:
                Id: {self.id},
                Username: {self.username},
                Email: {self.email},
                Contacts: {self.contacts}
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
