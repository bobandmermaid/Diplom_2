class Constants:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api/'
    REGISTER_URL = f'{BASE_URL}auth/register'
    USER_LOGIN_URL = f'{BASE_URL}auth/login'
    USER_EDIT_URL = f'{BASE_URL}auth/user'
    INGREDIENTS_URL = f'{BASE_URL}ingredients'
    ORDER_URL = f'{BASE_URL}orders'

    ERROR_RESPONSES_AUTH = 'You should be authorised'
    ERROR_RESPONSES_INGREDIENT = 'Ingredient ids must be provided'
    ERROR_PASSWORD_EMAIL = 'email or password are incorrect'
    ERROR_PASSWORD_EMAIL_NAME_REQ = 'Email, password and name are required fields'
    ERROR_USER_EXISTS = 'User already exists'
