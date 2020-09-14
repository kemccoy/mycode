#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
#print(proto)
#print(proto[1])
#proto.extend("dns") # this line will add d, n and s
#print(proto)
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)
http_count = proto.count('http') # Number of times 'http' is found in the protocol names. BUT IT NEVER FINDS MORE THAN 1 !!!!
print('The total number of web protocols present are: ', http_count) # print the number found (CURRENTLY ONLY FINDS 1)
