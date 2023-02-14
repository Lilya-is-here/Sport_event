# Sport_event
Sport event - букмекерская контора, которая выводит коэффициенты других букмекерских контор

## Установка

1. Клонируйте репозиторий, создайте виртуальное окружение
2. Установите зависимости `pip install -r requirements.txt`
3. Создайте файл config.py и создайте в нем переменные:

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
    basedir, "..", "webapp.db")

### Сгенерируйте 2 случайные строки и вставьте их как значения SECURITY_PASSWORD_SALT и SECRET_KEY:

SECRET_KEY = ""

SECURITY_PASSWORD_SALT = ""

SECURITY_PASSWORD_HASH = "sha512_crypt"

REMEMBER_COOKIE_DURATION = timedelta(days=5)

### Создайте переменные для Flask Security settings
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = True
SECURITY_REGISTER_URL = '/security/register'
SECURITY_CONFIRMABLE = True
SECURITY_CONFIRM_URL = "/confirm"
SECURITY_EMAIL_SUBJECT_CONFIRM = "Please confirm your email."
SECURITY_LOGIN_URL = '/security/login'
SECURITY_LOGOUT_URL = '/logout'
SECURITY_USERNAME_ENABLE = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECURITY_EMAIL_SENDER = 'no-reply@localhost'
SECURITY_SEND_REGISTER_EMAIL = True

### Flask_Mail
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = 'EMAIL_USER'
MAIL_PASSWORD = 'EMAIL_PASSWORD'
DEBUG = True

MAIL_DEFAULT_SENDER = MAIL_USERNAME

- Если у Вашего Gmail аккаунта есть двухэтапная аутентификация (https://support.google.com/accounts/topic/28786?hl=en&ref_topic=3382253), Google запретит доступ. Используйте пароль приложения(https://support.google.com/accounts/answer/185833?hl=en).

4. Запустите приложение командой "./run.sh"