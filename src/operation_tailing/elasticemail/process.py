
from src.configuration.config import *
from src.functions.functions import *
from src.databases.mysql import MySQL



class Elasticemail():

    def __init__(self):

        pass


    def process_aggregated_dlrs(self):

        aggregated_dlrs = get_last_minute_dlrs(URL_OPERATION_TAILING_ELASTICEMAIL)

        SELECT_QUERY_MAX_DATE_ELASTICEMAIL = """
        SELECT CAST(MAX(`datetime`) AS CHAR) FROM `operation_tailing`.`elasticemail`
        """
        con = MySQL(COSMOSTATS)
        max_date = con.sql_table_to_dataframe(SELECT_QUERY_MAX_DATE_ELASTICEMAIL)
        max_date = max_date["max_date"][0]
        aggregated_dlrs = aggregated_dlrs.loc[aggregated_dlrs["datetime"] > max_date]
        
        con.insert_dataframe("`operation_tailing`.`elasticemail`", aggregated_dlrs)
        
        return "elasticemail done"
