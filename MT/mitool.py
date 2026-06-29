#!/usr/bin/env python3

import subprocess
import sys
import os

version = "1.0.1"

# 🎨 সম্পূর্ণ কাস্টমাইজড সায়ান থিম কালার কনফিগারেশন
CYAN_MAIN = "\033[1;36m"   # মেইন টেক্সট, বর্ডার ও লিংকের সায়ান কালার
WHITE = "\033[1;37m"       # নম্বর ও ব্র্যাকেটের জন্য পরিষ্কার সাদা কালার
BOLD = "\033[1m"           # টেক্সট মোটা করার জন্য
RED = "\033[1;31m"         # এরর মেসেজের জন্য লাল কালার
RESET = "\033[0m"          # কালার রিসেট করার জন্য

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
    # কালার কোড ছাড়া শুধু টেক্সটের সঠিক দৈর্ঘ্য মেপে সেন্টারিং করার ফাংশন
    clean = text.replace(CYAN_MAIN, '').replace(RESET, '').replace(WHITE, '')
    pad = (term_width - len(clean)) // 2
    return ' ' * pad + text

print("\n")
# বর্ডার লাইন সম্পূর্ণ সায়ান কালার করা হলো
print(get_center(f"{CYAN_MAIN}{'═' * min(term_width, 70)}{RESET}"))

# 🛠️ ওসমান ভাই ব্র্যান্ডিং টাইটেল বক্স
title = f"Osman Bhai MiTool v{version}"
box_width = len(title) + 4
print(get_center(f"{CYAN_MAIN}┏{'━' * (box_width - 2)}┓{RESET}"))
print(get_center(f"{CYAN_MAIN}┃  Osman Bhai MiTool{RESET} {WHITE}v{version}{RESET}{CYAN_MAIN}  ┃{RESET}"))
print(get_center(f"{CYAN_MAIN}┗{'━' * (box_width - 2)}┛{RESET}"))

# টেলিগ্রাম লিংকও এখন সায়ান কালারে জ্বলজ্বল করবে
print(get_center(f"{CYAN_MAIN}https://t.me/osmanbhaiofficials{RESET}"))
print(get_center(f"{CYAN_MAIN}{'═' * min(term_width, 70)}{RESET}"))
print()

print(f"{CYAN_MAIN}{BOLD}Available Operations:{RESET}\n")

# 📊 ২ কলামের নিখুঁত স্পেসিং লজিক (যাতে কাছাকাছি লেগে না যায়)
col_width = 32  

# ১ম লাইন সাজানো (Unlock Bootloader এবং Flash Fastboot ROM)
text1_left = f"  [{WHITE}1{RESET}] {CYAN_MAIN}Unlock Bootloader{RESET}"
text1_right = f"[{WHITE}2{RESET}] {CYAN_MAIN}Flash Fastboot ROM{RESET}"
pad1 = " " * (col_width - len("  [1] Unlock Bootloader"))
print(f"{text1_left}{pad1}{text1_right}")

print() # কলামগুলোর মাঝে সুন্দর ১ লাইনের ফাঁকা স্পেস

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
    # কমান্ড রান করার সময়কার মেসেজ ও নিচের ডিভাইডার লাইন সায়ান করা হলো
    print(f"\n{CYAN_MAIN}►{RESET} {CYAN_MAIN}Executing:{RESET} {WHITE}{cmd}{RESET}\n")
    print(f"{CYAN_MAIN}{'─' * min(term_width, 70)}{RESET}\n")
    subprocess.run(cmd, shell=True)
else:
    print(f"{RED}✗ Invalid:{RESET} '{choice}'")
    print(f"{CYAN_MAIN}Select 1-4 or 'q' to quit{RESET}\n")
    sys.exit(1)