
# Flask MongoDB Demo Application

This is a simple Flask web application that demonstrates how to collect form data and store it in a MongoDB database. It includes a basic homepage, a form submission endpoint, and a view to display submitted data.

---

## Features

- Connects to MongoDB using **pymongo**
- Uses environment variables for sensitive information
- Basic form submission and data storage
- View all submitted data
- Displays current day and time on the homepage

---

## Project Structure

```
├── app3.py             # Main Flask app
├── .env                # Environment variables (MongoDB URI)
├── requirement.txt     # Python dependencies
└── templates/
    └── index.html      # Homepage template (you need to provide)
```

---

## Prerequisites

- Python 3.x installed on your system
- A MongoDB Atlas cluster or local MongoDB instance
- `pip` for managing Python packages

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Create a Virtual Environment (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirement.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add your MongoDB URI. Example:

```
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority
```

*Note: You already have an example `.env` file included.*

### 5. Add HTML Template

Create a `templates` folder and add an `index.html` file. Example basic content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask MongoDB Demo</title>
</head>
<body>
    <h1>Welcome!</h1>
    <p>Today is: {{ day }}</p>
    <p>Current time: {{ time }}</p>

    <form action="/submit" method="post">
        <input type="text" name="name" placeholder="Enter your name" required />
        <input type="email" name="email" placeholder="Enter your email" required />
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

---

## Running the Application

```bash
python app3.py
```

By default, the app runs in debug mode at `http://127.0.0.1:5000/`.

---

## API Endpoints

| Route      | Method | Description                        |
|------------|--------|------------------------------------|
| `/`        | GET    | Homepage showing day & time        |
| `/submit`  | POST   | Submits form data to MongoDB       |
| `/view`    | GET    | Displays all submitted data (JSON) |

---

## Example MongoDB Document

```json
{
    "name": "John Doe",
    "email": "john@example.com"
}
```

---

## Dependencies

Listed in `requirement.txt`:

- flask
- pymongo
- dnspython
- python-dotenv

Install with:

```bash
pip install -r requirement.txt
```

---

## Notes

- Make sure your MongoDB URI allows connections from your IP address.
- The application currently runs with debug enabled. Disable it in production.
- You can customize `index.html` to collect more data from users.

---

## License

This project is for educational/demo purposes.
