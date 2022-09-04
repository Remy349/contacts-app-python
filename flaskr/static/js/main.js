document.addEventListener('DOMContentLoaded', () => {
  /* Hide error messages */
  const errorMessage = document.querySelector('.error__message')

  if (errorMessage) {
    const errorMessageCloseBtn = document.querySelector('.error__message-icon')

    errorMessageCloseBtn.addEventListener('click', () => {
      errorMessage.style.display = 'none'
    })
  }
})

