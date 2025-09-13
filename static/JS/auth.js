// static/js/auth.js
document.addEventListener('DOMContentLoaded', function () {
    const authTabs = document.querySelectorAll('.auth-tab');
    const authForms = document.querySelectorAll('.auth-form');

    // Tabs switch
    if (authTabs.length && authForms.length) {
        authTabs.forEach(tab => {
            tab.addEventListener('click', function () {
                const tabId = this.dataset.tab; // safer than getAttribute

                // Update active tab
                authTabs.forEach(t => t.classList.remove('active'));
                this.classList.add('active');

                // Show corresponding form
                authForms.forEach(form => {
                    form.classList.remove('active');
                    if (form.id === `${tabId}Form`) {
                        form.classList.add('active');
                    }
                });
            });
        });
    }

    // Links that switch forms
    const switchToRegister = document.getElementById('switchToRegister');
    if (switchToRegister && authTabs[1]) {
        switchToRegister.addEventListener('click', function (e) {
            e.preventDefault();
            authTabs[1].click();
        });
    }

    const switchToLogin = document.getElementById('switchToLogin');
    if (switchToLogin && authTabs[0]) {
        switchToLogin.addEventListener('click', function (e) {
            e.preventDefault();
            authTabs[0].click();
        });
    }

    // Top nav buttons
    const loginTopBtn = document.getElementById('loginTopBtn');
    if (loginTopBtn && authTabs[0]) {
        loginTopBtn.addEventListener('click', () => authTabs[0].click());
    }
    const registerTopBtn = document.getElementById('registerTopBtn');
    if (registerTopBtn && authTabs[1]) {
        registerTopBtn.addEventListener('click', () => authTabs[1].click());
    }

    // Password toggle helper
    function togglePassword(toggleId, inputId) {
        const toggle = document.getElementById(toggleId);
        const input = document.getElementById(inputId);
        if (!toggle || !input) return;
        toggle.addEventListener('click', function () {
            const type = input.getAttribute('type') === 'password' ? 'text' : 'password';
            input.setAttribute('type', type);
            const icon = this.querySelector('i');
            if (icon) {
                icon.classList.toggle('fa-eye');
                icon.classList.toggle('fa-eye-slash');
            }
        });
    }
    togglePassword('toggleLoginPassword', 'loginPassword');
    togglePassword('toggleRegisterPassword', 'registerPassword');
    togglePassword('toggleConfirmPassword', 'confirmPassword');

    // Login form submit (safe)
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function (e) {
            e.preventDefault();
            // TODO: send to backend or validate properly
            alert('Login successful! Redirecting to your dashboard...');
        });
    }

    // Register form submit (safe)
    const registerForm = document.getElementById('registerForm');
    if (registerForm) {
        registerForm.addEventListener('submit', function (e) {
            e.preventDefault();
            const passwordEl = document.getElementById('registerPassword');
            const confirmEl = document.getElementById('confirmPassword');
            const termsEl = document.getElementById('terms');

            const password = passwordEl ? passwordEl.value : '';
            const confirmPassword = confirmEl ? confirmEl.value : '';

            if (password !== confirmPassword) {
                alert('Passwords do not match!');
                return;
            }

            if (!termsEl || !termsEl.checked) {
                alert('You must agree to the Terms of Service and Privacy Policy');
                return;
            }

            // TODO: real submission
            alert('Account created successfully! Please check your email for verification.');
        });
    }

    // Egyptian phone validation
    const mobile = document.getElementById('mobile');
    if (mobile) {
        mobile.addEventListener('blur', function () {
            const phone = this.value.trim();
            const regex = /^01[0125][0-9]{8}$/;
            if (phone && !regex.test(phone)) {
                alert('Please enter a valid Egyptian phone number (e.g., 01X XXXXXXX)');
                this.focus();
            }
        });
    }
});
