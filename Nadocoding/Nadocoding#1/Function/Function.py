# 함수에 대해 배워봅시다!

def open_account():
    print("새로운 계좌가 생성되었습니다.")


open_account()


def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money


def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("통장에 잔고가 부족합니다")
        return balance


def withdraw_night(balance, money):  # 저녁에 출금
    commission = 100 # 수수료
    return commission, balance - money - commission

balance = 1500  # 잔액
result = withdraw_night(balance, 1000)
commission, balance = withdraw_night ( balance, 500)
print("수수료 {0}원 이며, 잔액은 {1} 원 입니다.".format(commission, balance))
