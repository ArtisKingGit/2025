document.getElementById('registration-form').addEventListener('submit', function (e) {
    e.preventDefault();
  
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const passwordConfirm = document.getElementById('password-confirm').value;
  
    if (password !== passwordConfirm) {
      alert('Passwords do not match!');
      return;
    }
  
    if (username.length < 8 || username.length > 14 || password.length < 8 || password.length > 14) {
      alert('Username and password must be between 8 and 14 characters.');
      return;
    }
  
    // Simulate registration success
    alert('Registration successful!');
    redirectToLogin();
  });
  
  function redirectToLogin() {
    // Redirect to the login page
    window.location.href = 'login.html';
  }
  