#1
class StringManipulator:
    def __init__(self):
        self.text = ""

    def getString(self):
        """Gets a string from console input."""
        self.text = input("Enter a string: ")

    def printString(self):
        """Prints the stored string in uppercase."""
        print(self.text.upper())
        
obj = StringManipulator()
obj.getString()
obj.printString()
