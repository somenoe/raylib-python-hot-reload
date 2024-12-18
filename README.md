# Raylib Python Hot Reload

This project shows how to use hot reload with the Raylib library in Python.

## What you need

-   **uv:** A tool to manage Python projects. ([https://github.com/astral-sh/uv](https://github.com/astral-sh/uv))
-   **jurigged:** A tool for hot reloading code. ([https://github.com/breuleux/jurigged](https://github.com/breuleux/jurigged))
-   **raylib:** A library for making video games. ([https://www.raylib.com/](https://www.raylib.com/))
-   **raylib-python:**  A way to use raylib with Python. ([https://electronstudio.github.io/raylib-python-cffi/](https://electronstudio.github.io/raylib-python-cffi/))
-   **pyinstaller:** A tool to create .exe files. ([https://pyinstaller.org/en/stable/](https://pyinstaller.org/en/stable/))

## How to set up the project

1.  **Create a virtual environment:**
    ```bash
    uv venv
    ```

2.  **Activate the virtual environment:**
    ```bash
    .venv\Scripts\activate
    ```

3.  **Deactivate the virtual environment:** (Run this in the same terminal after activating)
    ```bash
    .venv\Scripts\deactivate
    ```

## .bat files (Windows)

-   `aider`:  Use an AI chatbot (optional).
-   `install`: Installs the necessary tools and creates the virtual environment.
-   `freeze`: Creates a list of required packages.
-   `dev`: Runs the project during development.
-   `build`: Creates an .exe file.
-   `exe`: Runs the .exe file created by `build`.
