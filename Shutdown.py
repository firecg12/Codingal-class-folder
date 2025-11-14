import sys

def shutdown():
    """
    Initiates a system shutdown.
    """
    choice = input("System is shutting down. Press Y to continue... else N to cancel: ")

    if choice.lower() == 'y':
        print("Shutting down the system...")
        print("System has been shut down.")
        sys.exit()  # Exits the program
    elif choice.lower() == 'n':
        print("Shutdown cancelled.")
        sys.exit()
    else:
        print("Invalid input. Shutdown cancelled.")
        sys.exit()

shutdown()
