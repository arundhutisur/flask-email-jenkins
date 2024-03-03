import pytest
from app import greet_user  # Assume your program is saved in 'your_program_file.py'

def test_greet_user(monkeypatch):
    # Mock the input to return 'Alice'
    monkeypatch.setattr('builtins.input', lambda _: 'Alice')
    
    # Check if the function returns the correct greeting
    assert greet_user() == "Hello, Alice!"