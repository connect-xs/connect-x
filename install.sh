#!/bin/bash

# Content-x Installer Script
# For Ubuntu/Debian VPS

set -e

GREEN="\033[1;32m"
CYAN="\033[1;36m"
RESET="\033[0m"

function info() {
    echo -e "${CYAN}➡ $1${RESET}"
    sleep 1
}

function print_banner() {
    echo -e "${GREEN}"
    echo " ██████╗ ██████╗ ███╗   ██╗████████╗███████╗███╗   ██╗████████╗"
    echo "██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔════╝████╗  ██║╚══██╔══╝"
    echo "██║     ██║   ██║██╔██╗ ██║   ██║   █████╗  ██╔██╗ ██║   ██║   "
    echo "██║     ██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██║╚██╗██║   ██║   "
    echo "╚██████╗╚██████╔╝██║ ╚████║   ██║   ███████╗██║ ╚████║   ██║   "
    echo " ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝   ╚═╝   "
    echo -e "        ${CYAN}⚡Full HD Content-x Video Uploader ⚡${RESET}"
    echo
    sleep 2
}

clear
print_banner

info "📦 Updating system packages..."
sudo apt update -y && sudo apt upgrade -y

info "🐍 Installing Python, pip, and dependencies..."
sudo apt install -y python3 python3-pip ffmpeg git lolcat pv

info "📂 Cloning Content-x repo..."
if [ ! -d "Content-x" ]; then
    git clone https://github.com/RTXFORCE-X/Content-x.git | lolcat
fi
cd Content-x

info "📁 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

info "📄 Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt | lolcat

info "✅ Setup complete!"
echo "--------------------------------------------" | lolcat
cat <<EOF | lolcat
🎉 NEXT STEPS:

1. ⚙️ Configure your .env file:
   - Copy the template: cp .env.example .env
   - Edit it with your credentials.

2. ▶️ Run:
   source venv/bin/activate
   python contentx.py links.txt

3. 📲 First time will ask Telegram login.

Happy Uploading! 🚀
EOF
echo "--------------------------------------------" | lolcat
