import requests

# API constants
API_KEY = "sGX5MTpcQPbtL6DknWFjPg==L22HMyYSGBkwcO4n"
API_URL = "https://api.api-ninjas.com/v1/animals?name={}"


def fetch_animal_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, where each animal is a dictionary:
  {
      'name': ...,
      'taxonomy': { ... },
      'locations': [ ... ],
      'characteristics': { ... }
  },
  or None if an error occurs.
  """
  headers = {"X-Api-Key": API_KEY}


  try:
    response = requests.get(API_URL.format(animal_name), headers = headers)
    if response.status_code == requests.codes.ok:
      return response.json()
    else:
      print(f"Error: Failed to fetch data. Status code: {response.status_code}")
      print(f"Details: {response.text}")
      return None
  except requests.RequestException as e:
    print(f"An error occurred {e}")
    return None
