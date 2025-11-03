#!/usr/bin/env python3

import argparse
import json
import os
from typing import List, Dict
from datetime import datetime

# Constants
TASKS_FILE = "tasks.json"

def load_tasks() -> List[Dict]:
    """Load tasks from JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks: List[Dict]) -> None:
    """Save tasks to JSON file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(title: str, description: str = "") -> None:
    """Add a new task to the list."""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "created_at": datetime.now().isoformat(),
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task: {title}")

def list_tasks() -> None:
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    
    print("\nTasks:")
    print("-" * 50)
    for task in tasks:
        status = "✓" if task["completed"] else " "
        print(f"[{status}] {task['id']}. {task['title']}")
        if task["description"]:
            print(f"   {task['description']}")
    print("-" * 50)

def main() -> None:
    """Main function to handle CLI commands."""
    parser = argparse.ArgumentParser(description="Simple TODO list CLI application")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Add task command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("-d", "--description", help="Task description", default="")

    # List tasks command
    subparsers.add_parser("list", help="List all tasks")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title, args.description)
    elif args.command == "list":
        list_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()