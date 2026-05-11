import subprocess
import sys
import os
import importlib.util
import time


def auto_install(package, upgrade=False, force=False):

    command = [
        sys.executable,
        "-m",
        "pip",
        "install",
        "--no-cache-dir"
    ]

    if upgrade:
        command.append("--upgrade")

    if force:
        command.append("--force-reinstall")

    command.append(package)

    try:
        subprocess.check_call(command)
        return True

    except:
        return False


def install_with_retry(package, import_name, retries=2):

    for i in range(retries):

        print(f"🔁 Retry {i+1} for {package}...")

        if auto_install(package, force=True):

            if importlib.util.find_spec(import_name):
                return True

    return False


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

print(Fore.MAGENTA + "🔥 FINAL SMART INSTALLER PRO 🔥\n")

print(Fore.YELLOW + f"🐍 Python ➜ {sys.version.split()[0]}\n")


modules = {

    "pyTelegramBotAPI": "telebot",
    "python-telegram-bot": "telegram",

    "python-cfonts": "cfonts",
    "pyfiglet": "pyfiglet",
    "colorama": "colorama",
    "pystyle": "pystyle",

    "requests": "requests",
    "aiohttp": "aiohttp",
    "selenium": "selenium",
    "beautifulsoup4": "bs4",
    "pysocks": "socks",
    "curl2pyreqs": "curl2pyreqs",

    "user_agent": "user_agent",
    "fake_useragent": "fake_useragent",

    "pycryptodome==3.19.0": "Crypto",
    "pycryptodomex==3.19.0": "Cryptodome",
    "brotli": "brotli",

    "youtube_dl": "youtube_dl",
    "pafy": "pafy",

    "Faker": "faker",
    "rich": "rich",
    "stdiomask": "stdiomask",
    "asmix": "asmix",
    "MedoSigner": "MedoSigner",
    "Topython": "Topython",
    "instaloader": "instaloader",
}


already_installed = []

newly_installed = []

failed_modules = []


def ensure_installed(package, import_name):

    if importlib.util.find_spec(import_name) is None:

        print(Fore.YELLOW + f"\n[➜] Installing {package}...\n")

        success = auto_install(package)

        if not success or importlib.util.find_spec(import_name) is None:

            print(Fore.RED + f"[!] Retrying {package} with force...\n")

            success = install_with_retry(package, import_name)

        if success:

            print(Fore.GREEN + f"[✓] INSTALLED → {package}\n")

            newly_installed.append(package)

        else:

            print(Fore.RED + f"[✗] FAILED → {package}\n")

            failed_modules.append(package)

    else:

        print(Fore.GREEN + f"[✓] ALREADY INSTALLED → {package}")

        already_installed.append(package)


print(Fore.BLUE + "════════ CHECKING MODULES ════════\n")


for pkg, imp in modules.items():

    ensure_installed(pkg, imp)

    time.sleep(0.1)


print(Fore.YELLOW + "\n[➜] Ensuring httpx HTTP2...\n")

auto_install("httpx[http2]", upgrade=True)


print(Fore.CYAN + "\n════════ FINAL REPORT ════════\n")


print(Fore.GREEN + "✅ ALREADY INSTALLED:\n")

for mod in already_installed:
    print(" -", mod)


print("\n🆕 NEWLY INSTALLED:\n")

for mod in newly_installed:
    print(" -", mod)


print("\n❌ FAILED MODULES:\n")

for mod in failed_modules:
    print(" -", mod)


print(Fore.CYAN + "\n════════ PROGRAM FINISHED ════════\n")