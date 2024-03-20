import pandas as pd
from b2sdk.v2 import *
from dotenv import load_dotenv
import os

load_dotenv()

def authenticate():

    info = InMemoryAccountInfo()
    b2_api = B2Api(info)

    application_key_id = os.getenv("KEY_ID")
    application_key = os.getenv("APPLICATION_KEY")

    b2_api.authorize_account("production", application_key_id, application_key)

    return b2_api


def getDataFrame(file_name):
    b2_api = authenticate()

    bucket_name = os.getenv("BUCKET_NAME")
    bucket = b2_api.get_bucket_by_name(bucket_name)

    file_name = "processed-data.csv"
    downloaded_file = bucket.download_file_by_name(file_name)

    local_file = os.path.join(os.getcwd(), file_name)
    downloaded_file.save_to(local_file)

    df = pd.read_csv(local_file)

    return df

def processTags(tags):
    processed_tags = tags[2:-2].replace("'", "").split(",")
    processed_tags = list(map(str.strip, processed_tags))
    
    return processed_tags