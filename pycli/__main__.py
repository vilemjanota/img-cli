import sys
from .save import save

def print_usage():
    """
    Prints the usage instructions for the command-line interface.
    """
    print("Usage: img-cli <command> <options>")
    print("Commands:")
    print("save <options> <filename> - Save an image from clipboard")
    print("\tOptions:")
    print("\t-h <height> - Resize the image to a specific height")
    print("\t-w <width> - Resize the image to a specific width")

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
        if len(args) == 2:
            save(args[1], 'original', 'original')
            return
        else:
            height = 'original'
            width = 'original'
            # Check if -h flag is present and if the next argument is a valid number
            if "-h" in args and args.index("-h") != len(args)-1 and args[args.index("-h")+1].isalnum():
                height = args[args.index("-h")+1]
                args.pop(args.index("-h")+1)
                args.remove("-h")
                
            # Check if -w flag is present and if the next argument is a valid number
            if "-w" in args and args.index("-w") != len(args)-1 and args[args.index("-w")+1].isalnum():
                width = args[args.index("-w")+1]
                args.pop(args.index("-w")+1)
                args.remove("-w")
            save(args[1], height, width)
            return


    print("Error: unknown command")
    print_usage()

if __name__ == '__main__':
    main()