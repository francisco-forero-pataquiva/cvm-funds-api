from dateutil.relativedelta import relativedelta
from server.db import fetch_quote_values
from fastapi import HTTPException
from dateutil.parser import parse
from datetime import datetime


def get_rentability(prices):
    if len(prices) < 2:  
        prices[0], prices[1] = 1,1
    initial_quote = prices[0]
    final_quote = prices[1]   
    f = (final_quote / initial_quote)
    r = (f - 1) * 100
    return r

def get_invest_value(invest_value,r):    
    if invest_value is None:
        return 0
    rentability_value = (invest_value * r)/100
    invest_value += rentability_value
    return invest_value

def get_time_diff(init_date,end_date):
    date1 = parse(init_date)
    date2 = parse(end_date)
    diff = int((date2 - date1).days)
    return diff

def proper_dates(init_date,end_date):
    try:
        datetime.strptime(init_date, '%Y-%m-%d')
        datetime.strptime(end_date, '%Y-%m-%d')
        return True
    except:
        return False

def get_full_response(cnpj,init_date,end_date,invest_value):
    full_response =[]
    index = 0
    iv_dict ={}
    diff = get_time_diff(init_date,end_date)
    for n in range(diff+1):
        d = str((parse(init_date) + relativedelta(days=+n)).date())
        r = get_rentability(fetch_quote_values(cnpj,init_date,d))
        if r == 0 and index !=0: #uses friday value for the weekend
            iv = iv_dict[index-1]  
        else:
            iv = get_invest_value(invest_value,r)
        iv_dict.update({index: iv}) 
        daily_r= {
            "date_report": d,
            "rentability": r,
            "equity_value": iv 
            }
        full_response.append(daily_r)
        index += 1
    return full_response

def check_parameters(cnpj,init_date,end_date):
    if len(cnpj) != 14:
        raise HTTPException(500, detail="CNPJ must be 14 characters long")
    if not proper_dates(init_date,end_date):
        raise HTTPException(500, detail="Dates must be formatted as YYYY-MM-DD")
    if "2021" not in init_date or "2021" not in end_date:
        raise HTTPException(500, detail="Only dates from 2021 are available")

