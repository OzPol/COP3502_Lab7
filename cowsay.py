import sys
from heifer_generator import HeiferGenerator

# Define a function to list the available cows
def list_cows(cows):
    cow_names = [cow.get_name() for cow in cows]
    print("Cows available: " + ' '.join(cow_names))

"""  also try this
def list_cows(cows):
    print("Cows available: " + " ".join([cow.get_name() for cow in cows]))
    """
# Define a function to find a cow by name
def find_cow(name, cows):
     # Loop through all cows and return the one with the matching name
    for cow in cows:
        if cow.get_name() == name:
            return cow
    # If no cow is found, return None
    return None

# Define a function to print a message using a cow image
def cowsay(message, cow=None):
    # If no cow is specified, use the default cow named "heifer"
    if cow is None:
        cow = find_cow("heifer", cow)

    # If no default cow is found, print an error message and return
    if cow is None:
        print("Could not find default cow!")
        return
    # Print the message and the cow image
    print(message)
    print(cow.get_image())

# Define the main function to be executed when the script is run
def main():
    # Get a list of all available cows
    cows = HeiferGenerator.get_cows()

    # Get any command line arguments provided after the script name
    args = sys.argv[1:]

    # If no arguments are provided, print the usage message and return
    if len(args) == 0:
        print("Usage: cowsay.py [-l] [-n name] message")
        return
    
    # If the first argument is "-l", list the available cows and return
    if args[0] == '-l':
        list_cows(cows)
        return
    
    # If the first argument is "-n", get the named cow and remove the "-n" and cow name arguments
    cow = None
    if args[0] == '-n':
        if len(args) < 2:
            print("Error: no cow specified")
            return
        cow = find_cow(args[1], cows)
        if cow is None:
            print("Could not find {} cow!".format(args[1]))
            return
        args = args[2:]

    # If no message is provided, print an error message and return
    if len(args) == 0:
        print("Error: no message specified")
        return

    # Join all remaining arguments to form the message string
    message = " ".join(args)
    # If no cow is specified, use the first available cow
    print(message)
    if cow is None:
        cow = cows[0]
    
    # Print the message using the specified cow
    print(cow.get_image())
# If the script is run directly (as opposed to being imported), call the main functio
if __name__ == '__main__':
    main()


"""First attempt failed, ???? check this code later and see what went wrong here
def main():
    cows = get_cows()

    if len(sys.argv) == 2 and sys.argv[1] == "-l":
        list_cows(cows)
    elif len(sys.argv) == 2:
        cowsay(sys.argv[1])
    elif len(sys.argv) == 4 and sys.argv[1] == "-n":
        cow = find_cow(sys.argv[2], cows)
        if cow is None:
            print(f"Could not find {sys.argv[2]} cow!")
        else:
            cowsay(sys.argv[3], cow)
    else:
        print("Invalid arguments")
        print("Usage: python3 cowsay.py -l")
        print("       python3 cowsay.py MESSAGE")
        print("       python3 cowsay.py -n COW MESSAGE")

"""
