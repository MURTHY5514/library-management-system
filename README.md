
# 📚 Library Management System 📚

Welcome to My Library Management Project! This Library Management System is a web-based application built using Django, designed to streamline the management of a library's resources, including books, 


## Features 🚀

- ### User Authentication 
Secure user authentication system allows librarians and patrons to access the system with their credentials, ensuring privacy and security of data.

- ### Book Management
Perform CRUD (Create, Read, Update, Delete) operations on the library's collection of books, including adding new books, updating book information, and removing outdated or damaged copies.

- ### Patron Management
Keep track of library patrons, including registration, updating patron information, and managing membership status.



## Technologies Used 🛠️
- ### Django
Python-based web framework for rapid development of robust and scalable web applications.

- ### SQLite 
Database management system for storing and retrieving library data efficiently.

- ### HTML/CSS/JavaScript
Frontend technologies for creating a user-friendly and responsive interface.

- ### Bootstrap
Frontend framework for designing consistent and visually appealing web pages.

- ### Git/GitHub
Version control system and collaboration platform for managing project code and facilitating collaboration among team members.
## Installation 📦

To run the Library Management System on your local machine, follow these steps:

### 1. Clone the Repository
```bash
  git clone https://github.com/MURTHY5514/library-management-system.git

```

### 2. Navigate to the Project Directory
```bash
  cd library-management-system
```

### 3. Set Up a Virtual Environment (Optional but Recommended)
```bash
  python -m venv my_venv
```
here  `my_venv` is the name of virtual env give your name

### 4. Activate virtual environment
```bash
  my_venv\Scripts\activate
```
here  `my_venv` is the name of virtual env give your name

### 5. Install Dependencies
```bash
  pip install -r requirements.txt
```


### 6. Apply Database Migrations
```bash
  python manage.py migrate

```
### 7. Create a Superuser (Optional, for admin access)
```bash
  python manage.py createsuperuser

```
### 8. Run the Development Server
```bash
  python manage.py runserver
```
### 9. Access the Application
  Open a web browser and go to http://localhost:8000 to access the Library Management System.




    
## Usage/Examples 💻

After installing the application, you can use the following credentials to log in:

### Admin Dashboard
If you created a superuser during installation, you can access the admin dashboard at http://localhost:8000/admin and log in using the superuser credentials.

### SignUP
To access the sign-up page, navigate to `/`
```url
http://localhost:8000/
```
### Log In
To access the log-in page, navigate to `/login/`
```url
http://localhost:8000/login/
```

### Log Out
To log out, navigate to `/logout/`
```url
http://localhost:8000/logout/
```

### Book List View
To view the list of books, navigate to `/books/`
```url
http://localhost:8000/books/
```

### Update Book
To update a specific book, replace `<id>` with the ID of the book and navigate to `/update/<id>/`
```url
http://localhost:8000/update/1/
```
make sure that given id - `1` is there in book list

### Delete Book
To delete a specific book, replace `<id>` with the ID of the book and navigate to `/delete/<id>/`
```url
http://localhost:8000/delete/1/
```
make sure that given id - `1` is there in book list

### Book Detail View
To view details of a specific book, replace `<pk>` with the primary key of the book and navigate to `/book_detail/<pk>/`
```url
http://localhost:8000/book_detail/1/
```
### Custom 404 Page
For any other unspecified URLs, a `custom 404` page will be displayed. For example
```url
http://localhost:8000/invalid_url/
```
