#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    
# Get all names defined in the module
    names = dir(hidden_4)

# Filter out names that start with '__' and print the rest
    for name in names:
        if not name.startswith('__'):
            print("{}".format(name))
