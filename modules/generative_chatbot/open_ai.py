import openai

# Documentation about the Tokopedih E-commerce Platform
project_doc = """
Documentation
Project Name: Tokopedih E-commerce Platform

Overview:
Tokopedih E-commerce Platform is an online marketplace that connects vendors with customers, providing a seamless shopping experience. This documentation provides an overview of the codebase structure and key functionalities.

Directory Structure:

css
Copy code
tokopedih-ecommerce/
│
├── frontend/
│   ├── index.html
│   ├── styles/
│   │   ├── main.css
│   ├── scripts/
│   │   ├── main.js
│
├── backend/
│   ├── server.py
│   ├── database/
│   │   ├── users.db
│   │   ├── products.db
│   ├── utils/
│   │   ├── authentication.py
│   │   ├── validation.py



Frontend:
index.html: Main HTML file for the web application.
styles/: Directory containing CSS stylesheets.
main.css: Main stylesheet for the application.
scripts/: Directory containing JavaScript files.
main.js: Main JavaScript file for client-side logic.

Backend:
server.py: Python script implementing the backend server logic.
database/: Directory containing SQLite databases.
users.db: Database storing user information.
products.db: Database storing product information.
utils/: Directory containing utility modules.
authentication.py: Module for user authentication logic.
validation.py: Module for input validation.

Key Functionality:

User Authentication:
Users can register, login, and logout securely.
Passwords are hashed for security using bcrypt.
Product Management:
Vendors can add, edit, and delete products.
Products are stored in the database with attributes such as name, description, price, and stock.

Shopping Cart:
Users can add products to their shopping cart.
Cart contents are stored in the session.

Checkout:
Users can proceed to checkout and place orders.
Orders are stored in the database with details such as products, quantities, and total price.


API Endpoints:
/register: Register a new user.
/login: Log in an existing user.
/logout: Log out the current user.
/products: Retrieve all products or add a new product.
/cart: Add, remove, or view items in the shopping cart.
/checkout: Process orders and create new orders in the database.

Dependencies:
Flask: Web framework for backend development.
SQLite3: Database management system.
bcrypt: Password hashing library for security.
JavaScript Fetch API: For making asynchronous requests from the frontend.

Note: This documentation provides a basic overview of the Tokopedih E-commerce Platform codebase. For detailed implementation and usage instructions, refer to the source code and relevant comments within the files.
"""

def chat_with_gpt(prompt, model="gpt-4-turbo"):
    # Combine user prompt with project documentation
    full_prompt = f"{project_doc}\n\nQuestion: {prompt}"
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "system", "content": "You are a helpful assistant familiar with the Tokopedih E-commerce Platform."}, {"role": "user", "content": full_prompt}],
    )
    return response['choices'][0]['message']['content'].strip()