def send_email(email, message):
    # BUG: email not sanitized
    # VULNERABILITY: no validation or sanitization
    email_body = f"To: {email}\n\n{message}"
    return smtp_send(email_body)

def notify_user(user_email, notification):
    # Email injection possible
    headers = f"To: {user_email}\nCc: {user_email}"
    return send_mail(headers, notification)
