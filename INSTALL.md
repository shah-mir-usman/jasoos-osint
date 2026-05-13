```
╔════════════════════════════════════════════════════════════════════════════╗
║                    JASOOS - INSTALLATION GUIDE                            ║
║                   Advanced OSINT Framework Setup                          ║
╚════════════════════════════════════════════════════════════════════════════╝
```

# Installation Guide for Jasoos OSINT Framework

## 🎯 Supported Environments

- ✅ Kali Linux (Recommended)
- ✅ Ubuntu 18.04+ / Debian
- ✅ Parrot OS
- ✅ BlackArch
- ✅ macOS
- ✅ VMware/Virtual Box
- ✅ WSL2 (Windows Subsystem for Linux)

## 📋 Requirements

### Minimum System Requirements
- RAM: 2GB
- Disk Space: 500MB
- Python: 3.8 or higher
- Internet Connection

### Recommended
- RAM: 4GB+
- SSD Storage
- Linux Kernel 5.0+
- Root/Admin access (for system-wide install)

---

## 🚀 Quick Installation (5 minutes)

### Step 1: Clone the Repository

```bash
# Using HTTPS
git clone https://github.com/shah-mir/jasoos-osint.git
cd jasoos-osint

# Or using SSH (if configured)
git clone git@github.com:shah-mir/jasoos-osint.git
cd jasoos-osint
```

### Step 2: Install Dependencies

#### Option A: User Installation (Recommended)

```bash
# Install pip3 if not present
sudo apt-get install python3-pip

# Install dependencies in user directory
pip3 install --user -r requirements.txt
```

#### Option B: Virtual Environment (Safest)

```bash
# Create virtual environment
python3 -m venv jasoos_env

# Activate virtual environment
source jasoos_env/bin/activate  # Linux/Mac
# OR
jasoos_env\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

#### Option C: System-Wide Installation (Root)

```bash
# Install system-wide
sudo pip3 install -r requirements.txt
```

### Step 3: Make Executable

```bash
chmod +x jasoos_main.py
```

### Step 4: Run!

```bash
python3 jasoos_main.py

# Or if executable:
./jasoos_main.py
```

---

## 🐧 Kali Linux Specific Installation

### Automated Setup

```bash
# Update system
sudo apt-get update && sudo apt-get upgrade -y

# Clone repository
git clone https://github.com/shah-mir/jasoos-osint.git
cd jasoos-osint

# Run installation script
bash install.sh  # If available

# Or manual installation
sudo pip3 install -r requirements.txt
chmod +x jasoos_main.py
```

### Install in Kali Tools Menu

```bash
# Copy to applications
sudo cp jasoos_main.py /usr/local/bin/jasoos
sudo chmod +x /usr/local/bin/jasoos

# Now you can run from anywhere
jasoos

# Or add to .bashrc for alias
echo "alias jasoos='python3 /path/to/jasoos_main.py'" >> ~/.bashrc
source ~/.bashrc
```

---

## 🐳 Docker Installation (Optional)

### Create Dockerfile

```dockerfile
FROM kalilinux/kali-rolling

WORKDIR /opt/jasoos

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "jasoos_main.py"]
```

### Build and Run

```bash
# Build Docker image
docker build -t jasoos:latest .

# Run container
docker run -it jasoos:latest

# Or with volume mount
docker run -it -v $(pwd)/reports:/opt/jasoos/reports jasoos:latest
```

---

## 🔧 Troubleshooting Installation

### Problem: "python3: command not found"

**Solution:**
```bash
# Install Python3
sudo apt-get install python3 python3-pip

# Verify installation
python3 --version
```

### Problem: "ModuleNotFoundError: No module named 'rich'"

**Solution:**
```bash
# Reinstall all dependencies
pip3 install --upgrade --force-reinstall -r requirements.txt

# Or install individually
pip3 install rich colorama phonenumbers requests beautifulsoup4
```

### Problem: "Permission denied" when running

**Solution:**
```bash
# Make script executable
chmod +x jasoos_main.py

# Or run with python3
python3 jasoos_main.py
```

### Problem: Import errors after installation

**Solution:**
```bash
# Clear Python cache
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name "*.pyc" -delete

# Reinstall
pip3 install -r requirements.txt --force-reinstall
```

### Problem: "aiohttp" timeout errors

**Solution:**
```bash
# Update aiohttp
pip3 install --upgrade aiohttp

# Or edit module timeout in code:
# Change: self.timeout = aiohttp.ClientTimeout(total=10)
# To: self.timeout = aiohttp.ClientTimeout(total=30)
```

---

## 📦 Dependency Details

### Core Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| rich | 13.7.0+ | Terminal UI and formatting |
| colorama | 0.4.6+ | Color terminal output |
| phonenumbers | 8.13.0+ | Phone number parsing |
| requests | 2.31.0+ | HTTP requests |
| aiohttp | 3.9.1+ | Async HTTP client |
| beautifulsoup4 | 4.12.2+ | HTML parsing |

### Optional Dependencies

```bash
# For enhanced features
pip3 install selenium  # Browser automation
pip3 install pandas    # Data analysis
pip3 install matplotlib  # Visualization
```

---

## ✅ Verification

### Test Installation

```bash
# Run basic test
python3 -c "import rich, colorama, phonenumbers, requests; print('✓ All dependencies installed')"

