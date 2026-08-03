from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Customer Support AI Agent"
)


app.include_router(router=router)


@app.get('/')
def home():
    return {
        "message": "Customer Support AI Agent is running"
    }

