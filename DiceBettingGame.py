def rolldice():
    import random
    list=[]
    for i in range(6):
        nu=random.randint(1,6)
        list.append(nu)
    return list

bal=int(input("enter how much money u have to play :"))

while bal>0:
    try:
        bet=int(input("enter the amount you want to bet :"))
        if bet>bal:
            print("bet cannot be placed due to insufficient balance")
        else:
            num=int(input("enter the number you want to bet on :"))
            if num>6:
                print("enter valid number {1-6}")
            else:
                dice=rolldice()
                print(dice)

                if num in dice:
                    c = dice.count(num)
                    print("You won")
                    bal = bal - bet
                    bal =bal+(c*bet)
                    print(f"Your current balance is {bal}")

                else:
                    print("lost")
                    bal = bal - bet
                    print(f"available balance is {bal}")

                play=input("want to play again {y/n}").lower()
                if play!='y':
                    break
    except ValueError:
        print("enter valid numbers only")
print(f"final balance is {bal}")