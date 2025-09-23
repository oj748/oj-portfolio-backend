# Portfolio Backend API

A simple FastAPI-based backend that provides AI-powered responses about portfolio information using OpenAI's GPT-4o-mini model.

## Features

- **Query Endpoint**: `/query` - Ask questions about the portfolio
- **Homepage**: `/` - API information and usage guide
- **Docker Support**: Easy deployment with Docker and Docker Compose

## Setup

### Prerequisites

- Python 3.11+
- OpenAI API Key
- Docker (optional)

### Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
4. Run the application:
   ```bash
   python main.py
   ```

The API will be available at `http://localhost:8000`

### Docker Deployment

1. Set your OpenAI API key in a `.env` file:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

2. Build and run with Docker Compose:
   ```bash
   docker-compose up --build
   ```

## API Usage

### Homepage
- **GET** `/` - Returns API information and available routes

### Query Portfolio
- **POST** `/query`
- **Body**: 
  ```json
  {
    "query": "What are the academic skills?"
  }
  ```
- **Response**:
  ```json
  {
    "response": "The academic skills include strong command over R and Python, strong background in Data Science, and a published technical paper on document-based report generation using officer package of R."
  }
  ```

## Example Queries

- "What is the education background?"
- "What are the hobbies and interests?"
- "Tell me about the extracurricular skills"
- "What programming languages are known?"

## Project Structure

```
├── main.py              # FastAPI application
├── knowledge.txt        # Portfolio information
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker Compose configuration
└── README.md           # This file
```
