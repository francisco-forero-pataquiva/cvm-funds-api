import pandas as pd
import io
import csv
from server.db import engine

def populate_db(year):
    for n in range(1,13):
        scrap_date = f"{year}{str(n).zfill(2)}"
        print(f"Getting {scrap_date} data...")
        url = f"http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_{scrap_date}.csv"
        df = pd.read_csv(url, sep=";")
        print("Processing data...")
        df = df[["CNPJ_FUNDO","VL_QUOTA","DT_COMPTC"]]
        df["CNPJ_FUNDO"] = df["CNPJ_FUNDO"].str.replace(r'\D+','', regex=True)
        print(f"{scrap_date} will start uploading...")
        df2db(df, "fund_report", engine)
        print(f"{scrap_date} uploaded!")
 
def df2db(df_a, table_name, engine):
    #code snippet from https://stackoverflow.com/questions/65800150/psycopg2-copy-from-for-csv-to-postgress 
    output = io.StringIO()
    df_a.to_csv(output, sep='\t', index = False, header = False, quoting=csv.QUOTE_NONE, escapechar='\\')
    output.getvalue()
    output.seek(0)
    connection = engine.raw_connection() 
    cursor = connection.cursor()
    cursor.copy_from(output,table_name,null='')
    connection.commit()
    cursor.close()        