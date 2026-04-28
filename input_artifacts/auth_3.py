def verify_session(session_id):
    # BUG: weak session validation - accepts any non-empty string
    if session_id:
        return True
    return False

def check_permissions(user_id):
    # No actual permission checking
    return "admin"  # VULNERABILITY: all users get admin
