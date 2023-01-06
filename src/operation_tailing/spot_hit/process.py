
from src.configuration.config import *
from src.functions.functions import *
from src.databases.mysql import MySQL


class SpotHit():

    def __init__(self):

        pass


    def process_aggregated_dlrs(self):

        aggregated_dlrs = get_last_minute_dlrs(URL_OPERATION_TAILING_SPOT_HIT)
        
        con = MySQL(COSMOSTATS)
        con.upsert_dataframe("`operation_tailing`.`spot_hit`", aggregated_dlrs)
        con.upsert_dataframe("`operation_tailing`.`sms`", aggregated_dlrs)
        
        return "spot hit done"