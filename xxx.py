
import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()

# Initial setup and promotion
os.system('clear')
print(' \x1b[38;5;46mFETCHING UNKNOWN....')
os.system('xdg-open ')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx pip install beautifulsoup4')
os.system('xdg-open ')
print('loading Modules ...\n')
os.system('clear')
print(' \x1b[38;5;46mSUCCESSFULY LOGIN....')
os.system('xdg-open ')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import shutil
import time
import urllib.parse

phone_number = "+639632133040"

raw_message = "Avail ako tools mo ya!"

# URL-encode message
prefill_message = urllib.parse.quote(raw_message)

channel_link = f"https://wa.me/{phone_number}?text={prefill_message}"

# approved key 
approved_keys = ["404"]

GREEN = "\033[1;32m"
RESET = "\033[0m"

MAX_ATTEMPTS = 3
COOLDOWN_SECONDS = 8

def clear_screen():
    os.system("clear")

def open_link(url):
    if shutil.which("termux-open-url"):
        subprocess.run(["termux-open-url", url], check=False)
    elif shutil.which("xdg-open"):
        subprocess.run(["xdg-open", url], check=False)
    else:
        subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", url], check=False)

def normalize(s):
    if s is None:
        return ""
    return " ".join(s.split()).lower()

approved_normalized = { normalize(k) for k in approved_keys }

def first_step():
    clear_screen()
    print("â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”")
    print(f"        {GREEN}ðŸŒ€ WELCOME ðŸŒ€{RESET}")
    print("â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\n")
    print(f"{GREEN} YOU CANâ€™T ACCESS! {RESET}\n")

    try:
        if shutil.which("termux-clipboard-set"):
            subprocess.run(["termux-clipboard-set", raw_message], check=False)
            print(f"{GREEN}Message copied to clipboard â€” Ø¢Ù¾ WhatsApp Ù…ÛŒÚº paste Ú©Ø± Ú©Û’ Ø¨Ú¾ÛŒØ¬ Ø³Ú©ØªÛ’ ÛÛŒÚº.{RESET}")
        else:
            print(f"{GREEN}Copy this message manually: {raw_message}{RESET}")
    except Exception:
        print(f"{GREEN}Copy to clipboard failed. Copy manually: {raw_message}{RESET}")

    # Still opens the chat link, as logic was NOT changed
    try:
        open_link(channel_link)
    except:
        pass

