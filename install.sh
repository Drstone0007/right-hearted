#!/bin/bash
set -e

GREEN='\033[0;32m'
NC='\033[0m'
echo -e "${GREEN}🐐 Right-Hearted Ecosystem v2.0 Installer${NC}"

# 1. System dependencies
echo "📦 Installing system packages..."
sudo apt update && sudo apt install -y python3-pip python3-venv python3-dev \
    nodejs npm git curl docker.io docker-compose-v2 unzip

# 2. Create project directory
mkdir -p ~/right-hearted && cd ~/right-hearted

# 3. Clone the ecoystem (only if the directory is empty)
if [ ! -f "README.md" ]; then
    git clone https://github.com/Drstone0007/right-hearted.git .
fi

# 4. Backend setup
echo "🐍 Setting up Python virtual environment..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 5. Environment variables
if [ ! -f .env ]; then
    cp ../.env.example ../.env
    echo ""
    echo "⚠️  Please edit the .env file with your secrets:"
    echo "   nano ../.env"
    echo ""
    echo "Required variables:"
    echo "   SECRET_KEY          - a long random string"
    echo "   ENCRYPTION_KEY       - output of: python -c \"from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())\""
    echo "   TELEGRAM_BOT_TOKEN   - your bot token from @BotFather (optional)"
    echo ""
    read -p "Press Enter after editing the .env file..."
fi

# 6. Start PostgreSQL & Redis
echo "🐘 Starting databases..."
cd ..
if [ ! -f docker-compose.yml ]; then
    echo "Missing docker-compose.yml – please add it to the project root."
    exit 1
fi
sudo docker compose up -d db redis

# 7. Initialize database
echo "🗄️ Initializing database..."
cd backend
python3 -c "from app import create_app; app = create_app(); app.app_context().push()"

# 8. Start Flask backend
echo "🚀 Starting backend..."
nohup python app.py > app.log 2>&1 &

# 9. TUI setup
echo "💻 Installing TUI dependencies..."
cd ../tui
npm install

# 10. Done
echo ""
echo "✅ Right-Hearted Ecosystem installed successfully!"
echo ""
echo "🌐 Web GUI:   http://localhost:5000"
echo "💻 TUI:       cd ~/right-hearted/tui && node index.js"
echo "🤖 Telegram:  Send /start to your bot (after setting webhook)"
echo ""
echo "📄 Logs:      ~/right-hearted/backend/app.log"
echo ""
echo "🫀 The swarm is ready. Nubia awaits your command."
