# Project Euler Solutions

Personal solutions for [Project Euler](https://projecteuler.net/) problems.

## Layout

```text
.
├── euler/
│   ├── problem_001.py
│   └── runner.py
└── tests/
    └── test_problem_001.py
```

Each problem module exposes a `solve()` function. Keep final answers out of
comments when possible, since Project Euler asks solvers not to publish large
answer dumps.

## Run a Solution

```powershell
python -m euler.runner 1
```

## Run Tests

```powershell
python -m pytest
```

Install test tooling if needed:

```powershell
python -m pip install pytest
```
