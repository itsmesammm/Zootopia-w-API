import requests
import json


def fetch_animal_data(api_url, headers, animal_name):
    """
        Fetch animal data from the API.
        """
    try:
        response = requests.get(api_url.format(animal_name), headers=headers)
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            print(f"Error: Failed to fetch data. Status code: {response.status_code}")
            print(f"Details: {response.text}")
            return None
    except requests.RequestException as e:
        print(f"An error occurred {e}")
        return None


def serialize_animal(animal):
    """
    Serialize a single animal object from json into an HTML string on a list.
    """
    output = ""
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    output += '    <ul class="details-list">\n'
    output += f'      <li class="details-item"><strong>Diet:</strong> {animal["characteristics"].get("diet", "N/A")}</li>\n'
    output += f'      <li class="details-item"><strong>Location:</strong> {", ".join(animal["locations"])}</li>\n'
    output += f'      <li class="details-item"><strong>Type:</strong> {animal["characteristics"].get("type", "N/A")}</li>\n'
    output += f'      <li class="details-item"><strong>Skin Type:</strong> {animal["characteristics"].get("skin_type", "Unknown")}</li>\n'
    output += '    </ul>\n'
    output += '  </p>\n'
    output += '</li>\n'
    return output


def generate_info_string(animals_data):
    """
    Generate an HTML string for a list of animals by serializing each one.
    """
    output = ""
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    return output


def read_animals_template(file_path):
    with open(file_path, 'r') as template_file:
        return template_file.read()


def replace_placeholder(template, animals_string):
    """
    Replace the placeholder in the template with the generated animals string.
    """
    return template.replace("__REPLACE_ANIMALS_INFO__", animals_string)


def write_html_to_new_file(file_path, content):
    with open(file_path, 'w') as new_file:
        new_file.write(content)


def main():
    #API config
    api_url = "https://api.api-ninjas.com/v1/animals?name={}"
    headers = {"X-Api-Key": "sGX5MTpcQPbtL6DknWFjPg==L22HMyYSGBkwcO4n"}

    # Fetch animal data from the API
    animals_data = fetch_animal_data(api_url, headers, "Fox")

    # Ensure data is fetched successfully
    if animals_data is None:
        print("Failed to fetch animal data. Exiting.")
        return

    # Generate the string for animals info
    animals_string = generate_info_string(animals_data)

    # Read the HTML template
    template = read_animals_template("animals_template.html")

    # Replace the placeholder in the template with the animals string
    new_html = replace_placeholder(template, animals_string)

    # Write the new HTML to a file
    write_html_to_new_file("animals.html", new_html)

    print("HTML file generated successfully as 'animals.html'.")


if __name__ == "__main__":
    main()
