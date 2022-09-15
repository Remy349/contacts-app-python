document.addEventListener('DOMContentLoaded', () => {
  /* Remove text from logout and just leave icon */
  const logoutLink = document.querySelector('.logout')

  if (logoutLink && window.innerWidth <= 330) {
    logoutLink.innerHTML = `
      <i class='bx bx-log-out'></i>
    `
  }

  /* Change background color */
  if (window.location.pathname !== "/auth/sign-in") {
    document.body.style.background = '#F3F9FB'
  }

  /* Validate form of new contact | Just numbers */
  const newContactForm = document.querySelector('.new__form')

  if (newContactForm) {
    newContactForm.addEventListener('submit', (e) => {
      const contactPhone = document.getElementById('contact_phonenumber')
      const justNumbers = /[A-Z]/gi

      if (justNumbers.test(contactPhone.value)) {
        const contactPhoneCont = document.getElementById('contactPhoneCont')
        const contactFormMessage = document.querySelector('.new__form-message')

        contactPhoneCont.style.border = '1px solid #F32424'
        contactFormMessage.style.display = 'block'
        contactFormMessage.innerHTML = 'Do not enter letters!'

        e.preventDefault()
      }
    })
  }

  /* Hide error | success messages */
  const errorMessage = document.querySelector('.error__message')
  const successMessage = document.querySelector('.principal__message')

  if (errorMessage) {
    const errorMessageCloseBtn = document.querySelector('.error__message-icon')

    errorMessageCloseBtn.addEventListener('click', () => {
      errorMessage.style.display = 'none'
    })
  }

  if (successMessage) {
    const successMessageCloseBtn = document.querySelector('.principal__message-icon')

    successMessageCloseBtn.addEventListener('click', () => {
      successMessage.style.display = 'none'
    })
  }

  /* Show form inputs */
  const usernameLabel = document.getElementById('usernameLabel'),
    emailLabel = document.getElementById('emailLabel'),
    passwordLabel = document.getElementById('passwordLabel'),
    passwordAgainLabel = document.getElementById('passwordAgainLabel')

  if (usernameLabel && emailLabel && passwordLabel && passwordAgainLabel) {
    const username = document.getElementById('username'),
      email = document.getElementById('email'),
      password = document.getElementById('password'),
      passwordAgain = document.getElementById('password_again')

    const usernameCont = document.getElementById('usernameCont'),
      emailCont = document.getElementById('emailCont'),
      passwordCont = document.getElementById('passwordCont'),
      passwordAgainCont = document.getElementById('passwordAgainCont')

    usernameLabel.addEventListener('click', () => {
      username.classList.toggle('show-input')
      usernameLabel.classList.toggle('change-label')
      usernameCont.classList.toggle('change-input-container')
    })

    emailLabel.addEventListener('click', () => {
      email.classList.toggle('show-input')
      emailLabel.classList.toggle('change-label')
      emailCont.classList.toggle('change-input-container')
    })

    passwordLabel.addEventListener('click', () => {
      password.classList.toggle('show-input')
      passwordLabel.classList.toggle('change-label')
      passwordCont.classList.toggle('change-input-container')
    })

    passwordAgainLabel.addEventListener('click', () => {
      passwordAgain.classList.toggle('show-input')
      passwordAgainLabel.classList.toggle('change-label')
      passwordAgainCont.classList.toggle('change-input-container')
    })
  } else if (usernameLabel && passwordLabel) {
    const username = document.getElementById('username'),
      password = document.getElementById('password')

    const usernameCont = document.getElementById('usernameCont'),
      passwordCont = document.getElementById('passwordCont')

    usernameLabel.addEventListener('click', () => {
      username.classList.toggle('show-input')
      usernameLabel.classList.toggle('change-label')
      usernameCont.classList.toggle('change-input-container')
    })

    passwordLabel.addEventListener('click', () => {
      password.classList.toggle('show-input')
      passwordLabel.classList.toggle('change-label')
      passwordCont.classList.toggle('change-input-container')
    })
  }
})

