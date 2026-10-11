\# Day 2 - FastAPI Basics



\## What I learned



\- Created a Python virtual environment.

\- Installed FastAPI.

\- Built a simple API using FastAPI.

\- Created GET endpoints.

\- Used path parameters and query parameters.

\- Tested API endpoints with the browser and FastAPI docs.



\## Endpoints



| Method | Endpoint | Purpose |

|---|---|---|

| GET | `/` | Welcome message |

| GET | `/about` | Project information |

| GET | `/hello/{name}` | Greeting by name |

| GET | `/search?keyword=AI\&page=1` | Search example |



\## Run locally



Activate the virtual environment and run:



```powershell

python -m uvicorn main:app --reload

```



Open the interactive API documentation at `http://127.0.0.1:8000/docs`.



\## Key concepts



\- FastAPI application

\- GET routes

\- Path parameters

\- Query parameters

\- Default parameter values

\- JSON responses

