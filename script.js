var loginForm = document.querySelector('.loginForm');
var signupForm = document.querySelector('.signupForm');
var loginLink = document.querySelector('.loginLink');
var signupLink = document.querySelector('.signupLink');

loginLink.addEventListener('click', function() {
  loginForm.classList.toggle('active');
  loginForm.classList.toggle('inactive');
  signupForm.classList.toggle('active');
  signupForm.classList.toggle('inactive');
});

signupLink.addEventListener('click', function() {
  loginForm.classList.toggle('active');
  loginForm.classList.toggle('inactive');
  signupForm.classList.toggle('active');
  signupForm.classList.toggle('inactive');
});