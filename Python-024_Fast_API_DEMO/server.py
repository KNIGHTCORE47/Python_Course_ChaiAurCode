from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def Home_Route():
    return {"message": "Home Page"}


@app.get("/about")
async def About_Route():
    return {"message": "About Page"}


@app.get("/contact")
async def Contact_Route():
    return {"message": "Contact Page"}


uvicorn.run(app)