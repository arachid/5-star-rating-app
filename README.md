# 5 Star Rating App

This is a small app that exposes a 5 star rating App. It's built using **Python** for the API and **React** for the frontend.

1. The 5 star rating app:

2. The list of all reviews submitted.

## Backend 
  
The backend is written with Python Framework FastAPI. For simplicity, the backend is persisting the the reviews in a CSV file.

1. Install FastAPI framework using pip

    `pip install fastapi`

2. Install uvicorn server using pip

    `pip install uvicorn`

3. Navigate tot the backend folder and run the app.
	```
	cd backend
	uvicorn main:app --reload
	```


## Frontend

The frontend is written with React.

To runt it:

    cd frontend
    npm start
