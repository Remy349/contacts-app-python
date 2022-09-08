document.addEventListener('DOMContentLoaded', () => {
  /* Hide error messages */
  const errorMessage = document.querySelector('.error__message')

  if (errorMessage) {
    const errorMessageCloseBtn = document.querySelector('.error__message-icon')

    errorMessageCloseBtn.addEventListener('click', () => {
      errorMessage.style.display = 'none'
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

