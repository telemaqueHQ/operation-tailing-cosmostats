from pymongo import MongoClient
import pandas as pd


class MongoDB():

    def __init__(self, uri):

        self.cnx = MongoClient(uri)

    def close_connexion(self):

        self.cnx.close()

    def get_mongo_aggregate_in_df(self, pipeline, database, collection):

        aggregate_df = pd.DataFrame(self.cnx[database][collection].aggregate(pipeline))

        return aggregate_df

    def get_mongo_find_in_df(self, filters, fields, database, collection):

        df = pd.DataFrame(self.cnx[database][collection].find(filters,fields))

        return df


