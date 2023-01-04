#!/usr/bin/python3
def uppercase(str):
    for x in str:
        x = ord(x)
        if x in range(ord("a"), ord("z")+1):
            x = x-32 
        print(chr(x) , end = "")
    print("\n")
