from fastapi import FastAPI
from planeta import Planeta
import json
app = FastAPI()


@app.get("/cartola")
async def root():
    endor = Planeta(1, 'Endor', "temperate", "forests, mountains, lakes", 0)
    return endor
