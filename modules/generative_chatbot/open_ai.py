import os
import openai
from openai import OpenAI

# Documentation about the Tokopedih E-commerce Platform
project_doc = """
Chatbot ini diperuntukan hanya untuk menjawab pertanyaan-pertanyaan yang berkaitan dengan project dibawah ini, kamu bisa menjawab sapaan atau menanyakan cuaca, 
juga bisa menjawab dengan jawaban fiktif apabila relevan tetapi informasinya tidak tercantum seperti struktur tim, struktur organisasi, kegunaan dari aplikasi, dan cakupan dari project. jika tidak relevan jawab dengan 
'Maaf chatbot ini diperuntukan untuk menjawab hal yang berkaitan dengan onboarding' jika pada setiap dokumentasi belum ditambahkan tab atau new line, kamu bisa tambahkan hal tersebut

Documentation 1 Sosofwerhausan Project :
Project Name: Tokopedih E-commerce Platform

Overview:
Tokopedih E-commerce Platform is an online marketplace that connects vendors with customers, providing a seamless shopping experience. This documentation provides an overview of the codebase structure and key functionalities.

Directory Structure:
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
- **index.html:** Main HTML file for the web application.
- **styles/:** Directory containing CSS stylesheets.
  - **main.css:** Main stylesheet for the application.
- **scripts/:** Directory containing JavaScript files.
  - **main.js:** Main JavaScript file for client-side logic.

Backend:
- **server.py:** Python script implementing the backend server logic.
- **database/:** Directory containing SQLite databases.
  - **users.db:** Database storing user information.
  - **products.db:** Database storing product information.
- **utils/:** Directory containing utility modules.
  - **authentication.py:** Module for user authentication logic.
  - **validation.py:** Module for input validation.

Key Functionality:

**User Authentication:**
- Users can register, login, and logout securely.
- Passwords are hashed for security using bcrypt.

**Product Management:**
- Vendors can add, edit, and delete products.
- Products are stored in the database with attributes such as name, description, price, and stock.

**Shopping Cart:**
- Users can add products to their shopping cart.
- Cart contents are stored in the session.

**Checkout:**
- Users can proceed to checkout and place orders.
- Orders are stored in the database with details such as products, quantities, and total price.

API Endpoints:
- **/register:** Register a new user.
- **/login:** Log in an existing user.
- **/logout:** Log out the current user.
- **/products:** Retrieve all products or add a new product.
- **/cart:** Add, remove, or view items in the shopping cart.
- **/checkout:** Process orders and create new orders in the database.

Dependencies:
- **Flask:** Web framework for backend development.
- **SQLite3:** Database management system.
- **bcrypt:** Password hashing library for security.
- **JavaScript Fetch API:** For making asynchronous requests from the frontend.

Note: This documentation provides a basic overview of the Tokopedih E-commerce Platform codebase. For detailed implementation and usage instructions, refer to the source code and relevant comments within the files.

Documentation 2 Sosofwerhausan Project :

Project Name: Acme Accounting Suite

Overview

Acme Accounting Suite is a comprehensive software solution designed to simplify financial management for small to medium-sized businesses. This documentation provides an overview of the codebase structure and key functionalities.

Directory Structure

acme-accounting-suite/
│
├── frontend/
│   ├── index.html
│   ├── styles/
│   │   ├── main.css
│   ├── scripts/
│   │   ├── main.js
│
├── backend/
│   ├── app.py
│   ├── database/
│   │   ├── users.db
│   │   ├── transactions.db
│   ├── utils/
│   │   ├── authentication.py
│   │   ├── validation.py
│   │   ├── reporting.py

Frontend

index.html: Main HTML file for the web application.
styles/: Directory containing CSS stylesheets.
main.css: Main stylesheet for the application.
scripts/: Directory containing JavaScript files.
main.js: Main JavaScript file for client-side logic.

Backend

app.py: Python script implementing the backend server logic.
database/: Directory containing SQLite databases.
users.db: Database storing user information.
transactions.db: Database storing transaction records.
utils/: Directory containing utility modules.
authentication.py: Module for user authentication logic.
validation.py: Module for input validation.
reporting.py: Module for generating financial reports.

Key Functionality

User Authentication :
Users can register, login, and logout securely.
Passwords are hashed for security using bcrypt.

Transaction Management :
Users can record income and expenses.
Transactions are stored in the database with attributes such as amount, date, category, and description.

Reporting :
Users can generate financial reports such as profit and loss statements and balance sheets.
Reports can be exported in PDF format.

API Endpoints :
/register: Register a new user.
/login: Log in an existing user.
/logout: Log out the current user.
/transactions: Retrieve all transactions or add a new transaction.
/reports: Generate and retrieve financial reports.

Dependencies :
Flask: Web framework for backend development.
SQLite3: Database management system.
bcrypt: Password hashing library for security.
JavaScript Fetch API: For making asynchronous requests from the frontend.
PDFKit: For generating PDF reports from HTML.

Documentation 3 Sosofwerhausan Project :

Project Name: SafeBank Suite
Overview
SafeBank Suite is a robust banking software designed to manage customer accounts, transactions, and financial operations efficiently. This documentation provides an overview of the codebase structure and key functionalities.

Directory Structure
safebank-suite/
│
├── frontend/
│   ├── index.html
│   ├── styles/
│   │   ├── main.css
│   ├── scripts/
│   │   ├── main.js
│
├── backend/
│   ├── app.py
│   ├── database/
│   │   ├── customers.db
│   │   ├── transactions.db
│   ├── utils/
│   │   ├── authentication.py
│   │   ├── validation.py
│   │   ├── reporting.py
│   │   ├── transaction_processor.py

Frontend

index.html: Main HTML file for the web application.
styles/: Directory containing CSS stylesheets.
main.css: Main stylesheet for the application.
scripts/: Directory containing JavaScript files.
main.js: Main JavaScript file for client-side logic.

Backend

app.py: Python script implementing the backend server logic.
database/: Directory containing SQLite databases.
customers.db: Database storing customer information.
transactions.db: Database storing transaction records.
utils/: Directory containing utility modules.
authentication.py: Module for user authentication logic.
validation.py: Module for input validation.
reporting.py: Module for generating financial reports.
transaction_processor.py: Module for processing financial transactions.

Key Functionality

User Authentication
Customers can register, login, and logout securely.
Passwords are hashed for security using bcrypt.

Account Management
Customers can view their account balance, transaction history, and personal details.
Admins can manage customer accounts, including creating and deactivating accounts.

Transaction Management
Customers can perform transactions such as deposits, withdrawals, and transfers.
Transactions are processed in real-time and stored in the database with attributes such as amount, date, type, and description.

Reporting
Admins can generate financial reports such as account summaries and transaction histories.
Reports can be exported in PDF format for record-keeping and analysis.

API Endpoints
/register: Register a new customer.
/login: Log in an existing customer.
/logout: Log out the current customer.
/accounts: Retrieve account details or manage customer accounts.
/transactions: Perform and view transactions.
/reports: Generate and retrieve financial reports.

Dependencies
Flask: Web framework for backend development.
SQLite3: Database management system.
bcrypt: Password hashing library for security.
JavaScript Fetch API: For making asynchronous requests from the frontend.
PDFKit: For generating PDF reports from HTML.
"""

def chat_with_gpt(prompt, model="gpt-4-turbo"):
    full_prompt = f"{project_doc}\n\nQuestion: {prompt}"
    client = OpenAI(
        api_key="sk-proj-WlWxxOwxqT9URBV7XqgCT3BlbkFJ6qm9vDs5stEDDUTQ36OA",
    )
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant familiar with the Sosofwerhausan Bot."},
                {"role": "user", "content": full_prompt}
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"