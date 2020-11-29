from fastapi import FastAPI

from api.recommendations.routes import router as recommendation_router


app = FastAPI()

app.include_router(recommendation_router, prefix="/api/recommendation", tags=["Recommendation"])
