
// Star rating functionality
const stars = document.querySelectorAll('.star');
let currentRating = 0;

stars.forEach(star => {
    star.addEventListener('click', function () {
        const value = parseInt(this.getAttribute('data-value'));
        currentRating = value;

        stars.forEach(s => {
            if (parseInt(s.getAttribute('data-value')) <= value) {
                s.classList.add('active');
            } else {
                s.classList.remove('active');
            }
        });
    });

    star.addEventListener('mouseover', function () {
        const value = parseInt(this.getAttribute('data-value'));

        stars.forEach(s => {
            if (parseInt(s.getAttribute('data-value')) <= value) {
                s.style.color = '#f6c23e';
            } else {
                s.style.color = '#ddd';
            }
        });
    });

    star.addEventListener('mouseout', function () {
        stars.forEach(s => {
            if (parseInt(s.getAttribute('data-value')) > currentRating) {
                s.style.color = '#ddd';
            }
        });
    });
});

// Report functionality
const reportButtons = document.querySelectorAll('.report-action');

reportButtons.forEach(button => {
    button.addEventListener('click', function () {
        const comment = this.closest('.comment');
        const author = comment.querySelector('.comment-author').textContent;

        if (confirm(`Report comment by ${author}?`)) {
            alert('Thank you for reporting. Our team will review this comment.');
            // In a real application, this would send a report to the backend
        }
    });
});

// Comment form functionality
const commentForm = document.querySelector('.comment-form');
const commentTextarea = commentForm.querySelector('textarea');
const commentButton = commentForm.querySelector('.btn');

commentButton.addEventListener('click', function () {
    if (commentTextarea.value.trim() === '') {
        alert('Please enter a comment before posting.');
        return;
    }

    // In a real application, this would send the comment to the backend
    alert('Comment posted successfully!');
    commentTextarea.value = '';
});
