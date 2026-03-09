#!/usr/bin/env python3

from library import *

def test_add_book_success():
    lib = {}
    add_book(lib, 101, "Python Basics", 3)
    assert 101 in lib
    assert lib[101]["copies"] == 3
    assert lib[101]["issued"] == 0

def test_add_duplicate_book():
    lib = {}
    add_book(lib, 101, "Python Basics", 3)

    try:
        add_book(lib, 101, "Python Basics", 3)
        assert False   # should not reach here
    except ValueError:
        assert True

def test_issue_book():
    lib = {}
    add_book(lib, 201, "DSA", 2)
    issue_book(lib, 201)
    assert lib[201]["issued"] == 1

def test_issue_book_no_copies():
    lib = {}
    add_book(lib, 301, "AI", 1)
    issue_book(lib, 301)

    try:
        issue_book(lib, 301)
        assert False
    except ValueError:
        assert True

def test_return_book():
    lib = {}
    add_book(lib, 401, "ML", 2)
    issue_book(lib, 401)
    return_book(lib, 401)
    assert lib[401]["issued"] == 0

def test_available_copies():
    lib = {}
    add_book(lib, 501, "DBMS", 5)
    issue_book(lib, 501)
    issue_book(lib, 501)
    assert available_copies(lib, 501) == 3

def test_clean_library():
    lib = {}
    add_book(lib, 601, "OS", 0)
    add_book(lib, 602, "CN", 2)
    clean = clean_library(lib)
    assert 601 not in clean
    assert 602 in clean
