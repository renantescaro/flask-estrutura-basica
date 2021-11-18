from waitress import serve
from flaskr import create_app
from flaskr.utils.config import Config


app = create_app()
serve(app, host=Config.get('IP_APLICACAO'), port=Config.get('PORTA_APLICACAO'))