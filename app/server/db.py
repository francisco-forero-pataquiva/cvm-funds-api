from server.credential_configs import access_configuration
from sqlalchemy import create_engine, text
import os


access_configuration()
DATABASE_URL = 'postgresql://{}:{}@database-1.c9uvt61lcxqq.us-east-1.rds.amazonaws.com:5432/postgres'.format(
            os.environ.get("DB_USER"), os.environ.get("DB_PASSWORD"))
engine = create_engine(DATABASE_URL, echo=True )
connection = engine.connect()

def create_db():
    query = "DROP TABLE IF EXISTS public.fund_report; CREATE TABLE IF NOT EXISTS public.fund_report(cnpj varchar(14), quote_value float(8) NULL, date_report date NOT NULL)"
    results = (connection.execute(query))


def fetch_quote_values(cnpj:str, init_date:str, end_date:str):
    query =  text(f"SELECT quote_value FROM public.fund_report WHERE cnpj = '{cnpj}' AND date_report = '{init_date}' OR date_report = '{end_date}' AND cnpj = '{cnpj}'")
    results = (connection.execute(query).fetchall())
    response = {}
    for count,n  in enumerate(results):
        response.update({count: n[0]})
    return (response)
