#!/usr/bin/env python3

import subprocess
import sys
import os

version = "1.5.9"

# 🎨 কালার কনফিগারেশন
CYAN_MAIN = "\033[1;36m"   # মেইন টেক্সট কালার
WHITE = "\033[1;37m"       # নম্বর কালার
DIM = "\033[2m"
BOLD = "\033[1m"
RED = "\033[1;31m"
RESET = "\033[0m"

TOOLS = {
    "1": ("Unlock Bootloader", "$PREFIX/bin/miunlock"),
    "2": ("Flash Fastboot ROM", "$PREFIX/bin/miflashf"),
    "3": ("Mi Assistant", "$PREFIX/bin/miasst"),
    "4": ("Firmware Content Extractor", "$PREFIX/bin/mifcetool")
}

try:
    term_width = os.get_terminal_size().columns
except:
    term_width = 80

def get_center(text):
    clean = text.replace(CYAN_MAIN, '').replace(RESET, '').replace(DIM, '').replace(WHITE, '')
    pad = (term_width - len(clean)) // 2
    return ' ' * pad + text

print("\n")
print(get_center(f"{DIM}{'═' * min(term_width, 70)}{RESET}"))

# 🛠️ ওসমান ভাই ব্র্যান্ডিং টাইটেল
title = f"Osman Bhai MiTool v{version}"
box_width = len(title) + 4
print(get_center(f"┏{'━' * (box_width - 2)}┓"))
print(get_center(f"┃  {CYAN_MAIN}Osman Bhai MiTool{RESET} {DIM}v{version}{RESET}  ┃"))
print(get_center(f"┗{'━' * (box_width - 2)}┛"))

print(get_center(f"{DIM}https://t.me/osmanbhaiofficials{RESET}"))
print(get_center(f"{DIM}{'═' * min(term_width, 70)}{RESET}"))
print()

print(f"{CYAN_MAIN}{BOLD}Available Operations:{RESET}\n")

# 📊 অদৃশ্য কালার কোড বাদ দিয়ে নিখুঁত কলাম স্পেসিং লজিক
col_width = 32  # কলামের স্ট্যান্ডার্ড দূরত্ব

# ১ম লাইন সাজানো (Unlock Bootloader এবং Flash Fastboot ROM)
text1_left = f"  [{WHITE}1{RESET}] {CYAN_MAIN}Unlock Bootloader{RESET}"
text1_right = f"[{WHITE}2{RESET}] {CYAN_MAIN}Flash Fastboot ROM{RESET}"
# কালার কোড ছাড়া আসল টেক্সটের দৈর্ঘ্য বের করে স্পেস বসানো
pad1 = " " * (col_width - len("  [1] Unlock Bootloader"))
print(f"{text1_left}{pad1}{text1_right}")

print() # মাঝখানে সুন্দর ফাঁকা স্পেস

# ২য় লাইন সাজানো (Mi Assistant এবং Firmware Extractor)
text2_left = f"  [{WHITE}3{RESET}] {CYAN_MAIN}Mi Assistant{RESET}"
text2_right = f"[{WHITE}4{RESET}] {CYAN_MAIN}Firmware Extractor{RESET}"
pad2 = " " * (col_width - len("  [3] Mi Assistant"))
print(f"{text2_left}{pad2}{text2_right}")

print("\n")
# সেন্টারে [q] Quit অপশন
print(get_center(f"{WHITE}[{RESET}{WHITE}q{RESET}{WHITE}]{RESET} {CYAN_MAIN}Quit{RESET}"))
print()

if len(sys.argv) > 1:
    choice = sys.argv[1].lower()
    print(f"{CYAN_MAIN}►{RESET} {CYAN_MAIN}Selected:{RESET} {WHITE}{choice}{RESET}\n")
else:
    try:
        choice = input(f"{CYAN_MAIN}{BOLD}►{RESET} {CYAN_MAIN}Enter choice:{RESET} ").strip().lower()
    except (KeyboardInterrupt, EOFError):
        print(f"\n\n{CYAN_MAIN}Cancelled{RESET}")
        sys.exit(0)

if choice in ['q', 'quit', 'exit']:
    print(f"{CYAN_MAIN}Exiting...{RESET}\n")
    sys.exit(0)

if choice in TOOLS:
    desc, cmd = TOOLS[choice]
    print(f"\n{CYAN_MAIN}►{RESET} {CYAN_MAIN}Executing:{RESET} {DIM}{cmd}{RESET}\n")
    print(f"{DIM}{'─' * min(term_width, 70)}{RESET}\n")
    subprocess.run(cmd, shell=True)
else:
    print(f"{RED}✗ Invalid:{RESET} '{choice}'")
    print(f"{DIM}Select 1-4 or 'q' to quit{RESET}\n")
    sys.exit(1)