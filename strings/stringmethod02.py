#!/usr/bin/env phython3

"""Alta3 Research || Author: RZFeeser@alta3.com"""


def main():
    lilstring = "Alta3 Research offers classes on Python coding"
    newlist = lilstring.split(" ") # this returns a list
    print(newlist)

myiplist = ["192", "168", "0", "12"]
singleip = ".".join(myiplist)

print(singleip)
