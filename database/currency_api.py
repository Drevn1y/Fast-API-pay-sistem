from fastapi import APIRouter
import requests

currency_router = APIRouter(prefix='/currency', tags=['Курсы валют'])


# Запрос на получении нужных курсов валют
@currency_router.post('/get-rates')
async def get_currency_rates():
    nbu_url = 'https://nbu.uz/uz/exchange-rates/json/'
    usd = requests.get(nbu_url).json()[-1]
    rub = requests.get(nbu_url).json()[-6]
    eur = requests.get(nbu_url).json()[7]
    return {'USD': usd, 'RUB': rub, 'EUR': eur}
