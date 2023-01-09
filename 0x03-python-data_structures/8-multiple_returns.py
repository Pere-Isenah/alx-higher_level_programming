#!/usr/bin/python3

def main():

    multiple_returns()


def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])


if __name__ == "__main__":

    main()
