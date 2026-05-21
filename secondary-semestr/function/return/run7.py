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
    time.sleep(0.2)
#import time
#import os
#
## Qizil rang (ANSI)
#RED = "\033[91m"
#RESET = "\033[0m"
#
#TEXT = "I LOVE YOU "
#
## Terminalni tozalash
#def clear():
#    os.system("cls" if os.name == "nt" else "clear")
#
## Yurak tenglamasi (klassik)
#def inside_heart(x, y):
#    # (x^2 + y^2 - 1)^3 - x^2*y^3 <= 0
#    f = (x*x + y*y - 1)
#    return (f*f*f - x*x*(y*y*y)) <= 0
#
#def render_frame(angle, scale, width=80, height=32):
#    # Grid o'lchamlari
#    # (0,0) markaz deb olinadi
#    out_lines = []
#    t = 0  # text index
#
#    # aspect ratio uchun y ni biroz cho'zamiz
#    for j in range(height):
#        y0 = (j - height/2) / (height/2) * 1.3
#        line = []
#
#        for i in range(width):
#            x0 = (i - width/2) / (width/2) * 1.8
#
#            # rotation
#            xr = x0 * math.cos(angle) - y0 * math.sin(angle)
#            yr = x0 * math.sin(angle) + y0 * math.cos(angle)
#
#            # puls (scale)
#            xr /= scale
#            yr /= scale
#
#            if inside_heart(xr, yr):
#                ch = TEXT[t % len(TEXT)]
#                t += 1
#                line.append(f"{RED}{ch}{RESET}")
#            else:
#                line.append(" ")
#
#        out_lines.append("".join(line))
#
#    return "\n".join(out_lines)
#
#def animate():
#    angle = 0.0
#    base_scale = 1.0
#
#    while True:
#        # puls: 0.85 - 1.15 oralig'ida uradi
#        scale = base_scale + 0.18 * math.sin(time.time() * 3.5)
#
#        clear()
#        print(render_frame(angle=angle, scale=scale))
#
#        # rotation tezligi
#        angle += 0.08
#        time.sleep(0.05)
#
#if __name__ == "__main__":
#    animate()