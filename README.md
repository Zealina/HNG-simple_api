# Public API - Basic Credentials

## Task Description
This project is a simple public API that returns basic credentials in JSON format. The API provides:

1. **Your registered email address** (used to register on the HNG12 Slack workspace).
2. The **current datetime** as an ISO 8601 formatted timestamp.
3. The **GitHub URL** of the project's codebase.

## Technologies Used
- **Flask** - A lightweight WSGI web application framework for Python.
- **Flask-CORS** - A Flask extension for handling Cross-Origin Resource Sharing (CORS).
- **Datetime** - A built-in Python module for working with dates and times.

## Setup Instructions
To run this API locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/Zealina/HNG-simple_api
   cd HNG-simple_api
   ```

2. Install dependencies:
   ```sh
   pip install flask flask-cors
   ```

3. Run the API:
   ```sh
   python app.py
   ```

4. The API will be available at:
   ```
   http://127.0.0.1:5000/
   ```

## API Documentation

### Base URL
```sh
http://127.0.0.1:5000/
```

### Endpoint: `GET /`
Returns basic credentials in JSON format.

#### **Request Format**
- Method: `GET`
- Headers: None
- Parameters: None

#### **Response Format**
```json
{
  "email": "hamilsebastine@gmail.com",
  "current_datetime": "2025-01-31T12:34:56.789Z",
  "github_url": "https://github.com/Zealina/HNG-simple_api"
}
```

#### **Example Usage**
Using `curl`:
```sh
curl -X GET http://127.0.0.1:5000/
```

Using Python:
```python
import requests

response = requests.get("http://127.0.0.1:5000/")
print(response.json())
```

## Related Resources
For more information about backend development with Flask, check out:
- [https://hng.tech/hire/python-developers]
