import os
from os import name as os_name, system
import subprocess

try:
    import discord
    import random
    from time import sleep
    import time
    import json
    from discord.ext import commands
    import threading
    import shutil
    from discord.utils import get
    import asyncio
    from datetime import date
    from datetime import datetime
    from discord.ui import Button, View
    from discord.ui import Select
    from colorama import init, Fore as cc
    import importlib
    import sys
except:
    cwd = os.path.abspath(__file__)
    #print(os.path.getcwd())
    os.chdir(cwd[:-11])
    subprocess.call(['python', 'setup.py'])
    print(f"\n")
    exit()


today = date.today()
now = datetime.now()

timenow = now.strftime("%H:%M:%S")

init()
clear = lambda: system('cls') if os_name == 'nt' else system('clear')
#colorama variables
dr = DR = r = R = cc.LIGHTRED_EX
g = G = cc.LIGHTGREEN_EX
b = B = cc.LIGHTBLUE_EX
m = M = cc.LIGHTMAGENTA_EX
c = C = cc.LIGHTCYAN_EX
y = Y = cc.LIGHTYELLOW_EX
w = W = cc.RESET

intents = discord.Intents.all()

hformat = f'''
   CUSTOM DISCORD.PY BOT MODULE
----------------------------------
Author : Xal Val Sef'Koj Komtaree
Date Created : NOV18.2022
----------------------------------
Commandline Arguments:

help               [to show this message]
packages           [to show what packages this module imports]
prefix   <prefix>  [Change Prefix]
'''


for arg in sys.argv:
    arg = arg.lower()
    if arg == "help":
        print(hformat)
        exit()
    if arg == "packages":
        modulenames = set(sys.modules) & set(globals())
        for name in modulenames:
            print(f"\n{name}")
        print("\n\n Some Packages May Not Be Listed, example: from XYZ import ZYX  will not be listed.")
        exit()
    if arg == "prefix":
        ind = sys.argv.index(arg)
        pref = sys.argv[ind+1]
        pref = pref.encode("utf-8")
        with open("prefix.pref", "wb") as f:
            f.write(pref)
            f.close()
        print(f"Prefix Saved Successfully, Run this command again later to change it!\nPrefix is :: {pref.decode('utf-8')}")
        exit()

try:
    with open('prefix.pref', "rb") as f:
        prefix = f.read()
        f.close()
    prefix = prefix.decode("utf-8")
except:
    print(f"{r}ERR Please Set a Prefix!\n{w}Example :: main.py prefix !\n")
try:
    print(f"Prefix is {prefix}")
    client = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents)
except:
    print(f"{r}ERR If 'prefix.pref' doesnt exist in the current project working directory, please set a prefix! (check help)\n\nIf a prefix is set then please ensure Privileged Intents are enabled via developer portal for your project.\n")
    exit()
client.remove_command('help')
print(f"Using unofficial 'bot' package for discord, V1.0\nfor help (example) type: 'main.py help'")