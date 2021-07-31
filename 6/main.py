#!/usr/bin/env python3
import random

FIRST_MONEY = 10_000
BET = 1000


# ユーザーの辞書型を作る
def create_user(user_name):
    return {'money': FIRST_MONEY, 'name': user_name}


# userのお金を見てゲームが終わってるかを見る
def is_finish_game(users):
    for user in users:
        if user['money'] <= 0:
            print("{}さんは破産しました".format(user['name']))
            return True
    return False


def get_card():
    return random.randint(1, 12)

# 2人しかいない想定
# 返り値: -1 引き分け, 0か1, 勝った人のindex
def battle(cards):
    if cards[0] == cards[1]:  # 同じ数だったら引き分け
        return -1
    for i in range(len(cards)):  # 1を引いてたら引いた人が勝ち
        if cards[i] == 1:
            return i
    if cards[0] > cards[1]:  # 数が大きい人が勝ち
        return 0
    return 1


# ユーザーのお金を更新する
# win_user_indexで指定されているuserは勝ったuser
def money_upgrade(users, win_user_index):
    for i in range(len(users)):
        if i == win_user_index:  # バトルに勝った人だったらお金を増やす
            users[i]['money'] += BET
            continue
        users[i]['money'] -= BET  # 負けた人ならお金を減らす


def main():
    users = []
    for user_name in ['あなた', 'ディーラー']: 
        users.append(create_user(user_name))
    turn = 0

    while 1:
        turn += 1
        cards = []
        print('{}ターン目 あなたの総資産 {}'.format(turn, users[0]['money']))
        for user in users:
            card = get_card()
            print('{}のカードは{}です'.format(user['name'], card))
            cards.append(card)

        win_user = battle(cards)
        if win_user < 0:  # -1で来ていた場合は引き分け
            print('引き分け\n')
            continue
        print('{}のかち\n'.format(users[win_user]['name']))
        money_upgrade(users, win_user)

        if is_finish_game(users):
            print('ゲーム終了')
            break


if __name__ == "__main__":
    main()
