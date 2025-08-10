# 🔐 Lox - CLI Password Manager

A secure, multi-user command-line password manager that keeps your passwords safe locally.

## ✨ Features

- **🔒 Military-grade encryption** - AES-128 with bcrypt hashing
- **👥 Multi-user support** - Separate vaults for different users
- **⏰ Auto-lock** - Sessions lock after 60 seconds of inactivity
- **📋 Smart clipboard** - Auto-clears passwords after 20 seconds
- **🛡️ Recovery system** - Never lose access with recovery tokens
- **🖥️ Cross-platform** - Works on Windows, macOS, and Linux

## 🚀 Quick Start

**Coming soon to PyPI!** For now, clone and run locally:

```bash
git clone https://github.com/adchad90/Lox.git
cd Lox
python -m venv venv
# Activate virtual environment:
# Linux/Mac: source venv/bin/activate
# Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m Lox.main
```

## 📖 Usage

### First Time Setup
1. Clone and set up the project (see Quick Start above)
2. Run `python -m Lox.main`
3. Create a new user
4. Set a master password
5. **IMPORTANT:** Save the recovery token somewhere safe offline!

### Daily Use
1. Activate your virtual environment
2. Run `python -m Lox.main`
3. Login with your master password
4. Manage your passwords securely

## 🔧 Commands

Once running, use these options:
- `1` - Get Password (copies to clipboard)
- `2` - Create/Update Password
- `3` - Delete Entry  
- `4` - List All Entries
- `5` - Change Master Password
- `6` - Logout
- `7` - Exit

## 🛡️ Security

- **Encryption:** Fernet (AES-128 CBC + HMAC-SHA256)
- **Password hashing:** bcrypt with random salts
- **Local storage:** All data stays on your machine
- **Recovery tokens:** Secure backup for master password reset
- **Auto-lock:** Prevents unauthorized access after inactivity
- **Clipboard security:** Passwords auto-clear after 20 seconds

## 📁 Data Location

Your encrypted vaults are stored locally at:
- **Linux:** `~/.local/share/lox/users/`
- **macOS:** `~/Library/Application Support/lox/users/`
- **Windows:** `%APPDATA%/lox/users/`

## 🚀 Coming to PyPI

Soon you'll be able to install with just:
```bash
pip install lox-cli
lox
```

## 🤝 Contributing

Found a bug or want to contribute? Issues and pull requests are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

**⚠️ Security Notice:** This tool stores passwords locally with strong encryption. Always keep your recovery tokens safe and consider regular backups of your vault files. Never share your master password or recovery tokens.
