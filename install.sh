#!/data/data/com.termux/files/usr/bin/bash

set -e

# 🎨 সায়ান এবং হোয়াইট কালার কম্বিনেশন
R='\033[1;31m'         # এরর (লাল)
CYAN_MAIN='\033[1;36m' # সায়ান কালার
G='\033[1;32m'         # সাকসেস (সবুজ)
N='\033[0m'            # রিসেট কালার
W='\033[1;37m'         # টেক্সট (সাদা)

TOTAL_STEPS=7
STEP=0

run_step() {
    STEP=$((STEP + 1))
    local msg="$1" cmd="$2" output

    printf "${CYAN_MAIN}[%d/%d] %s...${N} " "$STEP" "$TOTAL_STEPS" "$msg"

    if output=$(bash -c "$cmd" 2>&1); then
        echo -e "${G}✔${N}"
    else
        echo -e "${R}✘${N}"
        echo -e "${R}Error occurred during: $msg${N}"
        echo "$output"
        exit 1
    fi
}

echo

arch=$(dpkg --print-architecture)
if [[ "$arch" != "aarch64" && "$arch" != "arm" ]]; then
    echo -e "${R}MiTool does not support architecture $arch${N}"
    exit 1
fi

if [ ! -d "$HOME/storage" ]; then
    echo -e "\n${R}Grant permission: termux-setup-storage${N}\nThen rerun the command.\n"
    exit 1
fi

if ! cmd package list packages --user 0 com.termux.api < /dev/null 2>/dev/null | grep -q 'com.termux.api'; then
    echo -e "\n${R}com.termux.api app is not installed${N}\nPlease install it first\n"
    exit 1
fi

run_step "Updating system & fixing broken packages" \
    "yes | apt --fix-broken install && yes | apt update && yes | apt upgrade"

run_step "Installing Python3" \
    "yes | pkg install python3 -y"

run_step "Installing python-pip" \
    "yes | pkg install python-pip -y"

run_step "Installing libusb" \
    "yes | pkg install libusb -y"

run_step "Installing termux-api" \
    "yes | pkg install termux-api -y"

run_step "Installing termux-adb" \
    "curl -fsS https://raw.githubusercontent.com/nohajc/termux-adb/master/install.sh | bash && ln -sf \$PREFIX/bin/termux-fastboot \$PREFIX/bin/fastboot && ln -sf \$PREFIX/bin/termux-adb \$PREFIX/bin/adb"

# 🛠️ সংশোধন: আপনার গিটহাবের নতুন কোড ইনস্টল করবে
run_step "Installing Osman Bhai MiTool" \
    "pip install git+https://github.com/osmanbhai50505/Osman-Bhai-MiTool.git --force-reinstall --break-system-packages"

# Changelog ডিসপ্লে
curl -s -L https://raw.githubusercontent.com/osmanbhai50505/Osman-Bhai-MiTool/main/CHANGELOG.md | tac | awk -v I="$CYAN_MAIN" -v N="$N" '/^#/{exit} {print I $0 N}' | tac 2>/dev/null || true

echo -e "\n${CYAN_MAIN}✔ Installation completed successfully${N}"
echo -e "${W}Welcome Owner:${N} ${CYAN_MAIN}OSMAN BHAI${N}"
echo -e "${W}Run command:${N} ${CYAN_MAIN}mitool${N}\n"
