from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from router.rout_serveys import survey_router
from router.routes_users import router as user_router
import Database.database_utils as database

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(database.db_router)
#app.include_router(survey_router)
app.include_router(user_router, prefix="/users", tags=["users"])

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/test_db")
async def test_db():
    count = await database.db.users.count_documents({})
    return {"user_count": count}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=4000)