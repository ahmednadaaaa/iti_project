
// Tab switching functionality
const profileMenu = document.querySelectorAll('.profile-menu a');
const contentTabs = document.querySelectorAll('.content-tab');

profileMenu.forEach(menuItem => {
    menuItem.addEventListener('click', function (e) {
        e.preventDefault();

        // Remove active class from all menu items
        profileMenu.forEach(item => item.classList.remove('active'));

        // Add active class to clicked menu item
        this.classList.add('active');

        // Hide all content tabs
        contentTabs.forEach(tab => tab.classList.remove('active'));

        // Show the selected tab
        const tabId = this.getAttribute('data-tab');
        document.getElementById(tabId).classList.add('active');
    });
});

// Edit Profile button
document.getElementById('editProfileBtn').addEventListener('click', function () {
    // Switch to edit profile tab
    profileMenu.forEach(item => item.classList.remove('active'));
    document.querySelector('.profile-menu a[data-tab="edit-profile"]').classList.add('active');

    contentTabs.forEach(tab => tab.classList.remove('active'));
    document.getElementById('edit-profile').classList.add('active');
});

// Delete Account functionality
document.getElementById('deleteAccountBtn').addEventListener('click', function () {
    const password = document.getElementById('confirmPassword').value;
    const confirmed = document.getElementById('confirmDelete').checked;

    if (!password) {
        alert('Please enter your password to confirm account deletion.');
        return;
    }

    if (!confirmed) {
        alert('Please confirm that you understand this action is irreversible.');
        return;
    }

    // Show confirmation modal
    document.getElementById('deleteModal').style.display = 'flex';
});

// Modal functionality
document.querySelector('.close-modal').addEventListener('click', function () {
    document.getElementById('deleteModal').style.display = 'none';
});

document.getElementById('cancelDelete').addEventListener('click', function () {
    document.getElementById('deleteModal').style.display = 'none';
});

document.getElementById('confirmDeleteBtn').addEventListener('click', function () {
    // In a real application, this would send a request to delete the account
    alert('Your account has been scheduled for deletion. You will receive a confirmation email shortly.');
    document.getElementById('deleteModal').style.display = 'none';
});

// Close modal when clicking outside
window.addEventListener('click', function (e) {
    if (e.target === document.getElementById('deleteModal')) {
        document.getElementById('deleteModal').style.display = 'none';
    }
});

// Edit form submission
document.querySelector('.edit-form').addEventListener('submit', function (e) {
    e.preventDefault();
    // In a real application, this would save the changes
    alert('Profile updated successfully!');
});
