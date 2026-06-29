#!/data/data/com.termux/files/usr/bin/bash

set -e

# 🎨 সম্পূর্ণ সায়ান এবং হোয়াইট কালার কম্বিনেশন
R='\033[1;31m'         # এরর এর জন্য লাল কালার
CYAN_MAIN='\033[1;36m' # আপনার প্রিয় হালকা নীল/সায়ান কালার
I='\033[1;36m'         # লোডিং ডট [..] গুলোও এখন সায়ান দেখাবে
N='\033[0m'            # রিসেট কালার
W='\033[1;37m'         # টেক্সটের জন্য সাদা কালার

run_step() {
    local msg="$1"
    local cmd="$2"

    echo -e "${I}[..]${N} ${CYAN_MAIN}$msg...${N}"

    if eval "$cmd" > /dev/null 2>&1; then
        echo -e "     └─> ${CYAN_MAIN}[SUCCESS]${N}\n"
    else
        echo -e "     └─> ${R}[FAILED]${N}"
        echo -e "${R}Error occurred during: $msg${N}\n"
        exit 1
    fi
}

echo

if [ ! -d "$HOME/storage" ]; then
    echo -e "\nGrant permission: termux-setup-storage\nThen rerun the command.\n"
    exit 1
fi

if ! cmd package list packages --user 0 com.termux.api < /dev/null 2>/dev/null | grep -q 'com.termux.api'; then
    echo
    echo 'com.termux.api app is not installed'
    echo 'Please install it first'
    echo
    exit 1
fi

arch=$(dpkg --print-architecture)

if [[ "$arch" != "aarch64" && "$arch" != "arm" ]]; then
    echo "MiTool does not support architecture $arch"
    exit 1
fi

run_step "Updating System & Fixing Broken Packages" \
"yes | apt --fix-broken install && yes | apt update && yes | apt upgrade"

run_step "Installing Python3" \
"yes | pkg install python3"

run_step "Installing libusb" \
"yes | pkg install libusb"

run_step "Installing pv" \
"yes | pkg install pv"

run_step "Installing termux-adb" \
"curl -fsS https://raw.githubusercontent.com/nohajc/termux-adb/master/install.sh | bash"

run_step "symlink termux-adb/termux-fastboot — adb/fastboot" \
"ln -sf \$PREFIX/bin/termux-fastboot \$PREFIX/bin/fastboot && ln -sf \$PREFIX/bin/termux-adb \$PREFIX/bin/adb"

run_step "Installing colorama" \
"pip install -U colorama"

run_step "Installing miunlock" \
"pip install -U miunlock"

run_step "Installing fcetool" \
"pip install -U fcetool"

# 🛠️ কোটেশন ও ভ্যারিয়েবল এস্কেপিং নিখুঁতভাবে ফিক্সড
run_step "download mitool.py" \
"curl -s https://raw.githubusercontent.com/osmanbhai50505/Osman-Bhai-MiTool/main/MT/mitool.py -o \$PREFIX/bin/mitool && chmod +x \$PREFIX/bin/mitool"

run_step "download miflashf.py" \
"curl -fsS https://raw.githubusercontent.com/osmanbhai50505/Osman-Bhai-MiTool/main/MT/miflashf.py -o \$PREFIX/bin/miflashf && chmod +x \$PREFIX/bin/miflashf"

run_step "download mifcetool.py" \
"curl -fsS https://raw.githubusercontent.com/osmanbhai50505/Osman-Bhai-MiTool/main/MT/mifcetool.py -o \$PREFIX/bin/mifcetool && chmod +x \$PREFIX/bin/mifcetool"

run_step "download miasst.py" \
"curl -fsS https://raw.githubusercontent.com/osmanbhai50505/Osman-Bhai-MiTool/main/MT/miasst.py -o \$PREFIX/bin/miasst && chmod +x \$PREFIX/bin/miasst"

run_step "download miasst_termux" \
"curl -fsS -L -o \$PREFIX/bin/miasst_termux \$(curl -fsS 'https://api.github.com/repos/offici5l/MiAssistantTool/releases/latest' | grep 'browser_download_url.*miasst_termux_'\${arch} | cut -d '\"' -f 4) && chmod +x \$PREFIX/bin/miasst_termux"

# Changelog সেকশন
curl -s -L https://raw.githubusercontent.com/osmanbhai50505/Osman-Bhai-MiTool/main/CHANGELOG.md | tac | awk -v I="$CYAN_MAIN" -v N="$N" '/^#/{exit} {print I $0 N}' | tac

echo -e "${CYAN_MAIN}✔ Installation completed successfully${N}\n"

echo -e "${W}Welcome Owner:${N} ${CYAN_MAIN}OSMAN BHAI${N}"
echo -e "${W}Run command:${N} ${CYAN_MAIN}mitool${N}"
echo ""