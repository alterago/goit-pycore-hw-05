"""Task 4: the assistant bot from homework 4 with error handling by a decorator.

Commands (case-insensitive): hello, add <name> <phone>, change <name> <phone>,
phone <name>, all, close / exit. Ctrl+C or Ctrl+D also exits.
"""

from functools import wraps

Contacts = dict[str, str]


def input_error(func):
    """Turn input errors raised by a handler into messages for the user."""

    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except IndexError:
            return "Enter the argument for the command"
        except KeyError:
            return "Contact not found."

    return inner


def parse_input(user_input: str) -> tuple[str, ...]:
    """Split the input into a lower-case command and its arguments."""
    parts = user_input.split()
    if not parts:
        return ("",)
    cmd, *args = parts
    return cmd.strip().lower(), *args


def find_name(contacts: Contacts, name: str) -> str:
    """Return the stored name that matches ``name`` regardless of case.

    Raises KeyError when there is no such contact.
    """
    for stored in contacts:
        if stored.lower() == name.lower():
            return stored
    raise KeyError(name)


@input_error
def add_contact(args: list[str], contacts: Contacts) -> str:
    name, phone = args  # ValueError unless exactly two arguments
    try:
        name = find_name(contacts, name)  # keep the stored spelling
    except KeyError:
        pass
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: list[str], contacts: Contacts) -> str:
    name, phone = args  # ValueError unless exactly two arguments
    contacts[find_name(contacts, name)] = phone  # KeyError if unknown
    return "Contact updated."


@input_error
def show_phone(args: list[str], contacts: Contacts) -> str:
    name = args[0]  # IndexError when the name is missing
    return contacts[find_name(contacts, name)]  # KeyError if unknown


@input_error
def show_all(contacts: Contacts) -> str:
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    contacts: Contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
        except (KeyboardInterrupt, EOFError):
            # Ctrl+C or Ctrl+D ends the bot the same way as "exit".
            print("\nGood bye!")
            break
        command, *args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
