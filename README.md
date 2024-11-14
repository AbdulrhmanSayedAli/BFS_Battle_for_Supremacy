# BFS: Battle for Supremacy

BFS: Battle for Supremacy is a strategy-based game application written in Python. This project utilizes Poetry for dependency management and packaging, and it enforces code style with Black and Flake8.

## Project Overview

TODO

## Features

TODO

## Requirements

To work with this project, ensure you have the following installed:

- Python 3.8+
- Poetry

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/AbdulrhmanSayedAli/BFS_Battle_for_Supremacy.git
cd BFS_Battle_for_Supremacy
```

### 2. Install Dependencies

Use Poetry to install the project dependencies:

```bash
poetry install
```

This will create a virtual environment and install all the required packages.

### 3. Activate the Virtual Environment

To activate the virtual environment created by Poetry, use:

```bash
poetry shell
```

To deactivate the virtual environment, simply type:

```bash
exit
```

## Running the Application

To start the application in debug mode, use the following command:

```bash
cd bfs_battle_for_supremacy
poetry run python main.py
```

To build the final `exe` file and run it in production mode, use the following command:

```bash
cd bfs_battle_for_supremacy
poetry run pyinstaller main.spec
```

and then locate the `exe` file in `bfs_battle_for_supremacy\dist\bfs\bfs.exe`

## Adding New Packages

To add a new package, use the following Poetry command:

```bash
poetry add <package_name>
```

For development dependencies, use:

```bash
poetry add --dev <package_name>
```

This will automatically update your `pyproject.toml` file.

## Code Formatting and Linting

This project uses Black for code formatting and Flake8 for linting to maintain clean and consistent code.

### Code Formatting

To format the code using Black, run:

```bash
poetry run black .
```

### Linting

To check code for linting issues with Flake8, run:

```bash
poetry run flake8 .
```

You can configure Flake8 settings in the `.flake8` file if you need specific linting rules.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository and clone it locally.
2. Create a new branch for your feature or bugfix.
3. Ensure code quality by running Black and Flake8.
4. Commit your changes and submit a pull request.
