# Importing packages
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

## Load environment variables
load_dotenv()

## Login info
mysql_host = os.getenv("HOSTNAME_SQL")
mysql_user = os.getenv("USERNAME_SQL")
mysql_password = os.getenv("PASSWORD_SQL")
mysql_database = os.getenv("DATABASE_SQL")

# Connection string
connection = f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_database}'
db = create_engine(connection)

# Query
query = 'SELECT * FROM db2.table2;'
query
df = pd.read_sql(query, con=db)

# Create dataframe
devicesDF = pd.read_csv('https://raw.githubusercontent.com/crisrib/HHA-507-2022/main/ingestion/example_files/csv/synthetic/devices.csv')
devicesDF

# Import dataframe to mySQL
devicesDF.to_sql('table2', con=db, if_exists='replace', index=False)

## Testing query results
sql_query = """ SELECT * FROM table3 WHERE age = '47' """;
results_47 = pd.read_sql(sql_query, con=db)
results_47

df = pd.read_sql("""
SELECT * FROM db2.table2;""", con=db)