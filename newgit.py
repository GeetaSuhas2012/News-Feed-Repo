# ------------------------------------------------------------------------------
# Complete example of how to convert a csv to
# a pandas dataframe, and then to PostgreSQL
# ------------------------------------------------------------------------------
# Author: Naysan Saran, November 2019
# License: GPL V3.0
# ------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import psycopg2

def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    return conn


def single_insert(conn, insert_req):
    """ Execute a single INSERT request """
    cursor = conn.cursor()
    try:
        cursor.execute(insert_req)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    cursor.close()


def main():
    param_dic = {
        "host": "localhost",
        "database": "postgres",
        "user": "postgres",
        "password": "data123"

           }
       # Read the csv file
    csv_file = "NBC.csv"
    df = pd.read_csv(csv_file)
    # Connect to the database
    conn = connect(param_dic)
    # Create a list of tupples from the dataframe values
    cols = ','.join(list(df.columns))
    print(cols)
    for index, row in df.iterrows():
        query="""INSERT INTO fedds
                       (Link,Title,Pub_Date,Description)
        values(%s, %s, %s, %s)", row.Link, row.Title, row.Pub_Date, row.Description)"""
        single_insert(conn, query)

    print("All rows were sucessfully inserted in the emissions table")

    # Close the database connection
    conn.close()


if __name__ == "__main__":
   main()
