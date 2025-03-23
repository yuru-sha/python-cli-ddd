# python-cli-ddd

[![CI](https://github.com/yuru-sha/python-cli-ddd/actions/workflows/ci.yml/badge.svg)](https://github.com/yuru-sha/python-cli-ddd/actions/workflows/ci.yml)

A Python CLI application demonstrating Domain-Driven Design (DDD) and Clean Architecture principles.

## Features

- Task management through CLI commands
- SQLite database for data persistence
- Clean Architecture with DDD principles
- Dependency Injection using `dependency-injector`
- Type hints and strict type checking
- Comprehensive linting with `ruff` and `mypy`

## Requirements

- Python 3.12 or higher
- Poetry or pip for dependency management

## Installation

```bash
# Clone the repository
git clone https://github.com/yuru-sha/python-cli-ddd.git
cd python-cli-ddd

# Install dependencies
pip install -e .
```

## Available Commands

### List Tasks
Display all tasks in a formatted table:
```bash
list-tasks
```

### Print Message
Print a message with optional debug information:
```bash
print-message "Your message"
```

## Development

### Setup Development Environment

```bash
# Install development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
make test
```

### Linting

```bash
make lint
```

## Project Structure

```
src/python_cli_ddd/
├── domain/           # Domain layer (entities, repositories)
├── application/      # Application layer (use cases)
├── infrastructure/   # Infrastructure layer (database, external services)
└── interface/        # Interface layer (CLI commands)
```

## License

MIT License