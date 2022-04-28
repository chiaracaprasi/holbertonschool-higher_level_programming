#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4

    directory = dir(hidden_4)

    for file in directory:
        if file[:2] != "__":
            print(file)
