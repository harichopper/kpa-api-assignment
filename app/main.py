from fastapi import FastAPI
from app.routers import kpa
from app.database import Base, engine

app = FastAPI(title="KPA API Assignment")

app.include_router(kpa.router)

@app.on_event("startup")
@app.get("/")
def root():
    return {"message": "KPA API is live!"}

async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
