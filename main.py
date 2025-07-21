class HelloWorld:
    """
    A simple class to print 'Hello World' to the console.
    """
    def print_hello_world(self):
        """Prints 'Hello World' to the console."""
        print("Hello World")

def main():
    """Main function to demonstrate HelloWorld usage."""
    hello_world = HelloWorld()
    hello_world.print_hello_world()

if __name__ == "__main__":
    main()