from fastapi import FastAPI

app = FastAPI(title="AI Starter Kit Backend")

@app.get("/health")
def health():
    return {
        "sayhi": "Welcome to the AI starter modified July 8"
    }
