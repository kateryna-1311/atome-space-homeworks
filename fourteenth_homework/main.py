"""Small FastAPI application to practice testing with pytest."""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class BookCreate(BaseModel):
    title: str
    author: str
    year: int


books: list[dict] = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 2, "title": "Dune", "author": "Frank Herbert", "year": 1965},
    {"id": 3, "title": "Foundation", "author": "Isaac Asimov", "year": 1951},
]


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(payload: BookCreate):
    new_id = max((book["id"] for book in books), default=0) + 1
    new_book = {"id": new_id, **payload.model_dump()}
    books.append(new_book)
    return new_book


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": f"Book {book_id} deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
