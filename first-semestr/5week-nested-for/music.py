
import time
import itertools


lines = [
    
    
    "Can you remember and humanize? 🤔❤️",
    "It was still where we'd energized ⚡️",
    "Lie in the sand and visualize 🏖️✨",
    "Like it's seventy five again 🌅",
     "",
    "We are the people that rule the world 🌍👑",
    "A force running in every boy and girl 👦👧🔥",
    "All rejoicing in the world 🎉🌎",

    "",
    "I can't do well when I think 😣💭",
    "You're gonna leave me, but I know I try 💔💪",
    "Are you gonna leave me now? ❓😕",
    "Can't you be believing now? 🙏✨",

     "",
    "I can't do well when I think 😣💭",
    "You're gonna leave me, but I know I try 💔💪",
    "Are you gonna leave me now? ❓😕",
    "Can't you be believing now? 🙏✨",
    "",
    "I know everything about you😉🔥",
    "You know everything about me🤝",
    "Know everything about us💞",

    "",
    "I know everything about you👀✨",
    "You know everything about me🔐💭",
    "Know everything about us💙",
]


RESET = "\033[0m"
COLORS = [
    "\033[38;5;45m",   
    "\033[38;5;51m",
    "\033[38;5;87m",
    "\033[38;5;123m",
    "\033[38;5;159m",
    "\033[38;5;195m",  
    "\033[38;5;219m",  
    "\033[38;5;183m",
]


CHAR_DELAY = 0.045  
LINE_PAUSE = 1.0   
PUNCT_PAUSE = 0.25   

def print_lyrics_colored(lines):
    color_cycle = itertools.cycle(COLORS)
    for line in lines:
        color = next(color_cycle)
        
        for ch in line:
           
            extra = PUNCT_PAUSE if ch in ",.?!" else 0
            print(f"{color}{ch}{RESET}", end="", flush=True)
            time.sleep(CHAR_DELAY + extra)
        print()  
        time.sleep(LINE_PAUSE)

if __name__ == "__main__":
    print_lyrics_colored(lines)
