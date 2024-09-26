class StringManipulation:
    # Get a string from user input
    def getString(self):
        self.s = input("Enter a string: ")

    # Print the string in uppercase
    def printString(self):
        print(self.s.upper())

# Example usage:
str_manip = StringManipulation()
str_manip.getString()
str_manip.printString()
