from time import sleep
from rich.console import Console

console = Console()

# Qo‘shiq matni
lines = [
    "I wanna be your slave, I wanna be your master",
    "I wanna make your heartbeat run like rollercoasters",
    "I wanna be a good boy, I wanna be a gangster",
    "'Cause you could be the beauty and I could be the monster",
    "I love you since this morning, not just for aesthetic",
    "I wanna touch your body, so fucking electric",
    "I know you're scared of me, you say that I'm too eccentric",
    "I'm crying all my tears and that's fucking pathetic",
    "I wanna make you hungry, then I wanna feed ya",
    "I wanna paint your face like you're my Mona Lisa",
    "I wanna be a champion, I wanna be a loser",
    "I'll even be a clown 'cause I just wanna amuse ya",
]

delay = 2  # soniyalar orasidagi kechikish

try:
    for i, line in enumerate(lines, start=1):
        # Har bir satrni rangli chiqarish
        if i % 2 == 0:
            console.print(f"[bold cyan]{line}[/bold cyan]")
        else:
            console.print(f"[bold magenta]{line}[/bold magenta]")
        sleep(delay)

    console.print("\n[bold green]Tugadi ✅[/bold green]")

except KeyboardInterrupt:
    console.print("\n[bold yellow]To‘xtatildi (Ctrl+C).[/bold yellow]")
