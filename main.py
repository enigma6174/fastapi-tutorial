from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World!"}


@app.get("/posts")
def get_posts():
    return {"data": "DUMMY_POST_DATA"}


@app.post("/create/posts")
def create_posts(payload: dict = Body(...)):
    print(f'[INFO] payload: {payload}')
    return {"new_post": {"title": payload["title"], "content": payload["content"]}}


