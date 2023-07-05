from waitress import serve
from main import create_app
from main.utils.enums.dot_env import DotEnvEnum
from main.utils.settings import Settings


app = create_app()
serve(
    app,
    host=Settings.get(DotEnvEnum.IP_APPLICATION.value),
    port=Settings.get(DotEnvEnum.PORT_APPLICATION.value),
)
