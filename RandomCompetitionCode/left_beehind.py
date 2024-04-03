# Beekeeper Bill is ready to go to the annual beekeeper’s convention with his friends. Bill packed his honey in jars,
# but unfortunately the honey in some of the jars has turned sour. Bill’s friends are mean, and if too much of Bill’s
# honey is sour they will go to the convention without him.
#
# If Bill has more jars of sour honey than sweet, he will be left “beehind”. If Bill has more jars of sweet honey than
# sour he will go to the convention. If Bill has the same number of sweet and sour jars, his friends are undecided.
# Lastly, Bill’s friends are superstitious, if he has exactly 13 jars they will never speak to him again. Bill needs
# new friends.
#
# Input consists of multiple cases, each on its own line. Each case consists of two integers x and y (0=< x,y <= 1000),
# which are the number of sweet and sour jars Bill has, respectively. Input is terminated by a line containing
# two zeros, which should not be processed. There may be up to 15 test cases in the input.
#
# For each case, output one of the following results on its own line (without quotes).
#
#     “Left beehind.”
#
#     “Undecided.”
#
#     “To the convention.”
#
#     “Never speak again.”
#
# If Bill’s friends will never speak to him again, that is most important and should be the only output.

import sys

output = ""
never = False
cases = 0
while True:
    if cases == 15:
        break
    try:
        pots = input("")
        pots = pots.strip()
        sweet, sour = pots.split(" ")
        if int(sweet) == 0 or int(sour) == 0 or int(sweet) <= 1000 or int(sour) <= 1000 or int(sweet) >= 0 or int(
                sour) >= 0:
            break
        if not sweet.isnumeric() or not sour.isnumeric():
            sys.exit(0)
    except ValueError:
        sys.exit(0)
    if int(sweet) + int(sour) == 13:
        output = "Never speak again." + "\n"
        never = True
    elif int(sweet) < int(sour) and never is False:
        output += "Left beehind." + "\n"
    elif int(sweet) > int(sour) and never is False:
        output += "To the convention." + "\n"
    elif int(sweet) == int(sour) and never is False:
        output += "Undecided." + "\n"

print(output)
