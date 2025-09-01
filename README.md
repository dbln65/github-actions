## Simple Python Math App with CI

This repository contains a simple Python application that demonstrates basic functions and integrates with GitHub Actions for automated testing (CI).
It shows how to structure a Python project, write unit tests, and automatically verify code on each push.

## 📂 Project Structure

```bash
your-repo/
├── simple_app.py        # Main Python application
├── test_simple_app.py   # Unit tests for the app
└── .github/
    └── workflows/
        └── python-ci.yml  # GitHub Actions workflow for CI
```
## ⚙️ How It Works

| Component              | Description                                                                                                                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Python Application** | `simple_app.py` contains two functions: `square(x)` → returns x², `cube(x)` → returns x³. The main program calculates squares and cubes for the numbers `[2, 3, 4]` and prints them. |
| **Unit Testing**       | `test_simple_app.py` tests the `square` and `cube` functions using `pytest`. No user input is required, so it can run automatically in CI.                                           |
| **CI Workflow**        | `python-ci.yml` triggers on **push** to the `main` branch. Steps include: checkout repo, setup Python 3.11, install `pytest`, run tests.                                             |


## ▶️ Running Locally

1. Install Python: Python 3.11 or higher.

2. Install pytest (if not already installed):
```bash
pip install pytest
```
3. Run the application:
```bash
python simple_app.py
```
Expected output:
```bash
Squares:
2^2 = 4
3^2 = 9
4^2 = 16

Cubes:
2^3 = 8
3^3 = 27
4^3 = 64
```
4. Run unit tests:
```bash
pytest
```
All tests should pass successfully.


## 🛠 Requirements

- Python 3.11 or higher

- pytest for testing

- GitHub Actions for automated CI (optional)

## 🚀 Continuous Integration with GitHub Actions

- Trigger: Pushes to the main branch.

- Workflow steps:

