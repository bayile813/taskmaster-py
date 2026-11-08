# app.py
from typing import List

# Feature: storage for task strings
tasks: List[str] = ["Buy groceries", "Clean the room", "Fix Git bugs"]

def display_tasks(task_list: list[str]) -> None:
    """Prints all formatted tasks to the terminal."""
    print("\nYour current Tasks:")
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. [ ] {task}")

def main() -> None:
    """The entry point for the TaskMaster CLI application."""
    print("--- TaskMaster CLI ---")
    print("Welcome to your modern Python task manager!")

if __name__ == "__main__":
    main()
