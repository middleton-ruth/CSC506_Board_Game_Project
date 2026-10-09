"""
Input Validation Utilities
Best practices: Robust error handling, user-friendly prompts.
"""

from typing import Optional, List


def get_int_input(prompt: str, min_val: Optional[int] = None, max_val: Optional[int] = None, default: Optional[int] = None) -> int:
    """
    Get validated integer input from user.

    Args:
        prompt: Prompt to display
        min_val: Minimum acceptable value
        max_val: Maximum acceptable value
        default: Default value if user presses Enter

    Returns:
        Validated integer
    """
    while True:
        try:
            user_input = input(prompt).strip()

            if not user_input and default is not None:
                return default

            value = int(user_input)

            if min_val is not None and value < min_val:
                print(f"  ✗ Value must be at least {min_val}")
                continue

            if max_val is not None and value > max_val:
                print(f"  ✗ Value must be at most {max_val}")
                continue

            return value

        except ValueError:
            print("  ✗ Please enter a valid number")
        except KeyboardInterrupt:
            print("\n  Cancelled")
            raise


def get_float_input(prompt: str, min_val: Optional[float] = None, max_val: Optional[float] = None, default: Optional[float] = None) -> float:
    """
    Get validated float input from user.

    Args:
        prompt: Prompt to display
        min_val: Minimum acceptable value
        max_val: Maximum acceptable value
        default: Default value if user presses Enter

    Returns:
        Validated float
    """
    while True:
        try:
            user_input = input(prompt).strip()

            if not user_input and default is not None:
                return default

            value = float(user_input)

            if min_val is not None and value < min_val:
                print(f"  ✗ Value must be at least {min_val}")
                continue

            if max_val is not None and value > max_val:
                print(f"  ✗ Value must be at most {max_val}")
                continue

            return value

        except ValueError:
            print("  ✗ Please enter a valid number")
        except KeyboardInterrupt:
            print("\n  Cancelled")
            raise


def get_yes_no_input(prompt: str, default: Optional[bool] = None) -> bool:
    """
    Get yes/no input from user.

    Args:
        prompt: Prompt to display
        default: Default value if user presses Enter

    Returns:
        True for yes, False for no
    """
    while True:
        if default is True:
            prompt_text = f"{prompt} [Y/n]: "
        elif default is False:
            prompt_text = f"{prompt} [y/N]: "
        else:
            prompt_text = f"{prompt} [y/n]: "

        user_input = input(prompt_text).strip().lower()

        if not user_input and default is not None:
            return default

        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            return False
        else:
            print("  ✗ Please enter 'y' or 'n'")


def get_choice_input(prompt: str, choices: List[str], default: Optional[str] = None) -> str:
    """
    Get validated choice from a list of options.

    Args:
        prompt: Prompt to display
        choices: List of valid choices
        default: Default choice if user presses Enter

    Returns:
        Selected choice
    """
    choices_lower = [c.lower() for c in choices]

    while True:
        user_input = input(prompt).strip().lower()

        if not user_input and default is not None:
            return default

        if user_input in choices_lower:
            return user_input

        print(f"  ✗ Please enter one of: {', '.join(choices)}")


def get_string_input(prompt: str, min_length: int = 0, max_length: Optional[int] = None, allow_empty: bool = False) -> str:
    """
    Get validated string input from user.

    Args:
        prompt: Prompt to display
        min_length: Minimum string length
        max_length: Maximum string length
        allow_empty: Whether to allow empty strings

    Returns:
        Validated string
    """
    while True:
        user_input = input(prompt).strip()

        if not user_input:
            if allow_empty:
                return user_input
            print("  ✗ Input cannot be empty")
            continue

        if len(user_input) < min_length:
            print(f"  ✗ Input must be at least {min_length} characters")
            continue

        if max_length and len(user_input) > max_length:
            print(f"  ✗ Input must be at most {max_length} characters")
            continue

        return user_input


def confirm_action(action: str) -> bool:
    """
    Ask user to confirm an action.

    Args:
        action: Description of action to confirm

    Returns:
        True if confirmed, False otherwise
    """
    return get_yes_no_input(f"Are you sure you want to {action}?", default=False)


def main():
    """Test input validation functions."""
    print("=" * 80)
    print("INPUT VALIDATION TEST")
    print("=" * 80)

    # Test integer input
    print("\n1. Integer Input Test:")
    age = get_int_input("Enter a number between 1 and 100: ", min_val=1, max_val=100, default=50)
    print(f"  You entered: {age}")

    # Test yes/no input
    print("\n2. Yes/No Input Test:")
    confirm = get_yes_no_input("Do you like board games?", default=True)
    print(f"  You answered: {'Yes' if confirm else 'No'}")

    # Test choice input
    print("\n3. Choice Input Test:")
    choice = get_choice_input("Choose difficulty (easy/medium/hard): ", ['easy', 'medium', 'hard'], default='medium')
    print(f"  You chose: {choice}")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()
