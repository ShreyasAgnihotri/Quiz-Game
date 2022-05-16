from urllib import response
import requests


Parameters = {
    "amount" : 10,
    "category": 18,
    "type": "boolean",
}

response=requests.get("https://opentdb.com/api.php",params=Parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
    