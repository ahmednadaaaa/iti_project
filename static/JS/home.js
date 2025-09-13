
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function (e) {
        e.preventDefault();

        // Remove active class from all links
        document.querySelectorAll('.nav-link').forEach(l => {
            l.classList.remove('active');
        });

        // Add active class to clicked link
        this.classList.add('active');

        // Hide all pages
        document.querySelectorAll('.page-content').forEach(page => {
            page.classList.remove('active');
        });

        // Show the selected page
        const pageId = this.getAttribute('data-page');
        document.getElementById(pageId).classList.add('active');

        // Scroll to top
        window.scrollTo(0, 0);
    });
});

// Footer navigation
document.querySelectorAll('.footer-links .nav-link').forEach(link => {
    link.addEventListener('click', function (e) {
        e.preventDefault();

        // Remove active class from all links
        document.querySelectorAll('.nav-link').forEach(l => {
            l.classList.remove('active');
        });

        // Add active class to clicked link
        document.querySelectorAll(`.nav-link[data-page="${this.getAttribute('data-page')}"]`).forEach(l => {
            l.classList.add('active');
        });

        // Hide all pages
        document.querySelectorAll('.page-content').forEach(page => {
            page.classList.remove('active');
        });

        // Show the selected page
        const pageId = this.getAttribute('data-page');
        document.getElementById(pageId).classList.add('active');

        // Scroll to top
        window.scrollTo(0, 0);
    });
});
