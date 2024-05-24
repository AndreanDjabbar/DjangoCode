import requests
import json

def get_sources(url):
    headers = {
        "key": "a463ee5474f4cfa48bcfdee39cc09307"
    }
    params = {
        "id":12
    }
    try:
        response = requests.get(
            url,
            headers=headers,
        )
        data = response.json()
        return data
    except:
        return "Error"
    
def get_services(url, origin_id, destination_id, weight, courier):
    payload = {
        "origin": origin_id,
        "destination": destination_id,
        "weight":weight,
        "courier":courier
    }
    headers = {
        "key": "a463ee5474f4cfa48bcfdee39cc09307",
        "content":"application/x-www-form-urlencoded"
    }
    try:
        response = requests.post(
            url,
            headers=headers,
            data=payload
        )
        return response.json()
    except:
        return "Error"