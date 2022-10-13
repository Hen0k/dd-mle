"""
Functions to fetch the data from the DB.
"""

import os
import pandas as pd


def get_conn_string():
    """Gets a connection string to the database.
    """
    conn_string = f"postgresql+psycopg2://{os.environ['DS_DB_USER']}:{os.environ['DS_DB_PASSWORD']}@{os.environ['DB_HOSTNAME']}/companydata"
    return conn_string

def get_labels(indices: list):
    """Fetches the labels using a list of indices
    """
    indices = tuple(set(indices))
    if len(indices)==1:
            query = f"select * from labels where idx = {indices[0]}"
    else:
        query = f"select * from labels where idx in {indices}"

    print(query)
    dataset = pd.read_sql(
        query,
        get_conn_string()
    )

    return dataset