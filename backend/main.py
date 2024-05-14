from fastapi import FastAPI
from rating_service import rating_service, Rating

app = FastAPI()

@app.get("/ratings")
def get_ratings() -> list[Rating]:
    return rating_service.get_all()

@app.get("/ratings/stats")
def get_stats():
    return rating_service.get_stats()

@app.post('/ratings')
def review(review: Rating):
    return rating_service.save(review)
