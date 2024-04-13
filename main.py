from app_manager import PasswordManagerApp
from password_generator import PasswordGenerator

if __name__ == "__main__":
    password_generator = PasswordGenerator()
    app_manager = PasswordManagerApp(password_generator)

    app_manager.run()
