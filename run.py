from waitress import serve
from main import create_app
from main.utils.config import Config


app = create_app()
serve(
    app,
    host=Config.get('IP_APLICACAO'),
    port=Config.get('PORTA_APLICACAO')
)
