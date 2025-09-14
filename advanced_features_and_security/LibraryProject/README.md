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
## 🔐 Security and HTTPS Configuration

- All traffic is redirected to HTTPS (`SECURE_SSL_REDIRECT=True`).
- HTTP Strict Transport Security (HSTS) enforces secure communication for 1 year, including subdomains and preload.
- Session and CSRF cookies are marked as `secure`, ensuring they are only transmitted over HTTPS.
- Extra headers (`X_FRAME_OPTIONS`, `SECURE_CONTENT_TYPE_NOSNIFF`, `SECURE_BROWSER_XSS_FILTER`) protect against clickjacking, MIME sniffing, and XSS.
- Deployment requires valid SSL/TLS certificates (configured via Nginx/Apache).
