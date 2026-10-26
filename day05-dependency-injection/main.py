from fastapi import Depends, FastAPI

app = FastAPI(title="Day 5 - Dependency Injection")


def get_current_user(username: str = "alice"):
    return {
        "username": username,
        "role": "admin",
    }


def get_app_config():
    return {
        "app_name": "AI FDE Learning",
        "model_name": "gpt-test-model",
    }


@app.get("/")
def root():
    return {"message": "Day 5 is running"}


@app.get("/profile")
def get_profile(user: dict = Depends(get_current_user)):
    return {"profile": user}


@app.get("/dashboard")
def get_dashboard(user: dict = Depends(get_current_user)):
    return {
        "message": "Welcome to dashboard",
        "user": user,
    }


@app.get("/config")
def get_config(config: dict = Depends(get_app_config)):
    return {"config": config}