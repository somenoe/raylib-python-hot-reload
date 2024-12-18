# Raylib Python Hot Reload

A proof of concept of using hot reload with the raylib library in Python.

## requirements

- **[uv](https://github.com/astral-sh/uv)** package and project manager
- **[jurigged](https://github.com/breuleux/jurigged)** hot reload tool
- **[raylib](https://www.raylib.com/)** library for videogames
- **[raylib python](https://electronstudio.github.io/raylib-python-cffi/)** for raylib python binding
- **[pyinstaller](https://pyinstaller.org/en/stable/)** build .exe file

## set up virtual environment

1. setup
	```bash
	uv venv
	```

2. activate
	```bash
	.venv\Scripts\activate
	```

3. deactivate (same terminal after activate)
	```bash
	.venv\Scripts\deactivate
	```

## .bat files

- `aider` call ai chatbot (optional)
- `install` for install required deps and make python virsul environment
- `freeze` for generate requirements.txt
- `dev` for run during development
- `build` for build .exe file
- `exe` for run preview .exe file from `build`
