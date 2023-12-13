from app.services import UserService, SecurityService
from sqlalchemy.orm.exc import NoResultFound


class AuthService:
    """
    Este servicio se encarga de manejar la lógica de negocio referida a la autenticación.
    """
    def __init__(self):
        self.user_service = UserService()

    def register(self, user):
        if self.existence(user.email_address):
            return None
        else:
            user.password = SecurityService.generate_password(user.password)
            return self.user_service.create(user)

    def login(self, email, password):
        if self.existence(email):
            user = self.user_service.find_by_email(email)
            if SecurityService.check_password(user.password, password):
                return "token"
            else:
                return None
        else:
            return None

    def existence(self, email):
        try:
            self.user_service.find_by_email(email)
            return True
        except NoResultFound:
            return False