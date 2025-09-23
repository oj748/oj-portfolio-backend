from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os
from typing import Dict, Any

app = FastAPI(title="Portfolio Backend API", version="1.0.0")

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load knowledge content
def load_knowledge():
    with open("knowledge.txt", "r", encoding="utf-8") as f:
        return f.read()

knowledge_content = load_knowledge()

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response: str

@app.get("/")
async def root():
    return {
        "message": "Portfolio Backend API",
        "version": "1.0.0",
        "available_routes": {
            "/": "This homepage with API information",
            "/query": "POST endpoint to query about portfolio information"
        },
        "usage": {
            "endpoint": "/query",
            "method": "POST",
            "body": {"query": "Your question about the portfolio"}
        }
    }

@app.post("/query", response_model=QueryResponse)
async def query_portfolio(request: QueryRequest):
    try:
        # Prepare the prompt with knowledge context
        prompt = f"""
        Based on the following information about the portfolio owner, please answer the query.
        
        Portfolio Information:
        {knowledge_content}
        
        Query: {request.query}
        
        Please provide a helpful and accurate response based on the information provided.
        """
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions about a portfolio based on the provided information."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        return QueryResponse(response=response.choices[0].message.content)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
