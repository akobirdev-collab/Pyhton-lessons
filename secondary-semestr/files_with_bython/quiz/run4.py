import time
import sys

RED = "\033[91m"
RESET = "\033[0m"

text = "I LOVE YOU "
t = 0
print()
for y in range(12, -13, -1):
    line = ""
    for x in range(-30, 30):
        fx = x * 0.04
        fy = y * 0.1
        formula = fx**2 + fy**2 - 1

        if formula**3 - (fx**2) * (fy**3) <= 0:
            line += RED + text[t % len(text)] + RESET
            t += 1
        else:
            line += " "

    print(line)
    sys.stdout.flush()
    time.sleep(0.15)