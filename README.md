# Number Classification API

A RESTful API that provides mathematical properties and fun facts about numbers.

## Features

- Classifies numbers based on various mathematical properties
- Determines if a number is prime, perfect, or Armstrong
- Calculates digit sum
- Provides fun facts about numbers using the Numbers API
- CORS enabled
- Input validation and error handling

## Technology Stack

- Python 3.8+
- FastAPI
- httpx for async HTTP requests
- uvicorn for ASGI server

## Installation

1. Clone the repository:
```bash
git clone https://github.com/peliah/numbers-classification.git
cd number-classifier-api
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastapi uvicorn httpx
```

## Running the API

1. Start the server:
```bash
uvicorn main:app --reload
```

2. The API will be available at `http://localhost:8000`

## API Documentation

### Endpoint

`GET /api/classify-number?number={number}`

### Parameters

- `number` (required): An integer to classify

### Response Format

Success (200 OK):
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

Error (400 Bad Request):
```json
{
    "number": "alphabet",
    "error": true
}
```

### Properties Combinations

The `properties` field can contain the following combinations:
1. `["armstrong", "odd"]` - number is both Armstrong and odd
2. `["armstrong", "even"]` - number is Armstrong and even
3. `["odd"]` - number is only odd
4. `["even"]` - number is only even

## Deployment

The API can be deployed to any cloud platform that supports Python applications. Make sure to:

1. Set appropriate CORS origins in production
2. Configure environment variables if needed
3. Use a production-grade ASGI server
4. Set up monitoring and logging

## Performance

The API is designed to respond within 500ms for most requests. Response time may vary based on:
- Numbers API response time
- Server load
- Network conditions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.