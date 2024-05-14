from datetime import datetime, timedelta
import random

from rating_service import rating_service, Rating

NB_REVIEWS = 10

comments = [
    "This is a comment",
    "This is another comment",
    "This is a third comment",
    "This is a fourth comment",
    "This is nice",
    "This is not nice",
    "This is a comment",
    "I like this",
    "I don't like this",
]

for _ in range(NB_REVIEWS):
    starRating = random.randint(0, 10) * 0.5
    date = (datetime.now() - timedelta(days=random.randint(0, 365))).isoformat()
    comment = random.choice(comments)
    rating_service.save(Rating(fiveStarRating=starRating, comment=comment, dateTime=date))

print("Random ratings generated successfully")