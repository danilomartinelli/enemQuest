---

# FastAPI Application

This is a FastAPI application for managing and answering questions. It includes features for creating, reading, updating, and deleting questions, as well as a user ranking system based on their scores.

## Features

- Create, read, update, and delete questions.
- Submit answers to questions and calculate scores.
- User ranking system with different levels based on scores.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/fastapi-question-app.git
   cd fastapi-question-app
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory of the project.
   - Add the following environment variables:

     ```env
     MONGO_DB_URI=mongodb://root:password@localhost:27017/
     ```

   Replace `MONGO_DB_URI` with your MongoDB connection URI.

5. Run the application:

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

The application should now be running locally at `http://localhost:8000`.

## API Documentation

- Swagger UI: `http://localhost:8000/docs`

## Usage

You can use the provided API endpoints to manage questions and user answers. Here are some examples:

- Create a question:

  ```bash
  POST /questions/
  ```

- Retrieve a list of questions:

  ```bash
  GET /questions/
  ```

- Submit an answer to a question:

  ```bash
  POST /questions/{question_id}/answer
  ```

- Retrieve user ranking:

  ```bash
  GET /users/{user_id}/ranking
  ```
