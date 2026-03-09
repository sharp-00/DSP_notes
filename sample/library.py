#!/usr/bin/env python3

def add_book(library, isbn, title, copies):
    if isbn in library:
        raise ValueError("Book already exists")

    if copies < 0:
        raise ValueError("Copies cannot be negative")

    library[isbn] = {
        "title": title,
        "copies": copies,
        "issued": 0
    }
    return library

def issue_book(library, isbn):
    if isbn not in library:
        raise KeyError("Book not found")

    book = library[isbn]

    if book["issued"] >= book["copies"]:
        raise ValueError("No copies available")

    book["issued"] += 1
    return book["issued"]

def return_book(library, isbn):
    if isbn not in library:
        raise KeyError("Book not found")

    book = library[isbn]

    if book["issued"] == 0:
        raise ValueError("No issued copies to return")

    book["issued"] -= 1
    return book["issued"]

def available_copies(library, isbn):
    if isbn not in library:
        raise KeyError("Book not found")

    book = library[isbn]
    return book["copies"] - book["issued"]

def clean_library(library):
    """
    Remove books with zero total copies
    """
    return {
        isbn: book
        for isbn, book in library.items()
        if book["copies"] > 0
    }
