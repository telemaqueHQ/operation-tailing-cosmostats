from os import environ


## MYSQL
COSMOSTATS = {
    "user": environ.get("COSMOSTATS_USER"),
    "password": environ.get("COSMOSTATS_PASSWORD"),
    "host": environ.get("COSMOSTATS_HOST"),
    "port": 3306,
    "database": "switchboard",
    "charset": "utf8",
    "autocommit": True
}


APP_NAME_BUZZ_EXPERT = "BUZZ_EXPERT"
URL_OPERATION_TAILING_BUZZ_EXPERT = "https://dmp-team-monitoring-backend.private.prod.k8s.tlmq.fr/operation-tailing/last-minute-buzz-expert-dlrs"


APP_NAME_ELASTICEMAIL = "ELASTICEMAIL"
URL_OPERATION_TAILING_ELASTICEMAIL = "https://dmp-team-monitoring-backend.private.prod.k8s.tlmq.fr/operation-tailing/last-minute-elasticemail-tracking-logs"


APP_NAME_SPOT_HIT = "SPOT_HIT"
URL_OPERATION_TAILING_SPOT_HIT = "https://dmp-team-monitoring-backend.private.prod.k8s.tlmq.fr/operation-tailing/last-minute-spot-hit-dlrs"