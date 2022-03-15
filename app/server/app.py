from fastapi import FastAPI,HTTPException
from server.aux_app import get_full_response,check_parameters
from typing import Optional

app = FastAPI(title="REST API Rentability Carteira Global")


@app.get("/")
async def root():
     return {"message": "REST API Rentability Carteira Global 🌎 "}
   
@app.get("/funds/{cnpj}/rentability")
def get_fund_rentability(cnpj:str, init_date:str, end_date:str, invest_value: Optional[float] = None, _return: Optional[str] = None):
     check_parameters(cnpj,init_date,end_date)
     full_res = get_full_response(cnpj,init_date,end_date,invest_value)
     if _return == "full":
          response = full_res
     else:
          response = full_res[-1]
          response.pop("date_report")
          if not invest_value:
               response.pop("equity_value")
     if response:
          return response
     raise HTTPException(404, "Something went wrong" )
