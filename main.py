from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Nguyen Van A",
        "category": "programming",
        "year": 2022,
        "is_available": True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Tran Van B",
        "category": "web",
        "year": 2021,
        "is_available": False
    }
]


@app.get("/books/available")
def get_book_available():
    lst = []
    for i in books:
        if i["is_available"]:
            lst.append(i)
    return lst

@app.get("/books/borrowed")
def get_book_borrowed():
    lst = []
    for i in books:
        if not i["is_available"]:
            lst.append(i)
    return lst