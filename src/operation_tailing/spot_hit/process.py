
from src.configuration.config import *
from src.functions.functions import *
from src.databases.mysql import MySQL


class SpotHit():

    def __init__(self):

        pass


    def process_aggregated_dlrs(self):

        aggregated_dlrs = get_last_minute_dlrs(URL_OPERATION_TAILING_SPOT_HIT)

        SELECT_QUERY_MAX_DATE_SPOT_HIT = """
        SELECT MAX(`datetime`) FROM `operation_tailing`.`spot_hit`
        """
        con = MySQL(COSMOSTATS)
        max_date = con.sql_table_to_dataframe(SELECT_QUERY_MAX_DATE_SPOT_HIT)
        aggregated_dlrs = aggregated_dlrs.loc[aggregated_dlrs["datetime"] > max_date]
        
        con.insert_dataframe("`operation_tailing`.`spot_hit`", aggregated_dlrs)
        con.insert_dataframe("`operation_tailing`.`sms`", aggregated_dlrs)
        
        return "spot hit done"