import requests
from PIL import Image
from io import BytesIO

# URL του Dog CEO API
url = 'https://dog.ceo/api/breeds/image/random'
# Κάνουμε αίτηση για τα δεδομένα
response = requests.get(url)

# Ελέγχουμε αν η αίτηση ήταν επιτυχής
if response.status_code == 200:
    # Φορτώνουμε τα δεδομένα JSON σε λεξικό
    dog_data = response.json()
    
    # Παίρνουμε τη διεύθυνση της εικόνας
    image_url = dog_data['message']
    
    # Κάνουμε αίτηση για την εικόνα
    image_response = requests.get(image_url)
    
    # Ελέγχουμε αν η αίτηση για την εικόνα ήταν επιτυχής
    if image_response.status_code == 200:
        # Ανοίγουμε την εικόνα
        img = Image.open(BytesIO(image_response.content))
        
        # Εμφανίζουμε την εικόνα
        img.show()
    else:
        print(f"Σφάλμα κατά την λήψη της εικόνας: {image_response.status_code}")
else:
    print(f"Σφάλμα κατά την λήψη των δεδομένων: {response.status_code}")
