from flask import Flask
from flask_cors import CORS

from src.operation_tailing.buzz_expert.controller import app_buzz_expert
from src.operation_tailing.elasticemail.controller import app_elasticemail
from src.operation_tailing.spot_hit.controller import app_spot_hit


APPS_LIST = [
    app_buzz_expert,
    app_elasticemail,
    app_spot_hit
]


def create_flask_app():

    main_app = Flask(__name__)
    cors = CORS(main_app)

    for app in APPS_LIST:
        main_app.register_blueprint(app)

    return main_app



