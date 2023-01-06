from flask import Blueprint, Response

from src.configuration.config import APP_NAME_SPOT_HIT
from src.operation_tailing.spot_hit.process import SpotHit

app_spot_hit = Blueprint(APP_NAME_SPOT_HIT, __name__)

@app_spot_hit.route('/spotHit', methods=['POST'])
def spot_hit():

    print("SPOT HIT")

    cosmostats = SpotHit()
    response = cosmostats.process_aggregated_dlrs()

    return Response(response=response, status=200, mimetype="application/json")

