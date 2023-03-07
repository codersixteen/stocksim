import os


class Config(object):
    """Configuration for the app"""

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'postgresql:///stocksim_db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "secretkey_local")
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    API_KEY = "PK0GRC1UBR3JTTNCPQA6"
    API_SECRET_KEY = "qZEepGAYXleOWXlH4B7C3vzYuDgXNrsRVa3ymNxn"
