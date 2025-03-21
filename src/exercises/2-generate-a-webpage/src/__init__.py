from pathlib import Path
from sys import path


from flask import Flask


CURRENT_PATH = Path(__file__).parent
path.append(str(CURRENT_PATH))


from routes import bp  # noqa


def create_app():
    app = Flask(
        __name__,
        template_folder=str(CURRENT_PATH.joinpath("templates")))

    app.register_blueprint(bp)

    return app
