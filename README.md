# Administrative Management System for Libraries 🏫📚

This project focuses on developing a comprehensive administrative management system for libraries. It enables efficient handling of books, users, and loans, with the aim of optimizing processes and enhancing the user experience. ✨

## Key Features 🔑

- **Book Management**: Storage and administration of book information, including title, author, publisher, publication year, category, and availability. 📚
- **User Management**: Registration and control of user information, such as name and identification, as well as tracking of borrowed books. 👥
- **Loan Management**: Queue system to handle loan requests and returns in an orderly and efficient manner. 📝
- **Intuitive User Interface**: Main menu with access to the different system functionalities. 🖥️

## Technologies Used 🛠️

- Frontend: React.js
- Backend: Django
- Data Structures:
  - Doubly Linked List for Books
  - Dynamic Array for Users
  - Queue for Loan Management

## Usage Instructions 📚

### Backend (Django) 🐍

1. Clone the repository:
```
git clone [https://github.com/user/library-admin.git](https://github.com/AndresMarulanda10/Library_Management_System)
```

2. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate
```

3. Install the dependencies:
```
pip install -r requirements.txt
```

4. Apply the migrations:
```
python manage.py migrate
```

5. Start the server:
```
python manage.py runserver 0.0.0.0:8000
```

6. Access the backend at `http://localhost:8000/api/` 🌐

The backend is configured to run on the `0.0.0.0` host and `8000` port. You can access the system APIs through the URL `http://localhost:8000/api/`.

7. Create a superuser to access the Django admin panel:
```
python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password for the superuser.

### Frontend (React.js) 🌐

1. Navigate to the frontend directory:
```
cd library-admin/frontend
```

2. Install the dependencies:
```
npm install
```

3. Start the development server:
```
npm start
```

4. Open your browser and access `http://localhost:3000` 🖥️

The frontend will run on `http://localhost:3000`, where you can interact with the library administrative management system.

Make sure to have both the backend and the frontend running simultaneously to use all the system's functionalities.

## Contribution 💻

Want to be a part of this project? Great! Follow these steps:

1. Fork the repository. 🍴
2. Create a new branch for your feature or fix. 🖋️
3. Make your changes and ensure everything works correctly. ✅
4. Submit a pull request with a detailed description of your changes. 📥

## License 🪪

This project is licensed under the [RPL License](LICENSE).
