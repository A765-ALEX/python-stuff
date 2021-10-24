#!/usr/bin/python3
import os;
var = 1;
while var == 1:
    command = str(input("$ "));
    if command == "exit":
        quit()
    elif command == "cd ..":
        os.chdir("../");
    elif command == "cd":
        dir = input("To where? ")
        os.chdir(dir)
    else:
        os.system(command);
