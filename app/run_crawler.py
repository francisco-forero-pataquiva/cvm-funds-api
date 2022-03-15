from server.aux_crawler import populate_db
from server.db import create_db


def run_crawler():
    create_db()
    populate_db(2021)
  
run_crawler()