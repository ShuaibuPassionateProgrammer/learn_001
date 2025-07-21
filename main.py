import sys
from typing import Optional

def print_message(message: str) -> None:
    """
    Prints the provided message to the console.
    Args:
        message (str): The message to print.
    """
    print(message)

def get_message_from_args() -> Optional[str]:
    """
    Retrieves a custom message from command-line arguments if provided.
    Returns:
        Optional[str]: The custom message or None if not provided.
    """
    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:])
    return None

def main() -> None:
    """
    Main function to print a message. If a command-line argument is provided, it prints that message.
    Otherwise, it prompts the user for input, defaulting to 'Hello World'.
    """
    message = get_message_from_args()
    if not message:
        try:
            user_input = input("Enter a message to print (or press Enter for default): ").strip()
            message = user_input if user_input else "Hello World"
        except (EOFError, KeyboardInterrupt):
            message = "Hello World"
    print_message(message)

if __name__ == "__main__":
    main()