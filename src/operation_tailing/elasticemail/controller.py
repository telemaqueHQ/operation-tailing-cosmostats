from flask import Blueprint, Response

from src.configuration.config import APP_NAME_ELASTICEMAIL
from src.operation_tailing.elasticemail.process import Elasticemail

app_elasticemail = Blueprint(APP_NAME_ELASTICEMAIL, __name__)

@app_elasticemail.route('/elasticemail', methods=['POST'])
def elasticemail():

    cosmostats = Elasticemail()
    response = cosmostats.process_aggregated_dlrs()

    return Response(response=response, status=200, mimetype="application/json")

