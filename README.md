# Todo CLI Application

A simple command-line interface (CLI) application for managing your todo list, built with Python.

## Features

- Add new tasks with titles and optional descriptions
- List all tasks with their completion status
- Data persistence using JSON storage

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Bharathsai-Gella/ado-ai.git
cd ado-ai
```

2. Install the requirements:
```bash
pip install -r requirements.txt
```

3. Make the script executable:
```bash
chmod +x src/todo.py
```

## Usage

The application supports the following commands:

### Add a new task
```bash
./src/todo.py add "Task title" -d "Optional task description"
```

### List all tasks
```bash
./src/todo.py list
```

### Show help
```bash
./src/todo.py --help
```

## Data Storage

Tasks are stored in a `tasks.json` file in the root directory. Each task contains:
- Unique ID
- Title
- Description (optional)
- Creation timestamp
- Completion status