import json
import data_fetcher


def get_animal_from_user():
    """
    Prompt the user to input an animal name and return it.
    """
    while True:
        animal_name = input("Enter a name of an animal: ")
        if animal_name:
            return animal_name
        print("Animal name cannot be empty. Please enter a valid name.")




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


def generate_info_string(animals_data, animal_name):
    """
    Generate an HTML string for a list of animals by serializing each one.
    """
    if not animals_data:  # If no data is returned from the API
        return f"<h2>The animal '{animal_name}' doesn't exist.</h2>"

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
    """
    Orchestrates the process of fetching animal data,
    generating HTML content, and saving it to a file.
    """
    # Fetch API key and setup API request
    api_key = "sGX5MTpcQPbtL6DknWFjPg==L22HMyYSGBkwcO4n"  # Hardcoded for this exercise
    api_url = "https://api.api-ninjas.com/v1/animals?name={}"
    headers = {"X-Api-Key": api_key}

    while True:  # Loop until valid data is received
        animal_name = get_animal_from_user() # Prompts and gets animal name from user

        # Fetch animal data from the API
        animals_data = (data_fetcher.fetch_animal_data(animal_name))[:10]

        # Ensure data is fetched successfully
        if animals_data is None:
            print(f"Error: Failed to fetch data for '{animal_name}'. Status code: {response.status_code}")
            continue

        if not animals_data:
            print(f"No data found for '{animal_name}'. Please try again.")
            continue

        break # Data found, exits loop

    # Generate the string for animals info
    animals_string = generate_info_string(animals_data, animal_name)

    # Read the HTML template
    template = read_animals_template("animals_template.html")

    # Replace the placeholder in the template with the animals string
    new_html = replace_placeholder(template, animals_string)

    # Write the new HTML to a file
    write_html_to_new_file("animals.html", new_html)

    print("HTML file generated successfully as 'animals.html'.")


if __name__ == "__main__":
    main()
