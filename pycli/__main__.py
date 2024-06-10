import sys
from .save import save

def print_usage():
    """
    Prints the usage instructions for the command-line interface.
    """
    print("Usage: img-cli <command> <options>")
    print("Commands:")
    print("save <filename> - Save an image from clipboard")

def main():
    """
    Entry point of the command-line interface.
    Parses the command-line arguments and executes the corresponding command.
    """
    args = sys.argv[1:]
    if not args:
        print_usage()
        return
    if args[0] == 'save':
        if len(args) < 2:
            print("Error: save command requires a filename")
            return
        save(args[1])

if __name__ == '__main__':
    main()