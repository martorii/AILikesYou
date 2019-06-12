import mysql.connector as mysqlconn
import pandas as pd


def select(query):
    ddbb = mysqlconn.connect(
    host="localhost",
    user="App",
    passwd="63DCRZ2guwAdugnf",
    database="AILikeYou"
    )
    df = pd.read_sql(query, con=ddbb)
    return df

def execute(query):
    ddbb = mysqlconn.connect(
    host="localhost",
    user="App",
    passwd="63DCRZ2guwAdugnf",
    database="AILikeYou"
    )

    mycursor = ddbb.cursor()
    mycursor.execute(query)
    ddbb.commit()
    return