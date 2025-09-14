# Permissions & Groups Setup

This project demonstrates Django groups and permissions.

## Custom Permissions
Defined in `Book` model:
- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

## Groups
- **Viewers**: can_view
- **Editors**: can_view, can_create, can_edit
- **Admins**: all permissions

## How to Setup
1. Run migrations to apply permissions:
   ```bash
   python manage.py migrate
