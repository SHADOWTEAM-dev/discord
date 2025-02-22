import random
import string
import os
import time
import requests
import sys
import rich
from rich.console import Console
from colorama import Fore

# Banner and console setup
banner = (Fore.BLUE + """
         ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗████████╗███████╗ █████╗ ███╗   ███╗
         ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
         ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║   ██║   █████╗  ███████║██╔████╔██║
         ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║   ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
         ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝   ██║   ███████╗██║  ██║██║ ╚═╝ ██║
         ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
                 """)

generate = (Fore.BLUE + """
███████╗████████╗     ██████╗ ███████╗███╗   ██╗
██╔════╝╚══██╔══╝    ██╔════╝ ██╔════╝████╗  ██║
███████╗   ██║       ██║  ███╗█████╗  ██╔██╗ ██║
╚════██║   ██║       ██║   ██║██╔══╝  ██║╚██╗██║
███████║   ██║       ╚██████╔╝███████╗██║ ╚████║
╚══════╝   ╚═╝        ╚═════╝ ╚══════╝╚═╝  ╚═══╝
""")

# Spinner function for loading animation
def spinner():
    l = ['|', '/', '-', '\\']
    for i in l + l + l:
        sys.stdout.write('\r' + Fore.YELLOW + i)
        sys.stdout.flush()
        time.sleep(0.2)




count = 0
current_path = os.path.dirname(os.path.realpath(__file__))

# New Menu Code
console = Console()

print(banner)

options = [
    "[bold cyan]1[/] - [bold]🔥⬆️ Token Generator[/]",
    "[bold cyan]2[/] - [bold]🔥⬆️ Token Checker[/]",
    "[bold cyan]3[/] - [bold]🔥Delete Tokens[/]",
    "[bold cyan]4[/] - [bold]✅ Info[/]",
    "[bold red]0[/] - [bold]Exit[/]"
]

# Display the menu
panel = rich.panel.Panel("\n".join(options),
                         title="[bold red]Select an option[/]",
                         border_style="blue",
                         expand=False)
console.print(panel, justify="center")


# User input for menu choice
choice = console.input("[bold green]Enter your choice:[/] ")

# Handle menu actions
if choice == '1':
    print(generate)
    GAmount = int(input("\nAmount to generate: "))
    if GAmount > 999:
        print("Warning! You are generating more than 1000 tokens! This can cause rate limits or account restrictions. Proceed with caution.")
        time.sleep(2)

    while count < GAmount:
        generated_token = "NT" + random.choice(string.ascii_letters) + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21)) + "." + random.choice(string.ascii_letters).upper() + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5)) + "." + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
        with open(f"{current_path}/Generated.txt", "a") as f:
            f.write(generated_token + "\n")
        print(Fore.CYAN + "Token: " + Fore.RESET + generated_token)
        count += 1

    print(Fore.RED + "Tokens generated successfully!")
    print(Fore.WHITE + "Tokens saved in Generated.txt")
    input(Fore.BLUE + "\nPress enter to exit")
    print(Fore.BLUE + "Closing!")
    time.sleep(2)
    sys.exit()

elif choice == '2':
    with open('Generated.txt', 'r') as f:
        for line in f:
            time.sleep(0)
            token = line.rstrip("\n")
            headers = {'Authorization': f'{token}'}
            src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)

            try:
                if src.status_code == 200:
                    print(f'{Fore.BLUE}Invalid token! >{Fore.RESET} ' + token)
                else:
                    print(f'{Fore.LIGHTGREEN_EX}Valid token >{Fore.RESET} ' + token)
            except Exception:
                print(f"{Fore.CYAN}Error, please contact with SHADOWTEAM{Fore.RESET}")

elif choice == '4':
    print(Fore.BLUE + "ST GEN - Made by SHADOWTEAM")
    print(Fore.BLUE + "[Github] SHADOWTEAM")
    print(Fore.BLUE + "[Link] https://github.com/shadowteam")
    input(Fore.BLUE + "\nPress enter to exit")
    os.system("cls")
    print(Fore.BLUE + "Closing!")
    time.sleep(2)
    sys.exit()

elif choice == '3':
    print(Fore.RED + "Deleting Tokens...")
    time.sleep(2)
    if os.path.exists("Generated.txt"):
        os.remove("Generated.txt")
        print(Fore.GREEN + "Tokens deleted successfully.")
    else:
        print(Fore.YELLOW + "No tokens file found to delete.")
    sys.exit()

elif choice == '0':
    print("Exiting...")
    sys.exit()

else:
    print(Fore.RED + "Invalid choice, please try again.")
    sys.exit()
