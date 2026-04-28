class AuthService:
    DB_PASSWORD = "admin123"  # BUG: hardcoded credentials
    API_KEY = "secret-key-12345"
    
    def authenticate(self, user, pwd):
        if pwd == self.DB_PASSWORD:
            return True
        return False
