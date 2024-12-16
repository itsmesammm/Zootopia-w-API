import json


def load_data(file_path):
    try:
        with open(file_path, 'r') as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file '{file_path}'.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
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
    # Load animal data
    animals_data = load_data("animals_data.json")

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
