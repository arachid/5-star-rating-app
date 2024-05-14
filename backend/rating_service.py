import csv
from datetime import datetime

from fastapi import HTTPException
from pydantic import BaseModel

class Rating(BaseModel):
    fiveStarRating: float
    comment: str
    dateTime: str

class RatingService:
    def __init__(self):
        self.file = open('file.csv', 'a', newline='')
        self.writer = csv.writer(self.file)
        self.reader = csv.reader(self.file)

    def save(self, review: Rating):
        if review.fiveStarRating < 0 or review.fiveStarRating > 5:
            raise HTTPException(status_code=400, detail="fiveStarRating must be between 0 and 5")
        review.dateTime = datetime.now().isoformat()
        print("Saving review:", review)
        self.writer.writerow([review.fiveStarRating, review.comment, review.dateTime])
        return review

    def get_all(self):
        reviews = []
        for row in self.reader:
            reviews.append(Rating(fiveStarRating = row[0], comment = row[1], dateTime = row[2]))
        return reviews

    def get_stats(self):
        reviews = self.get_all()
        total = 0
        count = 0
        for review in reviews:
            total += review.fiveStarRating
            count += 1
        return {"average": total / count, "count": count}

rating_service = RatingService()