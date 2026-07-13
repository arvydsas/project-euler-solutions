"""Command-line runner for Project Euler solutions."""

from __future__ import annotations

import argparse
import importlib
from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run a Project Euler solution.")
    parser.add_argument("problem", type=int, help="Problem number to run.")
    args = parser.parse_args(argv)

    module_name = f"euler.problem_{args.problem:03d}"
    module = importlib.import_module(module_name)
    print(module.solve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
