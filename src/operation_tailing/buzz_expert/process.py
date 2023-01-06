
from src.configuration.config import *
from src.functions.functions import *
from src.databases.mysql import MySQL


class BuzzExpert():

    def __init__(self):

        pass


    def process_aggregated_dlrs(self):

        aggregated_dlrs = get_last_minute_dlrs(URL_OPERATION_TAILING_BUZZ_EXPERT)
        
        con = MySQL(COSMOSTATS)
        con.upsert_dataframe("`operation_tailing`.`buzz_expert`", aggregated_dlrs)
        con.upsert_dataframe("`operation_tailing`.`sms`", aggregated_dlrs)
        
        return "buzz_expert done"