"""
This module contains helper functions that are used across the project.
"""
from __future__ import annotations

def prompt_non_empty(prompt: str) -> str:
    while True:
        s: str = input(prompt).strip()
        if s != "":
            return s
        print("Empty input is not allowed, try again.")

def clean_name(name: str) -> str:
    return name.title()

def prompt_int(prompt: str, min_val: int = 0, max_val: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Invalid input, please enter a valid integer.")
            continue

        if val < min_val:
            print(f"Value must be at least {min_val}.")
            continue
        if max_val is not None and val > max_val:
            print(f"Value must be at most {max_val}.")
            continue
        return val
    
def prompt_float(prompt: str, min_val: float = 0.0, max_val: float | None = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
        except ValueError:
            print("Invalid input, please enter a valid number.")
            continue

        if val < min_val:
            print(f"Value must be at least {min_val}.")
            continue
        if max_val is not None and val > max_val:
            print(f"Value must be at most {max_val}.")
            continue
        return val
    
def grade_from_percentage(pct: float) -> str:
    if pct >= 90.0:
        return "A"
    elif pct >= 80.0:
        return "B"
    elif pct >= 70.0:
        return "C"
    elif pct >= 60.0:
        return "D"
    else:
        return "F"