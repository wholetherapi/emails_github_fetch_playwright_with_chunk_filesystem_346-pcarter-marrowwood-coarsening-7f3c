"""Reproduction entry point for the paper's main results."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/default.yaml")
    args = parser.parse_args()
    print(f"running with {args.config}")


if __name__ == "__main__":
    main()
