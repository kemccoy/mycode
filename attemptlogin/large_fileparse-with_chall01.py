#!/usr/bin/python3

# parse keystone.common.wsgi and return number of successful login attempts
loginpass = 0 # counter for pass

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'success pattern' appears in the line...
        if "Loaded 2 encryption keys (max_active_keys=3)" in line:
            loginpass += 1
print("The number of successful logins is ", loginpass)
