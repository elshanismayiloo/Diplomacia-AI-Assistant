from fastapi import FastAPI

app = FastAPI(
    title="Diplomacia AI Assistant",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "project": "Diplomacia AI Assistant",
        "status": "running",
        "version": "0.1.0"
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }
