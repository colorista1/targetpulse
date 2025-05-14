document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.getElementById('registerForm');
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirm_password');
    const email = document.getElementById('email');
    const username = document.getElementById('username');

    // Function to show error message
    function showError(input, message) {
        const formGroup = input.parentElement;
        const errorDiv = formGroup.querySelector('.error-message') || document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.textContent = message;
        if (!formGroup.querySelector('.error-message')) {
            formGroup.appendChild(errorDiv);
        }
        input.classList.add('error');
    }

    // Function to clear error message
    function clearError(input) {
        const formGroup = input.parentElement;
        const errorDiv = formGroup.querySelector('.error-message');
        if (errorDiv) {
            errorDiv.remove();
        }
        input.classList.remove('error');
    }

    // Validate email format
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email.value.trim());
    }

    // Validate password strength
    function validatePassword(password) {
        // At least 8 characters, 1 uppercase, 1 lowercase, 1 number
        const re = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;
        return re.test(password.value);
    }

    // Real-time validation
    username.addEventListener('input', function() {
        clearError(username);
        if (username.value.length < 3) {
            showError(username, 'Имя пользователя должно содержать минимум 3 символа');
        }
    });

    email.addEventListener('input', function() {
        clearError(email);
        if (!validateEmail(email)) {
            showError(email, 'Пожалуйста, введите корректный email');
        }
    });

    password.addEventListener('input', function() {
        clearError(password);
        if (!validatePassword(password)) {
            showError(password, 'Пароль должен содержать минимум 8 символов, включая заглавные и строчные буквы, и цифры');
        }
    });

    confirmPassword.addEventListener('input', function() {
        clearError(confirmPassword);
        if (confirmPassword.value !== password.value) {
            showError(confirmPassword, 'Пароли не совпадают');
        }
    });

    // Form submission
    registerForm.addEventListener('submit', function(e) {
        let isValid = true;

        // Validate username
        if (username.value.length < 3) {
            showError(username, 'Имя пользователя должно содержать минимум 3 символа');
            isValid = false;
        }

        // Validate email
        if (!validateEmail(email)) {
            showError(email, 'Пожалуйста, введите корректный email');
            isValid = false;
        }

        // Validate password
        if (!validatePassword(password)) {
            showError(password, 'Пароль должен содержать минимум 8 символов, включая заглавные и строчные буквы, и цифры');
            isValid = false;
        }

        // Validate password confirmation
        if (confirmPassword.value !== password.value) {
            showError(confirmPassword, 'Пароли не совпадают');
            isValid = false;
        }

        if (!isValid) {
            e.preventDefault();
        }
    });
}); 