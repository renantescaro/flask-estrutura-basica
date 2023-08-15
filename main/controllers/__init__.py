from .api_keys_ctrl import bp as apikey_bp
from .index_ctrl import bp as index_bp
from .login_ctrl import bp as login_bp
from .user_ctrl import bp as user_bp
from .user_group_ctrl import bp as user_group_bp
from .user_group_access_ctrl import bp as user_group_access_bp

blueprints_ctrl = [
    apikey_bp,
    index_bp,
    login_bp,
    user_bp,
    user_group_bp,
    user_group_access_bp,
]
