# Instagram Clone Project Documentation

instagram-clone/
│
├── ig_prj/ # Main project directory
│ ├── **init**.py
│ ├── settings.py # Project settings and configurations
│ ├── urls.py # Main URL routing
│ ├── wsgi.py # WSGI configuration
│ └── asgi.py # ASGI configuration
│
├── authy/ # Authentication and User Profile app
│ ├── migrations/
│ ├── templates/
│ ├── models.py # User Profile models
│ ├── forms.py # User forms
│ ├── urls.py
│ └── views.py
│
├── post/ # Post handling app
│ ├── migrations/
│ ├── templates/
│ ├── models.py # Post and related models
│ ├── forms.py # Post forms
│ ├── urls.py
│ └── views.py
│
├── comment/ # Comment handling app
│ ├── migrations/
│ ├── templates/
│ ├── models.py # Comment models
│ ├── forms.py
│ ├── urls.py
│ └── views.py
│
├── directs/ # Direct messaging app
│ ├── migrations/
│ ├── templates/
│ ├── models.py # Message models
│ ├── forms.py
│ ├── urls.py
│ └── views.py
│

├── notification/ # Notification system app
│ ├── migrations/
│ ├── templates/
│ ├── models.py # Notification models
│ ├── urls.py
│ └── views.py
│
├── static/ # Static files directory
│ ├── css/
│ ├── js/
│ └── images/
│
├── media/ # User uploaded content
│
├── templates/ # Global templates
│ ├── base.html
│ └── includes/
│
├── manage.py # Django management script
│
└─requirements.txt # Project dependencies

## Project Overview

A Django-based web application that replicates core Instagram functionality. The project is structured with multiple apps to handle different features and uses Django's built-in authentication system.

Technical Stack
• Framework: Django 3.1
• Database: Default Django SQLite
• Frontend: Django Templates with Crispy Forms
• Static File Handling: WhiteNoise
• Deployment: Heroku-ready

## Core Applications

### 1. Post App

Handles all post-related functionality including:
• Image uploads
• Post creation and management
• Feed display
• Like/unlike functionality

### 2. Authy App

Manages user authentication and profiles:
• User registration
• Profile management
• User settings
• Profile customization

### 3. Comment App

Handles the post commenting system:
• Comment creation
• Comment display
• Comment management

### 4. Directs App

Manages private messaging functionality:
• Direct message sending
• Message inbox
• Conversation threading

### 5. Notification App

Handles user notifications for:
• Likes
• Comments
• Follow requests
• Direct messages

## Key Features

• User authentication and authorization
• Image posting and sharing
• User following system
• Direct messaging between users
• Real-time notifications
• Profile customization
• Feed generation
• Comment system
• Like system

## Configuration

• Debug mode enabled for development
• Configured for Heroku deployment
• WhiteNoise middleware for static files
• Supports both local development (127.0.0.1) and production deployment
• Uses Django's humanize for better date/time display

## Security Features

• CSRF protection enabled
• Django's built-in security middleware
• Session handling
• Authentication middleware

## Architecture and Structure

Each app follows Django's MVT (Model-View-Template) architecture:
• Models define the data structure.
• Views contain the business logic.
• Templates handle the presentation layer.

### The project uses:

• Crispy Forms for enhanced form rendering.
• Django's built-in authentication system.
• Static file serving with WhiteNoise.
• Template inheritance with a base template.
• Separate apps for modular functionality.

### This structure allows for:

• Clean separation of concerns.
• Easy maintenance and scalability.
• Modular development.
• Clear organization of features.
• Efficient code reuse.
