import time
import pyperclip


def get_delay(x):
    if x <= 15:
        return 65

    if x <= 23:
        return 105

    if x <= 25:
        return 125

    return 0


def get_message(x):
    if x == 6:
        return 'Pop Paint, Villers, and Arcadia!!!'

    if x == 16:
        return 'Mechs build UC & freshen towers'

    if x == 19:
        return 'Pop Sparks!!!'

    if x == 22:
        return 'Flood the place!!!'

    if x == 23:
        return 'Teleport buffs out and back! Wait until 24 Launches for Dragon'

    return ""


#
# Main Loops
#

print("ID Start time:", time.ctime())

wave = 1
while wave < 25:
    print('Round {}'.format(wave) + ' has landed')
    wave = wave + 1

    delay = get_delay(wave)
    message = get_message(wave)

    if len(message) > 0:
        print(message)
        pyperclip.copy(message)

    time.sleep(delay)

# the end
print("ID is over")
