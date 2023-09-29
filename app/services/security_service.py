from werkzeug.security import generate_password_hash, check_password_hash

class SecurityService:

    """
    En este servicio van todas las funciones referidas a la seguridad.
    Generar un hash de una contraseña, comparar una contraseña con un hash.
    """

    
    @staticmethod
    def generate_password(password: str) -> str:
        """Genera un hash de una contraseña pasada por parámetro."""
        return generate_password_hash(password)
    
    @staticmethod
    def check_password(password1: str, password2: str) -> bool:
        """Compara los hashs de dos contraseñas."""
        return check_password_hash(password1, password2)