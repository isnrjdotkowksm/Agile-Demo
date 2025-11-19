from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

# Optional: add a root endpoint so "/" works too
@app.get("/")
def root():
    return {"message": "Hello! FastAPI is running."}
