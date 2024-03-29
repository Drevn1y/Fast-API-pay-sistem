from fastapi import FastAPI
from database.currency_api import currency_router

app = FastAPI(docs_url='/')

app.include_router(currency_router)