# Virtual Environment (venv)
"""
A virtual environment in Python is a self-contained directory that contains:
- A specific Python interpreter.
- Installed libraries/packages for a project.
Purpose:
- Isolate dependencies for a specific project from the global environment.
- Prevent conflicts between different projects using different library versions.

Steps to Use Virtual Environment:
1. Create a virtual environment.
2. Activate the environment.
3. Install dependencies locally for the project.

Commands:
- Create a virtual environment:
  python -m venv <env_name>

- Activate the virtual environment:
  # Windows:
  <env_name>\Scripts\activate

  # Linux/Mac:
  source <env_name>/bin/activate

- Deactivate the virtual environment:
  deactivate

- Check installed packages in the environment:
  pip list

- Remove the virtual environment (simply delete the folder):
  rm -rf <env_name>
"""

#----------------------------------------------------------------------

# PIP (Python Package Index Installer)
"""
PIP is the package manager for Python. It is used to:
- Install packages from the Python Package Index (PyPI).
- Manage dependencies for your Python projects.

Key Idea:
 When using pip, it doesn't inherently manage isolation. However, when you use pip inside a virtual environment (created manually using venv or virtualenv), it installs packages only for that specific project.

Details:
The virtual environment for a project contains all the dependencies needed for that project.
This is manually set up, and you need to activate the virtual environment to use the installed packages.

Example:
Setting up a project with pip:
Virtual environment: myproject_env/
Installed packages: django, requests, etc., specific to that project.
Packages are available only when the virtual environment is activated.

Common Commands:
- Install a package:
  pip install <package_name>

- Install a specific version of a package:
  pip install <package_name>==<version>

- Upgrade a package:
  pip install --upgrade <package_name>

- Uninstall a package:
  pip uninstall <package_name>

- Freeze installed packages into a requirements file:
  pip freeze > requirements.txt

- Install dependencies from a requirements file:
  pip install -r requirements.txt

- Check the version of PIP:
  pip --version

- Upgrade PIP to the latest version:
  python -m pip install --upgrade pip
"""


# ---------------------------------------------------------------------


# PIPX
"""
PIPX is a tool to:
- Install and run Python applications in isolated environments.
- Unlike venv or pip, pipx is designed for globally installed CLI-based Python applications (e.g., black, pylint).

Purpose:
- Keep CLI tools isolated from each other and your global environment.
- Easier to manage globally installed Python tools than pip.


Key Idea:
 pipx creates a dedicated virtual environment for each tool or package you install. This keeps tools isolated from each other and ensures they don’t interfere with other system-wide dependencies or tools.

Details:
Each tool gets its own virtual environment, managed by pipx.
These environments are stored in a directory (e.g., ~/.local/pipx/venvs/ by default).
The tool itself can still be used globally via the command line (thanks to pipx linking the tool’s executable to a location in your system’s PATH).
Example:
 Installing httpie with pipx:
Virtual environment: ~/.local/pipx/venvs/httpie/
Global command: You can run http anywhere, even though it's isolated.


Common Commands:
- Install pipx (if not already installed):
  python -m pip install --user pipx

- Install a Python application globally using pipx:
  pipx install <package_name>

- Run a Python application temporarily without installing it:
  pipx run <package_name>

- Upgrade a globally installed application:
  pipx upgrade <package_name>

- Uninstall a globally installed application:
  pipx uninstall <package_name>

- List all globally installed applications:
  pipx list

"""


# ---------------------------------------------------------------------


# Differences Between venv, PIP, and PIPX
"""
1. Virtual Environment (venv):
   - Purpose: Create isolated Python environments for projects.
   - Typical Usage: Per-project isolation for dependencies.
   - Commands: `python -m venv`, `activate`, `deactivate`.

2. PIP:
   - Purpose: Isolate dependencies for a project.
   - Typical Usage: Install libraries or manage dependencies.
   - Environment Scope: One environment per project.
   - Global Availability: Packages are project-local only.
   - Commands: `pip install`, `pip uninstall`, `pip freeze`.

3. PIPX:
   - Purpose: Isolate CLI tools for global use.
   - Typical Usage: Install tools like `black`, `pylint` without polluting the global environment.
   - Environment Scope: One environment per tool or package.
   - Global Availability: Tool is globally accessible.	
   - Commands: `pipx install`, `pipx run`, `pipx list`.
"""

"""
Virtual Environments in Both Cases
Both pipx and pip rely on virtual environments. Here's how:

pipx Virtual Environment: Automatically created for each tool and managed transparently by pipx.
pip Virtual Environment: Manually created by the user using venv or similar, then packages are installed into it.
"""

"""
Notes:
- Always run python3 -m before pip command
    -m: Ensures you’re running a Python module (like pip) with the specified Python interpreter of the right python version.
    On Linux, always use python3 instead of py.
    Use python3 -m pip to avoid ambiguity and ensure you're installing packages for the correct Python version.
"""