#!/usr/bin/env python3

def main():
    show_number = 1
    width = 1
    for i in range(0, 8):
        for _ in range(0, width):
            print(show_number, end='\t')
            show_number += 1
        width += 1
        print('')


if __name__ == "__main__":
    main()
