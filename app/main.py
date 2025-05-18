from fastapi import FastAPI
from app.routers import reports

app = FastAPI()

app.include_router(reports.router, prefix="/reports")
