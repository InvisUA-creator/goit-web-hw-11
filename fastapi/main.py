from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from src.dbase.dbase import get_db
from src.routes import contacts


app = FastAPI()

app.include_router(contacts.router, prefix="/api")


@app.get("/")
def index():
    return {"message": "Address Book App"}


@app.get("/api/healthchecker")
async def healthchecker(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT 1"))
        result = result.fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail=str(e))
        return {"status": "OK"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
