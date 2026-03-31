import requests
import random

BASE_URL = "https://petstore.swagger.io/v2"

def create_pet():
    pet_id = random.randint(1000, 9999)
    pet_data = {
        "id": pet_id,
        "name": f"TestPet{pet_id}",
        "photoUrls": ["http://example.com/photo1.jpg"],
        "tags": [{"id": 1, "name": "test"}],
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/pet", json=pet_data)
    response.raise_for_status()

    return response.json()