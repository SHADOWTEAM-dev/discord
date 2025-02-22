from rich.console import Console
from rich.text import Text
from rich.panel import Panel
import os
import time
import requests
import subprocess

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

import requests
from rich.console import Console

def login_with_token(token):
    url = "https://discord.com/api/v9/users/@me"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        console.print("[bold green]Login Successful! The token is valid.[/]")
        get_token_info(token)  # Token bilgilerini göster
    else:
        console.print(f"[bold red]Invalid token! Status Code: {response.status_code}[/]")


console = Console()

# Badge değerleri
BADGE_INFO = {
    1 << 0: ("🏅 Discord Staff", "good"),
    1 << 1: ("💠 Partnered Server Owner", "good"),
    1 << 2: ("📢 HypeSquad Events", "good"),
    1 << 3: ("🐛 Bug Hunter Level 1", "good"),
    1 << 6: ("🏅 HypeSquad Bravery", "bad"),
    1 << 7: ("🏅 HypeSquad Brilliance", "bad"),
    1 << 8: ("🏅 HypeSquad Balance", "bad"),
    1 << 9: ("💎 Early Supporter", "good"),
    1 << 10: ("🛠️ Verified Bot Developer", "good"),
    1 << 14: ("🛡️ Discord Certified Moderator", "good"),
    1 << 17: ("⚙️ Active Developer", "good"),
}

def get_user_badges(flags):
    """Kullanıcının badge'lerini iyi, kötü ve nötr olarak ayırır."""
    good_badges = []
    bad_badges = []
    neutral_badges = []

    for bit, (name, category) in BADGE_INFO.items():
        if flags & bit:
            if category == "good":
                good_badges.append(name)
            elif category == "bad":
                bad_badges.append(name)
            else:
                neutral_badges.append(name)

    return good_badges, bad_badges, neutral_badges

def get_token_info(token):
    url = "https://discord.com/api/v9/users/@me"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_info = response.json()

        # E-posta maskeleme
        email = user_info.get('email', 'Not available')
        masked_email = email[0] + "****@" + email.split("@")[1] if email != "Not available" else email

        # Telefon numarası maskeleme (Son 4 hane açık)
        phone = user_info.get('phone')
        masked_phone = "Not available"
        if phone:
            masked_phone = "*" * (len(phone) - 4) + phone[-4:]
       
        # Kullanıcı nitro sahibi mi?
        premium_type = user_info.get('premium_type', 0)

        if premium_type == 0:
            nitro_status = "None"
        elif premium_type == 1:
            nitro_status = "Classic"
        elif premium_type == 2:
            nitro_status = "Full Nitro"
        else:
            nitro_status = "Unknown"

        # Badge'leri çek
        public_flags = user_info.get('public_flags', 0)
        good_badges, bad_badges, neutral_badges = get_user_badges(public_flags)

        console.print(f"\n[bold green]Token Info:[/]")
        console.print(f"[bold gray]Username:[/] {user_info['username']}#{user_info['discriminator']}")
        console.print(f"[bold gray]Display Name:[/] {user_info.get('global_name', 'Not set')}")
        console.print(f"[bold gray]ID:[/] {user_info['id']}")
        console.print(f"[bold gray]BIO:[/] {user_info.get('bio') or 'Not set'}")
        console.print(f"[bold gray]Email:[/] {masked_email}")
        console.print(f"[bold gray]Phone:[/] {masked_phone}")
        console.print(f"[bold gray]Nitro Type:[/] {nitro_status}")
        console.print(f"[bold gray]MFA Enabled:[/] {user_info.get('mfa_enabled', False)}")
        console.print(f"[bold gray]Verified:[/] {user_info.get('verified', False)}")


        # Badge gösterimi
        if not (good_badges or bad_badges or neutral_badges):  # Hiç badge yoksa
            console.print("[bold yellow]No badges found.[/]")
        else:
            if good_badges:
                console.print(f"[bold cyan]Good Badges:[/] {', '.join(good_badges)}")
            if bad_badges:
                console.print(f"[bold red]Bad Badges:[/] {', '.join(bad_badges)}")

    else:
        console.print(f"[bold red]Invalid token or failed to fetch data![/] (Status Code: {response.status_code})")



def menu():
    while True:
        clear()

        # ASCII ART
        ascii_art = Text("""
███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗████████╗███████╗ █████╗ ███╗   ███╗
██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║   ██║   █████╗  ███████║██╔████╔██║
╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║   ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝   ██║   ███████╗██║  ██║██║ ╚═╝ ██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
        """, style="blue")

        console.print(ascii_art, justify="center")

        # Menü seçenekleri
        options = [
            "[bold cyan]1[/] - [bold]🔥⬆️ Bomb Account[/]",
            "[bold cyan]2[/] - [bold]🔥 Token Info[/]",
            "[bold cyan]3[/] - [bold]⏳ Login with Token[/]",
            "[bold cyan]4[/] - [bold]⏳ Token Generator[/]",
            "[bold cyan]5[/] - [bold]⏳ Spam Webhook[/]",
            "[bold red]0[/] - [bold]Exit[/]"
        ]

        panel = Panel("\n".join(options),
                      title="[bold red]Select an option[/]",
                      border_style="blue",
                      expand=False)
        console.print(panel, justify="center")

        choice = console.input("[bold green]Enter your choice:[/] ")

        if choice == "1":
            clear()
            console.print("[bold red]Bomb Account Selected[/]")
            console.print("[bold red]It should look like this : https://discord.com/api/v9/channels/XXXXXXXXXXXXXXXXXX/messages[/]")
            url = console.input("[bold green]Enter a channel URL [bold red](User must be on the server!)[bold green] :[/] ")
            mesaj = {
                'content': "**SHADOWTEAM** wanna use the program? : https://github.com/SHADOWTEAM-dev/discord @everyone @here"
            }

            tkn = console.input("[bold green]Enter Token [bold black](Dont know? Check this: https://github.com/piotr-ginal/discord-token-grabber) [bold green]: [/]")
            token = {
                'authorization': tkn
            }
            tekrar_sayisi = int(console.input("[bold green]How many times do you want to send the message? : [/]"))
            for _ in range(tekrar_sayisi):
                response = requests.post(url, headers=token, data=mesaj)
                console.print(f"İstek gönderildi! Durum kodu: {response.status_code}")

        elif choice == "2":
            clear()
            console.print("[bold cyan]Token Info Selected[/]")
            tkn = console.input("[bold green]Enter Token: [/]")
            get_token_info(tkn)

        elif choice == "3":
            clear()
            console.print("[bold cyan]Login with Token Selected[/]")
            token = console.input("[bold green]Enter your Token: [/]")
            login_with_token(token)
        elif choice == "4":
            clear()
            subprocess.run(['python', 'generator.py'])

        elif choice == "0":
            console.print("\n[bold yellow]Çıkış yapılıyor...[/]")
            time.sleep(0.4)
            break

        input("\nDevam etmek için Enter'a bas...")

menu()
