from .index_ctrl import bp as index_bp
from .person_ctrl import bp as person_bp
from .login_ctrl import bp as login_bp
from .user_ctrl import bp as user_bp

blueprints_ctrl = [
    index_bp,
    person_bp,
    login_bp,
    user_bp,
]
