import pandas as pd
import psycopg2
import psycopg2.extras as extras


import psycopg2
import numpy as np
import psycopg2.extras as extras
import pandas as pd


def execute_values(conn, df, table):
    tuples = [tuple(x) for x in df.to_numpy()]

    cols = ",".join(list(df.columns))
    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("The dataframe is inserted")
    cursor.close()


df = pd.read_csv("HINDALCO_1D.csv", parse_dates=["datetime"])

conn = psycopg2.connect(
    host="172.18.0.3", database="stock", user="postgres", password="changeme"
)

execute_values(conn, df, "stock_prices")


conn.autocommit = True
cursor = conn.cursor()

sql1 = """select * from stock_prices;"""
cursor.execute(sql1)
for i in cursor.fetchall():
    print(i)
