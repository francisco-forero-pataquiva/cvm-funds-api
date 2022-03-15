# REST API Rentability Carteira Global 🌎

## About 

This REST API+Crawler project was made as a back-end challenge for <a href = "https://www.carteiraglobal.com/">Carteira Global</a>. The API was centered around getting a response with several parameterers containg the rentability of a funds using data from  <a href = "http://dados.cvm.gov.br/">Portal Dados Abertos CVM</a>, latter stored in a AWS Postresql database. The database was populated using a crawler that scrapped the data, processed it and later load it to the and aws database.

### Stack 

The API was written using Python 3.9 with FastApi as the framework and a AWS Postgresql database. 
To perform the database operations, the sqlalchemy library was chosen. 
For the crawler and scrapper, the pandas library was for the processing of the data and io was used to load the data in bulk in a buffered fashion.

### Installing

Use the following commands to create a virtual environment on your Linux/Mac:

```
python3 -m venv venv
source venv/bin/activate
```

To install the dependencies of the project, use this command:

```
python3 -m pip install -r requirements.txt
```

To start the API, just run the main.py file, and to run the populator, run_crawler.py.

**The credentials required to access the database will be sent by email.**



