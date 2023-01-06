
import requests
import pandas as pd


def get_last_minute_dlrs(url):

        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)

        aggregated_dlrs = pd.json_normalize(response.json())

        aggregated_dlrs["source"] = aggregated_dlrs["key"].apply(lambda x: x.split("#")[0])
        aggregated_dlrs["product"] = aggregated_dlrs["key"].apply(lambda x: x.split("#")[1])
        aggregated_dlrs = aggregated_dlrs.explode("series")
        aggregated_dlrs["datetime"] = aggregated_dlrs["series"].apply(lambda x: x.get("date").replace("T", " ")[0:19])
        aggregated_dlrs["value"] = aggregated_dlrs["series"].apply(lambda x: x.get("length"))
        aggregated_dlrs = aggregated_dlrs[["source", "product", "datetime", "value"]]

        print(aggregated_dlrs.shape)
        
        return aggregated_dlrs