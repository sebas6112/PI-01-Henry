from fastapi import FastAPI
from routes.query import query

app = FastAPI()

app.include_router(query)
