from ..services import UserService, SecurityService
from sqlalchemy.orm.exc import NoResultFound


class AuthService:
    def __init__(self):
        self.user_service = UserService()
        self.security_service = SecurityService()

    def register(self, user):
        if self.existence(user.email_address):
            return None
        else:
            user.password = self.security_service.generate_password(user.password)
            return self.user_service.create(user)

    def login(self, email, password):
        pass

    def existence(self, email):
        try:
            self.user_service.find_by_email(email)
            return True
        except NoResultFound:
            return False