from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FDE!", "day": 2}

@app.get("/about")
def about():
    return {
        "project": "AI FDE Learning",
        "purpose": "Learn to build AI applications"
    }


@app.get("/hello/{name}")
def say_hello(name: str):
    return {
        "message": f"Hello, {name}!",
        "role": "FDE"
    }


@app.get("/search")
def search(keyword: str, page: int = 1):
    return {
        "keyword": keyword,
        "page": page,
        "message": f"Searching for {keyword}"
    }
