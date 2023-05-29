# Project Name

Client app

## Description

The Client app is a web application built using Django framework. It provides functionality to manage client information, including their personal details, education background, and preferred mode of contact. The system allows users to create new clients, view a list of all clients, and search for specific clients.

## Installation

To run the Client app locally, follow these steps:

1. Clone the repository:

   ```
   git clone <[repository_url>](https://github.com/phoenixsubash/client_app.git)
   ```

2. Navigate to the project directory:

   ```
   cd client-management-system
   ```

3. Create a virtual environment:

   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - For Windows:

     ```
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```
     source venv/bin/activate
     ```

5. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

   The following packages will be installed:

   - asgiref==3.7.2
   - beautifulsoup4==4.12.2
   - certifi==2023.5.7
   - cloudinary==1.33.0
   - Django==4.2.1
   - django-bootstrap-v5==1.0.11
   - six==1.16.0
   - soupsieve==2.4.1
   - sqlparse==0.4.4
   - urllib3==1.26.16

6. Apply database migrations:

   ```
   python manage.py migrate
   ```

7. Create a superuser (admin) account:

   ```
   python manage.py createsuperuser
   ```

   Follow the prompts to enter your desired username and password.

8. Start the development server:

   ```
   python manage.py runserver
   ```

   The Client Management System will be accessible at http://localhost:8000.

## Usage

1. Open a web browser and go to http://localhost:8000.

2. Login using the superuser account created in the installation step.

3. After logging in, you will be redirected to the client list page. Here, you can view all the clients in the system.

4. To add a new client, click on the "Create Client" button and fill in the required information in the provided form fields, including name, profile image, gender, phone, email, nationality, date of birth, education background, and preferred mode of contact.

5. Click on the "Submit" button to save the client details.

6. To search for a specific client, enter the search query in the search box on the client list page. The system will display the matching results based on the client's name, email, or phone number.

7. You can view the detailed information of a client by clicking on their name in the client list. It will redirect you to the client detail page.

## Additional Features

The Client Management System includes the following additional features:

- Django-Bootstrap5 Integration: The system utilizes the Django-Bootstrap5 package to style the forms and provide a consistent look and feel.
- Custom Error Messages: If there are any form validation errors during client creation or login, relevant error messages will be displayed to guide the user.
- Custom 404 Page: If a user tries to access a non-existing page, they will be shown a custom 404 error page.

## Conclusion

The Client app  provides a user-friendly interface to manage client information effectively.