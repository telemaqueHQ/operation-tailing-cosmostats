import mysql.connector
import pandas as pd
import simplejson

import time

class MySQL:
    
    def __init__(self, configuration):

        self.cnx = mysql.connector.connect(**configuration)
        

    def close_connection(self):

        self.cnx.close()
        

    def cursor(self, dictionary=False):

        cursor = self.cnx.cursor(dictionary=dictionary)
        return cursor
    

    def execute_query(self, query):

        cursor = self.cursor(dictionary=True)
        cursor.execute(query)
        cursor.close()


    def sql_table_to_json(self, sql_select_query):

        cursor = self.cursor(dictionary=True)
        cursor.execute(sql_select_query)
        json_table = cursor.fetchall()

        cursor.close()

        return simplejson.dumps(json_table, use_decimal=True)


    def sql_table_to_dataframe(self, sql_query):

        dataframe = pd.read_sql_query(sql_query, self.cnx)
        return dataframe


    def upsert_dataframe(self, table_name, dataframe_to_insert):

        print("UPSERT")
        
        ## creation dynamique de la query / a ameliorer
        cols = ""
        duplicate_key_update = ""
        for col in dataframe_to_insert.columns:
            cols = cols + "`" + col + "`,"
            if col != "dialboxCallId":
                duplicate_key_update = duplicate_key_update + "`" + col + "`" + "=VALUES(" + "`" + col + "`" + ")," 
            
        cols = cols[:-1]
        duplicate_key_update = duplicate_key_update[:-1]
        values = "%s,"*(len(dataframe_to_insert.columns))
        values = values[:-1]

        upsert_query = "INSERT INTO {table_name} (" + cols + ") VALUES (" + values + ") ON DUPLICATE KEY UPDATE " + duplicate_key_update
        upsert_query = upsert_query.format(table_name=table_name)

        ## upsert
        cursor = self.cursor()
        records_to_insert = list(dataframe_to_insert.itertuples(index=False, name=None))
        cursor.executemany(upsert_query, records_to_insert)
        cursor.close()

        return dataframe_to_insert.to_json(orient="records")


    def insertion(self, df_to_insert, query):
        cursor = self.cnx.cursor()
        records_to_insert = list(df_to_insert.itertuples(index=False, name=None))
        cursor.executemany(query, records_to_insert)
        self.cnx.commit()     
        if self.cnx.is_connected():
            cursor.close()
            self.close_connection()


    def insert_dataframe(self, table_name, dataframe_to_insert):

        print("INSERT")
        start_time = time.time()
        
        cols = ""
        for col in dataframe_to_insert.columns:
            cols = cols + "`" + col + "`,"

        cols = cols[:-1]
        values = "%s,"*(len(dataframe_to_insert.columns))
        values = values[:-1]

        insert_query = "INSERT INTO {table_name} (" + cols + ") VALUES (" + values + ")"
        insert_query = insert_query.format(table_name=table_name)

        cursor = self.cursor()
        records_to_insert = list(dataframe_to_insert.itertuples(index=False, name=None))
        print("step1 done")
        print("--- %s seconds ---" % (time.time() - start_time))
        cursor.executemany(insert_query, records_to_insert)
        print("step2 done")
        print("--- %s seconds ---" % (time.time() - start_time))
        cursor.close()


    def truncate_table(self, table_name):

        print("TRUNCATE")

        truncate_query = """
        TRUNCATE TABLE {table_name}
        """.format(table_name=table_name)

        cursor = self.cursor(dictionary=True)
        cursor.execute(truncate_query)
        cursor.close()

