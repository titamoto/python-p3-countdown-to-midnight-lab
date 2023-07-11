import time

def countdown(integer):

    while integer > 0:
        print(f'{integer} SECOND(S)!')
        integer -= 1
    else:
        print('HAPPY NEW YEAR!')


def countdown_with_sleep(integer):
    while integer > 0:
        print(f'{integer} SECOND(S)!')
        integer -= 1
        time.sleep(1)
    else:
        print('HAPPY NEW YEAR!')