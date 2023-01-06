
from src.configuration.config import *
from src.functions.functions import *
from src.databases.mysql import MySQL



class Elasticemail():

    def __init__(self):

        pass


    def process_aggregated_dlrs(self):

        aggregated_dlrs = get_last_minute_dlrs(URL_OPERATION_TAILING_ELASTICEMAIL)
        
        con = MySQL(COSMOSTATS)
        con.upsert_dataframe("`operation_tailing`.`elasticemail`", aggregated_dlrs)
        
        return "elasticemail done"
