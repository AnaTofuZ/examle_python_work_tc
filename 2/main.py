#!/usr/bin/env python3

student_number = int(input('学籍番号(8桁)を入力'))
birthday_year = int(input('和暦を入力'))

# 文字列をlist関数を通すと1文字ずつのリストになって帰ってくる
# intで受け取っていたので一旦strする
student_number_splitted = list(str(student_number))
student_number_sum = 0
for number in student_number_splitted:
    student_number_sum += int(number)

dividable_number_count = 0

# 学籍番号の足した数と和暦の両方で割り切れる数 == 両方をかけた数で割り切れればいい
divisor = student_number_sum * birthday_year

for i in range(1, student_number + 1):
    # if i % student_number_sum == 0 and i % birthday_year: でもok
    if i % divisor == 0:
        dividable_number_count += 1

print('1から{}までに{}と{}の両方で割り切れる数は{}個'.format(
    student_number,
    student_number_sum,
    birthday_year,
    dividable_number_count)
)
