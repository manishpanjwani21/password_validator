#!/usr/bin/env python

'''
NIST recently updates their Digital Identity Guidelines in June 2017. 
The new guidelines specify general rules for handling the security of user supplied passwords. 
Previously passwords were suggested to have certain composition rules (special characters, numbers, etc), hints and expiration times. 
Those have gone out the window and the new suggestions are as follows: Passwords MUST

Have an 8 character minimum
AT LEAST 64 character maximum
Allow all ASCII characters and spaces (unicode optional)
Not be a common password

Project
We'd like you to build a program to detect if a password meets these requirements. 
Use a 64 character maximum and allow only ASCII characters. 
As for checking if the password is common, the program should take a file of newline delimited common passwords 
and efficiently check if a password is in that file. 
Of course leverage appropriate data structures, but try to be efficient in your resource usage. 
Use this Common Password List to develop with, but the program should be able to be supplied with any newline delimited file. 
The program should accept passwords from STDIN in newline delimited format and print invalid passwords to the command line. 
An example usage would look like the following: (asterixes used to print unprintable chars)

cat input_passwords.txt | ./password_validator weak_password_list.txt
mom -> Error: Too Short
password1 -> Error: Too Common
*** -> Error: Invalid Charaters
Feel free to use any language, libraries or tools, with a preference towards Python and Go. 
Treat this project as if it was an open source utility that you were going to distribute. 
Things like writing tests, a README with what it does, how to use it and how to build it locally.
'''
import sys
import string

# Password Check Function
def password_check(passwd,filedata): 
    val = True
    
    if not str(passwd).isascii():
        print(f'{passwd} --> Error: Invalid Characters')
        val = False
    elif len(passwd) < minNumberChar: 
        print(f'{passwd} --> Error: Too Short') 
        val = False
    elif len(passwd) > maxNumberChar: 
        print(f'{passwd} --> Error: Too Long') 
        val = False
    elif filedata.find(passwd) !=  -1:
        print(f'{passwd} --> Error: Common Password')
        val = False
    else:
        val = True
    
    if val: 

        return val 

# Added as per requirement for minimum and maximum char
minNumberChar = 8
maxNumberChar = 64   

# Main method 
def main():
    data = list(i.strip() for i in sys.stdin.readlines())

    if len(sys.argv) < 2:
        print(f'Please input the common password file, Paramaters are -- {sys.argv}') 
        exit(1)
    else:
        try:
            with open(sys.argv[1]) as filetext:
                filedata = filetext.read()
                for passwd in data:
                    password_check(passwd,filedata) 
        except IOError:
            print(f'unable to open the file/Password Validation function failed, Paramaters are -- {sys.argv}')
            exit(1)

# Calling Main Function         
if __name__ == '__main__': 
    main() 