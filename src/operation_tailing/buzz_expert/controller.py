from flask import Blueprint, Response

from src.configuration.config import APP_NAME_BUZZ_EXPERT
from src.operation_tailing.buzz_expert.process import BuzzExpert

app_buzz_expert = Blueprint(APP_NAME_BUZZ_EXPERT, __name__)

@app_buzz_expert.route('/buzzExpert', methods=['POST'])
def buzz_expert():

    cosmostats = BuzzExpert()
    response = cosmostats.process_aggregated_dlrs()

    return Response(response=response, status=200, mimetype="application/json")

