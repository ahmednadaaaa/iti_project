# Crowdfunding Platform

A comprehensive crowdfunding platform built with Django featuring a complete REST API, payment integration, and user management system.

## Features

### Project Management
- Create and edit crowdfunding projects
- Categorize projects with categories and tags
- Upload multiple images per project
- Track funding progress with percentage calculations
- Cancel projects (with specific conditions)
- Featured and latest project displays
- Project search and filtering capabilities

### Donation System
- Make donations to projects
- Multiple payment methods (Credit Card/Debit Card/Cash)
- Secure payment processing with card validation
- Donation tracking and history
- Payment confirmation system

### User Interaction
- User registration and authentication
- Profile management with custom fields
- Project rating system (1-5 stars)
- Comment system with nested replies
- Report system for projects and comments
- User dashboard with projects and donations

### API Integration
- Complete REST API for all models
- CRUD operations for all entities
- Filtering and searching capabilities
- Pagination support
- Authentication-based permissions

## Technology Stack

### Backend
- **Django** - Web framework
- **Django REST Framework** - API development
- **Pillow** - Image processing
- **django-filter** - Advanced filtering
- **django-creditcards** - Payment card validation

### Database Models
- User management with custom Customer profiles
- Project with categories, tags, and images
- Donation and payment tracking
- Rating and comment systems
- Reporting functionality

## Project Structure

```
crowdfunding/
├── models.py          # Database models
├── views.py           # Web views
├── api.py            # REST API views
├── serializers.py    # API serializers
├── forms.py          # Django forms
├── filters.py        # Search and filter logic
├── urls.py           # URL routing
└── templates/        # HTML templates

accounts/
├── models.py         # User profile models
├── views.py          # Authentication views
├── forms.py          # User forms
├── signals.py        # User creation signals
└── decorators.py     # Authentication decorators
```

## Models Overview

### Core Models
- **Category** - Project categorization
- **Tag** - Project tagging system
- **Project** - Main crowdfunding projects
- **ProjectImage** - Multiple images per project
- **Donation** - User donations to projects
- **Rating** - Project rating system
- **Comment** - Project comments with replies

### Payment Models
- **Payment** - Card payment processing
- **CashPayment** - Cash payment handling

### Reporting Models
- **ProjectReport** - Report inappropriate projects
- **CommentReport** - Report inappropriate comments

### User Models
- **Customer** - Extended user profiles with additional fields

## Key Features Implementation

### Project Logic
- Automatic donation percentage calculation
- Average rating computation
- Days remaining calculation
- Project cancellation rules (< 25% funded)
- Featured project system

### Payment Processing
- Credit/debit card validation
- Secure payment form handling
- Payment confirmation workflow
- Cash payment option with confirmation

### Search and Filtering
- Title-based search
- Category filtering
- Project status filtering (Active/Completed/Upcoming)
- Sorting options (Newest, Most Funded, etc.)

### Security Features
- User authentication required for sensitive operations
- Permission-based API access
- Input validation and sanitization
- Secure payment data handling

## API Endpoints

### Projects
- `GET/POST /api/projects/` - List/Create projects
- `GET/PUT/DELETE /api/projects/<id>/` - Project details

### Donations
- `GET/POST /api/donations/` - List/Create donations
- `GET/PUT/DELETE /api/donations/<id>/` - Donation details

### Categories & Tags
- `GET/POST /api/categories/` - Manage categories
- `GET/POST /api/tags/` - Manage tags

### User Interactions
- `GET/POST /api/ratings/` - Project ratings
- `GET/POST /api/comments/` - Project comments
- `GET/POST /api/project-reports/` - Report projects
- `GET/POST /api/comment-reports/` - Report comments

### Payments
- `GET/POST /api/payments/` - Card payments
- `GET/POST /api/cash-payments/` - Cash payments

## Web Interface

### Public Pages
- Homepage with featured/latest projects
- Project detail pages
- Project search and filtering
- User registration/login

### Authenticated Features
- Create new projects
- Make donations
- Rate and comment on projects
- User profile management
- Project management dashboard

## Installation & Setup

### Prerequisites
```bash
pip install django
pip install djangorestframework
pip install Pillow
pip install django-filter
pip install django-creditcards
pip install django-import-export
```

### Database Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

### Running the Server
```bash
python manage.py runserver
```

## Usage Examples

### Creating a Project
Users can create projects through the web interface or API with title, description, funding target, timeline, and images.

### Making Donations
Donors can contribute to projects using credit cards or cash payments, with secure payment processing.

### Project Interaction
Users can rate projects, leave comments, and report inappropriate content.

## Security Considerations

- All payment data is validated using django-creditcards
- User authentication required for sensitive operations
- Input sanitization and validation
- Permission-based API access control

## Future Enhancements

- Email notifications for project updates
- Social media integration
- Advanced analytics dashboard
- Mobile app API extensions
- Multi-currency support

---

This platform provides a complete crowdfunding solution with robust backend functionality, secure payment processing, and comprehensive user interaction features.
