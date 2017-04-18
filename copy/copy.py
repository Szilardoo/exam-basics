# This should be the basic replica of the 'cp' command
# If ran from the command line without arguments
# It should print out the usage:
# copy [source] [destination]
# When just one argument is provided print out
# No destination provided
# When both arguments provided and the source is a file
# Read all contents from it and write it to the destination

class Copy():

    def __init__(self, source = "[source]", destination = "[destination]"):
        self.source = source
        self.destination = destination
        self.opportunities()

    def opportunities(self):
        if self.source == "[source]" and self.destination == "[destination]":
            print("copy " + self.source + self.destination)
        elif self.source != "[source]" and self.destination == "[destination]":
            print("No destination provided")
        else:
            self.copy_paste()

    def copy_paste(self):
        try:
            source_file = open(self.source, 'r')
            source = source_file.read()
            destination_file = open(self.destination, 'w')
            destination_file.write(source)
            source_file.close
            destination_file.close
        except FileNotFoundError:
            return print("That is not a file")

copy = Copy('copy_this.txt', 'paste_here.txt')
