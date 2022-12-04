import random
import time
sum=0
sum2=0


def usrplay():
    global sum
    while True:
        computer_hand = random.randint(1, 6)
        while True:
            user_hand = int(input('\nEnter digit (1-6)'))
            if user_hand in [1, 2, 3, 4, 5, 6]:
                break
            else:
                print('Enter correct number\n')
                continue
        print('Computer:', computer_hand)
        if computer_hand != user_hand:
            sum += user_hand
        elif computer_hand == user_hand:
            print('You are OUT !!!\n')
            time.sleep(1)
            break



def compplay():
    global sum2
    while True:
        computer_hand = random.randint(1, 6)
        user_hand = int(input('\nEnter digit (1-6)'))
        print('Computer:', computer_hand)
        if computer_hand != user_hand:
            sum2 += computer_hand
        elif computer_hand == user_hand:
            print('Computer is OUT !!!\n')
            time.sleep(1)
            break


def play():
    global sum
    global sum2
    if toss == toss_crosscheck:
        if bat_or_ball == 'bat':
            print(('!!!Your Batting!!!'))
            usrplay()
            print('Your score:', sum);time.sleep(1)
            print('!!!Your Bowling!!!')
            compplay()
            print('Computer\'s score is', sum2);time.sleep(1)
        elif bat_or_ball == 'ball':
            print('!!!Your Bowling!!!')
            compplay()
            print('Computer\'s score is', sum2);time.sleep(1)
            print(('!!!Your Batting!!!'))
            usrplay()
            print('Your score:', sum);time.sleep(1)

    else:
        if bat_or_ball == 'bat':
            print('!!!Your Bowling!!!')
            compplay()
            print('Computer\'s score is', sum2);time.sleep(1)
            print(('!!!Your Batting!!!'))
            usrplay()
            print('Your score:', sum);time.sleep(1)
        elif bat_or_ball == 'ball':
            print(('!!!Your Batting!!!'))
            usrplay()
            print('Your score:', sum);time.sleep(1)
            print('!!!Your Bowling!!!')
            compplay()
            print('Computer\'s score is', sum2);time.sleep(1)

print()
print('#'*50,'\nWELCOME TO HAND CRICKET - COMPUTER vs USER','\n'+'#'*50)
time.sleep(1)
while True:
    # Choosing even or odd
    print(('choose odd/even (o/e)'))
    toss = input(('>>>'))
    if toss == 'o':
        toss = 'odd'
        break
    elif toss == 'e':
        toss = 'even'
        break
    else:
        print('chose correct option')
        continue
    print('You have chosen',toss,'\n')
while True:
    # Tossing takes place here
    print('Enter a digit to toss (1-6)')
    user_num = int(input('>>>'))
    if user_num in [1,2,3,4,5,6]:
        break
    else:
        print('Enter correct number\n')

computer_num = random.randint(1,6)
toss_sum = user_num +computer_num
print('Computer selected',computer_num )
time.sleep(1)
print('deciding toss...\n')
time.sleep(2)
print('\nSum of choises is',toss_sum)
toss_crosscheck = ''
if toss_sum%2 == 0:
    toss_crosscheck = 'e'
else:
    toss_crosscheck = 'o'

if toss == toss_crosscheck :
    print('You won the toss!!!\nChoose batting or bowling(bat/ball)')
    bat_or_ball = input('>>>')
    while True:
        if bat_or_ball == 'bat' or bat_or_ball == 'ball':
            break
        else:
            print('!!!enter either bat or ball')
            continue
    print('You chose', bat_or_ball + 'ing')
    play()
else:
    print('Computer won the toss!!!')
    bat_or_ball = random.choice(['bat', 'ball'])
    if bat_or_ball == 'bat':
        print('Computer hast chosen to bat')
    else:
        print('Computer has chosen to bowl')
    play()

final = None
if sum > sum2:
    print('\n!!YOU WON THE GAME!! by',sum-sum2,'runs!!')
elif sum2 > sum:
    print('\nComputer won the game!! by',sum2-sum,'runs!!')
    print('Better luck next time!')
elif sum==sum2:
    print('GAME IS TIED at score',sum)

