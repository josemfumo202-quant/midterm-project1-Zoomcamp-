import requests

url = 'http://localhost:9696/predict'

client = {
    "longitude": -122.23,
    "latitude": 37.88,
    "housing_median_age": 41.0,
    "total_rooms": 880.0,
    "total_bedrooms": 129.0,
    "population": 322.0,
    "households": 126.0,
    "median_income": 8.3252
}

response = requests.post(url, json=client)
print("Status Code:", response.status_code)
print("Response Text:", response.text)