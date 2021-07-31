#!/usr/bin/env python3


def main():
    width = 1
    for i in range(1, 8 + 1):
        is_circle = first_position_is_circle(i)  # 奇数だったらo、偶数ならx
        for _ in range(0, width):
            print(circle_or_cross(is_circle), end='\t')
            is_circle = not is_circle  # 右隣はoが来てたらxになる
        width += 1
        print('')


def circle_or_cross(is_circle):
    if is_circle:
        return 'o'
    return 'x'


# 奇数だったらo、偶数ならx
# oのときはis_circleがTrueなので、奇数だったらTrueを返す
def first_position_is_circle(width):
    return width % 2 != 0


if __name__ == "__main__":
    main()
