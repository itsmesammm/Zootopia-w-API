# 🦊 Zootopia Animal Info Generator

Zootopia Animal Info Generator is a Python program that fetches animal data from the API Ninjas Animals API and generates a dynamic HTML website displaying animal details based on user input. The project adheres to a clean architecture by separating concerns into different modules for fetching data and generating the website.

### 🚀 Features

Fetch detailed animal information by name via the API.
Generate an HTML webpage with dynamic content, including:
* Animal name
* Diet
* Location(s)
* Type
* Skin type

Handle invalid animal names with a friendly error message.
Structured into multiple files for improved maintainability.
Uses .env to securely manage API keys.

### Project Structure
#### Zootopia-w-API/
```
.env                      # Environment variables file (contains API key)
.gitignore                # Git ignore file (ignores .env, __pycache__, etc.)

animals_web_generator.py  # Main program: orchestrates user input and HTML generation
data_fetcher.py           # Module for fetching data from the API

animals_template.html     # HTML template file (used to generate the website)
animals.html              # Output file: Generated animal details webpage

animals_data.json         # Optional static JSON file (can serve as fallback data)
```

### 🛠️ Setup Instructions

Prerequisites
Ensure you have Python 3.8+ installed. You also need to install required dependencies.


## Installation Steps

**1. Clone the repository:**

`
git clone https://github.com/<your-username>/Zootopia-w-API.git
cd Zootopia-w-API`


**2. Set up a virtual environment (optional but recommended):**

`python3 -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
Install dependencies:`

**3. Install dependencies:**

`pip install python-dotenv requests`

**4. Set up your API key:**
* Create a .env file in the project root.
* Add your API key like this:
`API_KEY=your_api_key_here`
###### You can get a free API key from API Ninjas.

**5. Run the program:**
`python animals_web_generator.py`


### 📋 How It Works
The program prompts the user to enter an animal name.
It fetches data from the API Ninjas Animals API using the data_fetcher module.
If valid data is returned, the program generates an HTML file (animals.html) with the details.
If no data is found, an error message is displayed both in the terminal and on the webpage.

### 🤝 Contributing
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.


### 🔒 License
This project is open-source and available under the MIT License.

