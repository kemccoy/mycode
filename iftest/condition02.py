#!/usr/bin/enc python3

hostname = input("What value should we set for hostname?")
## Notice how the next line changed
## here we use the str.lower() method to return lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("Hostname matches expected config") # This will add the correct text
    print("  ") # This will create a blank space before the next line
    print("Exiting the script") # This will print "exiting the script" before exiting
