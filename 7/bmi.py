#!/usr/bin/env python3

ONE_METER = 100


def cm_to_m(cm):
    return cm/ONE_METER


def compute_bmi(height_cm, weight):
    height = cm_to_m(height_cm)  # BMIはメートルで計算する
    return weight/height**2


def fatness_judge(name, bmi):
    print('{}さん、あなたのBMIは{}でした'.format(name, bmi))
    msg = ''
    if bmi < 18.5:
        msg = 'やせとる'
    elif bmi < 25.0:
        msg = 'ふつうです'
    elif bmi < 30.0:
        msg = '予備軍'
    else:
        msg = '肥満です'
    print('[分類] {}'.format(msg))


def main():
    name = input('氏名を入力 ')
    height = float(input('身長[cm]を入力 '))
    weight = float(input('体重を入力 '))

    fatness_judge(name, compute_bmi(height, weight))


if __name__ == "__main__":
    main()
