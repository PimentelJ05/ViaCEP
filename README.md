# 📦 Address Lookup by ZIP Code - ViaCEP API
Welcome to the Address Lookup by ZIP Code project! This project uses the ViaCEP API to retrieve address information based on a ZIP code provided by the user. It is designed to be a simple and interactive command-line tool that allows users to input a Brazilian ZIP code (CEP) and get the corresponding address details.

## 📋 Overview
This Python project leverages the requests library to interact with the ViaCEP API, fetching details like street name, neighborhood, city, and state based on a valid ZIP code.

## Key Features:
- API Integration: Retrieves real-time address data from ViaCEP.
  
- User Input: Prompts the user to input a ZIP code.

- Error Handling: Displays a message if the ZIP code is invalid or no address is found.

- Detailed Address Output: Displays the full address in an easy-to-read format.

## 🚧 Under Development:
This project is still under development with the goal of evolving into a responsive front-end web page for address searches. The future version will include an intuitive user interface optimized for both mobile and desktop devices, making it even easier to search for addresses directly from a browser.

## 🚀 How to Run
- Clone the repository:

git clone https://github.com/your-repo/address-lookup-by-cep.git
cd address-lookup-by-cep

- Install Dependencies: Make sure you have the requests library installed. You can install it using pip:

pip install requests

- Run the Application: Simply execute the Python script:

python app.py

- Enter a ZIP Code (CEP): After running the script, you’ll be prompted to input a Brazilian ZIP code (CEP). The script will then display the corresponding address.

## 🛠️ Technologies Used
Python: The core language for this project.
Requests Library: For making HTTP requests to the ViaCEP API.
ViaCEP API: Provides the address details based on the Brazilian postal code (CEP).

  
