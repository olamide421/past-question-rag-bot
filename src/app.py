# src/app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager
from src.rag_pipeline import load_rag_chain
from src.config import HOST, PORT

qa_chain = None


class Query(BaseModel):
    q: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Load the RAG chain when app starts
    global qa_chain
    qa_chain = load_rag_chain()
    yield
    # Shutdown: cleanup code here if needed
    # qa_chain = None


# Move app initialization here, after lifespan is defined
app = FastAPI(title="Past Questions RAG Bot", lifespan=lifespan)


@app.post("/ask")
def ask(query: Query):
    if not query.q.strip():
        raise HTTPException(status_code=400, detail="Query must not be empty")
    result = qa_chain.run(query.q)
    return {"answer": result}


@app.get("/")
def root():
    return {"msg": "Past Questions RAG Bot is running"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.app:app", host=HOST, port=PORT, reload=True)
