
from src.configuration.config import *
from src.functions.functions import *
from src.databases.mysql import MySQL


class BuzzExpert():

    def __init__(self):

        pass


    def process_aggregated_dlrs(self):

        aggregated_dlrs = get_last_minute_dlrs(URL_OPERATION_TAILING_BUZZ_EXPERT)

        SELECT_QUERY_MAX_DATE_BUZZ_EXPERT = """
        SELECT MAX(`datetime`) FROM `operation_tailing`.`buzz_expert`
        """
        con = MySQL(COSMOSTATS)
        max_date = con.sql_table_to_dataframe(SELECT_QUERY_MAX_DATE_BUZZ_EXPERT)
        aggregated_dlrs = aggregated_dlrs.loc[aggregated_dlrs["datetime"] > max_date]

        con.insert_dataframe("`operation_tailing`.`buzz_expert`", aggregated_dlrs)
        con.insert_dataframe("`operation_tailing`.`sms`", aggregated_dlrs)
        
        return "buzz_expert done"