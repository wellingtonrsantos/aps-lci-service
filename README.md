# LCI Service API
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) 
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

A simple FastAPI service that provides Life Cycle Inventory (LCI) data through REST endpoints. This project simulates external LCI data services and returns formatted inventory data for sustainable products.

## Features

- REST API endpoints for LCI data
- SQLite database with sample LCI products and flows
- Automatic database seeding with sample data
- Clean architecture with routes, models, and database layers

## Prerequisites

- Python 3.12+
- pip (Python package manager)

## Installation

1. Clone the repository:
```sh
git clone https://github.com/wellingtonrsantos/aps-lci-service.git
cd aps-lci-service
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

3. Install dependencies:
```sh
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server using uvicorn:

```sh
uvicorn app.main:app --reload --port 9000
```

The API will be available at `http://localhost:9000`

## API Endpoints

### List All Products

```
GET /api/lci/products
```

Returns a list of all available LCI products with their IDs, names, and descriptions.

### Get Product LCI Data

```
GET /api/lci/products/{product_id}
```

Returns detailed LCI flows for a specific product, including:
- Flow Name
- Amount
- Unit
- Flow Direction
- UEV (Unit Emergy Value)
- Category (R: Renewable, N: Non-renewable, F: External Resources)

## Database Structure

The application uses SQLite with two main models:

- `LCIProduct`: Stores product information
  - id
  - name
  - description

- `LCIFlow`: Stores LCI flows for each product
  - id
  - product_id
  - flow_name
  - amount
  - unit
  - flow_direction
  - uev
  - category

## Sample Data

The sample LCI data is stored in `/data/seed_lci.json`. This file contains pre-configured data for various sustainable products including:
- Solar Water Heater
- Electric Bicycle
- Biodigester
- Wind Turbine
- Solar Refrigerator
- And more...

To modify the sample data:
1. Edit the `/data/seed_lci.json` file
2. Delete the existing SQLite database file
3. Restart the application - it will automatically create a new database with your updated data

Note: The database will be automatically seeded with the data from `seed_lci.json` when the application starts and no existing database is found.

## Development

The project structure follows a modular approach:
```
app/
├── main.py          # Application entry point
├── routes/          # API endpoints
├── models/          # SQLModel definitions
└── db/              # Database configuration
```

## Dependencies

- FastAPI: Web framework
- SQLModel: SQL database ORM
- Uvicorn: ASGI server
- SQLite: Database

## License

This project is licensed under the MIT License - see the LICENSE file for details.