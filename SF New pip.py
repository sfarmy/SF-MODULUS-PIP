import subprocess
import sys
import os
import importlib.util
import time


def auto_install(package, upgrade=False):
    command = [sys.executable, "-m", "pip", "install"]
    if upgrade:
        command.append("--upgrade")
    command.append(package)
    subprocess.call(command)

try:
    from colorama import Fore, init
except:
    auto_install("colorama")
    from colorama import Fore, init


try:
    import pyfiglet
except:
    auto_install("pyfiglet")
    import pyfiglet


init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')

banner = pyfiglet.figlet_format("SF MODULES", font="slant")
print(Fore.CYAN + banner)
print(Fore.MAGENTA + "🔥 FINAL SMART INSTALLER 🔥\n")
print(Fore.YELLOW + f"🐍 Python Version ➜ {sys.version.split()[0]}\n")



modules = {
    "telebot": "telebot",
    "telegram": "telegram",
    "stdiomask": "stdiomask",
    "user_agent": "user_agent",
    "instaloader": "instaloader",
    "requests": "requests",
    "rich": "rich",
    "pyfiglet": "pyfiglet",
    "colorama": "colorama",
    "instagrapi": "instagrapi",
    "generate_user_agent": "generate_user_agent",
    "selenium": "selenium",
    "python-cfonts": "cfonts",
    "pycryptodome": "Crypto",
    "pycryptodomex": "Cryptodome",
    "fake_useragent": "fake_useragent",
    "asmix": "asmix",
    "MedoSigner": "MedoSigner",
    "python-telegram-bot": "telegram",
    "pystyle": "pystyle"
}

already_installed = []
newly_installed = []
failed_modules = []

def ensure_installed(package, import_name):

    if importlib.util.find_spec(import_name) is None:
        print(Fore.YELLOW + f"\n[➜] Installing {package}...\n")

        auto_install(package)

        if importlib.util.find_spec(import_name) is None:
            print(Fore.RED + f"[✗] FAILED → {package}\n")
            failed_modules.append(package)
        else:
            print(Fore.GREEN + f"[✓] INSTALLED → {package}\n")
            newly_installed.append(package)
    else:
        print(Fore.GREEN + f"[✓] ALREADY INSTALLED → {package}")
        already_installed.append(package)


print(Fore.BLUE + "════════ CHECKING MODULES ════════\n")

for pkg, imp in modules.items():
    ensure_installed(pkg, imp)
    time.sleep(0.2)



print(Fore.YELLOW + "\n[➜] Ensuring httpx with HTTP2 support...\n")

auto_install("httpx[http2]", upgrade=True)

if importlib.util.find_spec("httpx") is not None:
    print(Fore.GREEN + "[✓] HTTPX with HTTP2 READY\n")
else:
    print(Fore.RED + "[✗] HTTPX HTTP2 INSTALL FAILED\n")
    failed_modules.append("httpx[http2]")


print(Fore.CYAN + "\n════════ FINAL REPORT ════════\n")

print(Fore.GREEN + "✅ ALREADY INSTALLED MODULES:\n")
for mod in already_installed:
    print(Fore.GREEN + f" - {mod}")

print(Fore.CYAN + "\n--------------------------------\n")

print(Fore.YELLOW + "🆕 NEWLY INSTALLED MODULES:\n")
for mod in newly_installed:
    print(Fore.YELLOW + f" - {mod}")

print(Fore.CYAN + "\n--------------------------------\n")

if failed_modules:
    print(Fore.RED + "❌ FAILED MODULES:\n")
    for mod in failed_modules:
        print(Fore.RED + f" - {mod}")
else:
    print(Fore.GREEN + "🎉 ALL MODULES INSTALLED SUCCESSFULLY 🦅")

print(Fore.CYAN + "\n════════ PROGRAM FINISHED ════════\n")
