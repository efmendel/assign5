import argparse
import json
import sys
from pathlib import Path
from typing import List, Optional

from .user_manager import UserProfileManager


# Sort profiles by the specified key
def _sort_profiles(manager: UserProfileManager, key: str):
    # Sort by age
    if key == "age":
        return manager.sort_profiles_by_age()
    # Sort by name
    if key == "name":
        return manager.sort_profiles_by_name()
    # Sort by email
    if key == "email":
        return manager.sort_profiles_by_email()
    # Sort by location
    if key == "location":
        return manager.sort_profiles_by_location()
    raise SystemExit(f"Unknown sort key: {key}")


def _write_output(obj, output_path: Optional[str]):
    if output_path:
        out_path = Path(output_path)
        with out_path.open("w") as f:
            json.dump(obj, f, indent=4)
    else:
        json.dump(obj, sys.stdout, indent=4)
        sys.stdout.write("\n")


def main(argv: Optional[List[str]] = None) -> int:
    # Set up argument parser
    parser = argparse.ArgumentParser(description="User profiles processor")
    parser.add_argument("--input", "-i", required=True, help="Path to input JSON (single user or list)")
    parser.add_argument("--output", "-o", help="Path to write output JSON (defaults to stdout)")
    parser.add_argument(
        "--sort",
        choices=["age", "name", "email", "location"],
        default="age",
        help="Sort key (default: age)",
    )
    args = parser.parse_args(argv)

    # Create manager and load profiles
    manager = UserProfileManager()
    manager.load_profiles_from_json(args.input)
    
    # Check if any profiles were loaded
    if len(manager.user_profiles) == 0:
        raise SystemExit("No valid profiles loaded from input file.")
    
    # Sort and output
    sorted_profiles = _sort_profiles(manager, args.sort)
    output_list = [p.to_dict() for p in sorted_profiles]
    _write_output(output_list, args.output)
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())