# Or run framework
python3 jasoos_main.py

# Check if startup sequence works
# You should see animated loading and welcome screen
```

---

## 🔧 Post-Installation Setup

### 1. Create Configuration File (Optional)

```bash
mkdir -p ~/.jasoos
cat > ~/.jasoos/config.ini << EOF
[FRAMEWORK]
version = 1.0.0
mode = production

[LOGGING]
level = INFO
format = detailed

[MODULES]
timeout = 10
retries = 3
EOF
```

### 2. Create Directories

```bash
mkdir -p ./reports
mkdir -p ./logs
mkdir -p ./cache
```

### 3. Set Permissions

```bash
chmod 700 ./reports
chmod 700 ./logs
```

---

## 🌐 Network Configuration

### Proxy Setup (If Behind Firewall)

Edit modules to add proxy support:

```python
# Add to modules
import os
proxies = {
    'http': os.environ.get('HTTP_PROXY'),
    'https': os.environ.get('HTTPS_PROXY')
}
```

Set environment variables:

```bash
export HTTP_PROXY=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080
python3 jasoos_main.py
```

### DNS Configuration

```bash
# Use Google DNS
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
echo "nameserver 8.8.4.4" | sudo tee -a /etc/resolv.conf
```

---

## 🔐 Security Considerations

### 1. File Permissions

```bash
# Restrict report directory
chmod 700 ./reports

# Make logs private
chmod 700 ./logs

# Script should not be world-readable
chmod 755 jasoos_main.py
```

### 2. API Keys (If Using)

```bash
# Create secure config
mkdir -p ~/.jasoos
chmod 700 ~/.jasoos
nano ~/.jasoos/config.ini

# Never commit API keys
echo "config.ini" >> .gitignore
```

### 3. Virtual Environment Isolation

```bash
# Always use virtual environment for security
python3 -m venv jasoos_env
source jasoos_env/bin/activate
pip install -r requirements.txt
```

---

## 🎓 First Run

### Launch Framework

```bash
python3 jasoos_main.py
```

### What You'll See

1. **Ethical Warning** - Legal disclaimer
2. **Startup Sequence** - Animated loading
3. **System Info Panel** - Framework details
4. **Main Menu** - 7 module options + exit

### Try a Test Search

```
Enter your choice: 1
Enter phone number (+1234567890): +923001234567
```

---

## 📚 Post-Installation Resources

### Documentation
- Read `README.md` for full documentation
- Check module-specific docstrings: `python3 -c "import modules.phone_intelligence; help(modules.phone_intelligence)"`

### Update Framework

```bash
# Get latest version
cd jasoos-osint
git pull origin main
pip3 install --upgrade -r requirements.txt
```

### Uninstall

```bash
# Remove directory
rm -rf jasoos-osint

# Uninstall dependencies (if using global)
pip3 uninstall -r requirements.txt -y
```

---

## 🆘 Getting Help

### Common Issues

1. **Check Python version:** `python3 --version`
2. **Verify pip:** `pip3 --version`
3. **Test imports:** `python3 -c "import rich"`
4. **Check logs:** `cat logs/jasoos_*.log`

### Debug Mode

```bash
# Run with verbose logging
PYTHONVERBOSE=1 python3 jasoos_main.py

# Or enable debug in code
# Change: logger.setLevel(logging.DEBUG)
```

---

## 🎯 Next Steps

1. ✅ Complete installation
2. 📖 Read the README
3. 🧪 Test each module
4. 📊 Generate your first report
5. 🔍 Explore advanced features
6. 🤝 Contribute improvements

---

## ⚠️ Important Reminders

- **Educational Use Only** - This tool is for learning
- **Authorization Required** - Only scan systems you own/have permission for
- **Legal Compliance** - Follow all applicable laws
- **Ethical Usage** - Use responsibly and ethically
- **No Warranty** - Author assumes no liability

---

## 📞 Support Channels

- GitHub Issues: Create detailed issue reports
- Documentation: Check README.md
- Code Comments: Review docstrings
- Community: Share in cybersecurity forums

---

## 🎉 Installation Complete!

You're ready to use Jasoos! Run:

```bash
python3 jasoos_main.py
```

Enjoy responsible OSINT research! 🔍

---

```
╔════════════════════════════════════════════════════════════════════════════╗
║                  Installation Guide Complete                              ║
║               For full documentation, see README.md                        ║
║                    Educational Use Only                                    ║
╚════════════════════════════════════════════════════════════════════════════╝
```
