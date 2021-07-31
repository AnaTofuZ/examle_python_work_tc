#!/usr/bin/env python3


def main():
    is_circle = True
    width = 1
    for i in range(0, 8):
        is_first_number_circle = is_circle
        for _ in range(0, width):
            print(circle_or_cross(is_circle), end='\t')
            is_circle = not is_circle  # 右隣はoが来てたらxになる
        width += 1
        is_circle = not is_first_number_circle  # 各行の最初のoxは、直前の行の先頭と逆
        print('')


def circle_or_cross(is_circle):
    if is_circle:
        return 'o'
    return 'x'


if __name__ == "__main__":
    main()
