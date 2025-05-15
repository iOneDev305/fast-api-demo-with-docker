# FastAPI Clean Architecture Demo

This project demonstrates a FastAPI application structured using Clean Architecture principles.

## Project Structure

```
fastapi-demo/
├── app/
│   ├── domain/              # Enterprise business rules
│   │   ├── models/         # Domain entities
│   │   └── repositories/   # Repository interfaces
│   ├── application/        # Application business rules
│   │   └── services/      # Use cases
│   ├── infrastructure/     # Frameworks and drivers
│   │   └── repositories/  # Repository implementations
│   └── presentation/      # Interface adapters
│       └── api/          # API routes
├── main.py               # Application entry point
└── requirements.txt      # Project dependencies
```

## Layers

1. **Domain Layer** (`app/domain/`)
   - Contains enterprise business rules
   - Independent of other layers
   - Contains entities and repository interfaces

2. **Application Layer** (`app/application/`)
   - Contains application business rules
   - Orchestrates the flow of data to and from entities
   - Implements use cases

3. **Infrastructure Layer** (`app/infrastructure/`)
   - Contains frameworks and tools
   - Implements interfaces defined in the domain layer
   - Handles external concerns like databases, file systems, etc.

4. **Presentation Layer** (`app/presentation/`)
   - Contains interface adapters
   - Converts data from the format most convenient for entities and use cases
   - Contains API routes and controllers

## Setup and Running

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /users` - Get all users
- `GET /users/{user_id}` - Get a specific user by ID

## Clean Architecture Benefits

1. **Independence of Frameworks**: The core business logic is independent of any external frameworks
2. **Testability**: Business rules can be tested without UI, database, or external elements
3. **Independence of UI**: The UI can change easily without changing the rest of the system
4. **Independence of Database**: The database can be swapped out without affecting the business rules
5. **Independence of External Agency**: Business rules don't know about the outside world 