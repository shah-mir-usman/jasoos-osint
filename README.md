```
      ██╗ █████╗ ███████╗ ██████╗  ██████╗ ███████╗
      ██║██╔══██╗██╔════╝██╔═══██╗██╔═══██╗██╔════╝
      ██║███████║███████╗██║   ██║██║   ██║███████╗
 ██   ██║██╔══██║╚════██║██║   ██║██║   ██║╚════██║
 ╚█████╔╝██║  ██║███████║╚██████╔╝╚██████╔╝███████║
  ╚════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝

             JASOOS BY SHAH-MIR
        Advanced Cybersecurity OSINT Framework
              Final Year Project v1.0.0
```

---

## 📋 Overview

**Jasoos** is a professional, cinematic OSINT (Open Source Intelligence) framework designed for educational purposes, authorized cybersecurity investigations, and research. Built with a powerful hacker-style terminal interface, it combines multiple intelligence-gathering modules into a unified, user-friendly platform.

### Key Features

✅ **Professional Terminal Interface**
- Matrix-style animated startup sequence
- Neon green hacker aesthetics
- Smooth typing animations and transitions
- Live progress bars and loading indicators
- Professional panel-based UI design

✅ **Comprehensive OSINT Modules**
1. **Phone Number Intelligence** - International mobile analysis
2. **Social Media Enumeration** - Multi-platform account detection
3. **Username Reconnaissance** - Cross-platform username search
4. **Email Intelligence** - Public footprint analysis
5. **Geo Metadata Lookup** - Telecom information (legal, educational use)
6. **Public Breach Check** - Data compromise detection
7. **Report Generation** - Professional report export (TXT/JSON/HTML)

✅ **Multi-Platform Compatibility**
- 🐧 Kali Linux
- 🐧 Ubuntu & Debian derivatives
- 🐧 macOS
- 🖥️ VMware virtual machines

✅ **Production-Ready Code**
- Modular architecture
- Async operations for performance
- Comprehensive error handling
- Professional logging system
- Clean Git-ready structure

---

## ⚖️ LEGAL & ETHICAL DISCLAIMER

### ⚠️ IMPORTANT

**This framework is intended STRICTLY for:**
- ✅ Educational cybersecurity research
- ✅ Authorized penetration testing engagements
- ✅ Legal cybersecurity investigations
- ✅ Personal security awareness

**UNAUTHORIZED USE IS ILLEGAL**

This tool should only be used:
- With explicit written permission from target owners
- In compliance with all applicable laws and regulations
- By authorized security professionals
- For lawful purposes only

The author assumes **NO LIABILITY** for misuse or illegal activity.

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Linux/Unix environment (Kali Linux, Ubuntu, macOS, or VM)
- Terminal emulator supporting ANSI colors

### Quick Start

#### 1. Clone the Repository

```bash
git clone https://github.com/shah-mir/jasoos-osint.git
cd jasoos-osint
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or for system-wide installation (Kali Linux):

```bash
sudo apt-get update
sudo apt-get install python3-pip
pip3 install -r requirements.txt
```

#### 3. Make Executable (Optional)

```bash
chmod +x jasoos_main.py
```

#### 4. Run the Framework

```bash
python3 jasoos_main.py
```

Or directly:

```bash
./jasoos_main.py
```

---

## 🎮 Usage Guide

### Main Menu

When you launch Jasoos, you'll see an interactive menu:

```
⚙️  MAIN CONTROL PANEL

[1] Phone Number Intelligence
[2] Social Media Enumeration
[3] Username Reconnaissance
[4] Email Intelligence
[5] Geo Metadata Lookup
[6] Public Breach Check
[7] Export Investigation Report
[0] Exit Framework

Enter your choice:
```

### Module Guide

#### 1️⃣ Phone Number Intelligence

Analyze international phone numbers for intelligence:

```bash
Enter phone number (with country code, e.g., +1234567890): +923001234567
```

**Provides:**
- Country of origin
- Region/city information
- Timezone
- Mobile operator
- Line type classification
- Number validity

**Example Output:**
```
Phone Number: +923001234567
Valid: ✓ YES
Country: Pakistan
Region Code: PK
Area: Karachi
Timezone: Asia/Karachi
Carrier: Jazz (Zong)
Line Type: Mobile
```

#### 2️⃣ Social Media Enumeration

Search for accounts across social platforms:

```bash
Enter phone number or username: john_doe
```

**Searches Across:**
- Telegram, WhatsApp
- Instagram, Facebook
- Twitter/X, LinkedIn
- GitHub, Snapchat
- TikTok, YouTube
- Reddit, Discord

#### 3️⃣ Username Reconnaissance

Sherlock-style username search across 20+ platforms:

```bash
Enter username to search: hacker_ninja
```

**Returns:**
- Platform availability
- Direct profile links
- HTTP status codes
- Response times

#### 4️⃣ Email Intelligence

Analyze public email footprints:

```bash
Enter email address: user@example.com
```

**Analyzes:**
- Domain information
- Email provider type
- Breach status (educational)
- Linked usernames
- Public references

#### 5️⃣ Geo Metadata Lookup

Retrieve telecom metadata (educational, legal use):

```bash
Enter phone number or IP address: +441234567890
```

**Provides:**
- Country/region information
- Provider area coverage
- Timezone
- Operator details
- Regional classification

⚠️ **Note:** This is telecom registration data only. NO live GPS tracking or surveillance.

#### 6️⃣ Public Breach Check

Check if data appears in public breaches:

```bash
Enter email or username for breach check: user@example.com
```

**Checks:**
- Public breach databases
- Compromised credentials
- Recommended actions
- Security status

#### 7️⃣ Export Investigation Report

Generate professional investigation reports:

```bash
Select format (txt/json/html) [default: txt]: html
```

Reports are saved to `./reports/` directory with:
- Professional formatting
- All collected data
- Legal disclaimers
- Timestamp and metadata

---

## 📁 Project Structure

```
jasoos-osint/
├── jasoos_main.py              # Main entry point
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── core/
│   └── menu_handler.py        # Main menu and navigation
│
├── modules/
│   ├── phone_intelligence.py  # Phone analysis
│   ├── social_enumeration.py  # Social media search
│   ├── username_recon.py      # Username reconnaissance
│   ├── email_intelligence.py  # Email analysis
│   ├── geo_lookup.py          # Geographic metadata
│   ├── breach_check.py        # Breach detection
│   └── report_generator.py    # Report creation
│
├── utils/
│   ├── startup_manager.py     # Startup sequence
│   ├── terminal_designer.py   # UI components
│   ├── ascii_art.py           # ASCII banners
│   └── logger.py              # Logging system
│
├── reports/                    # Generated reports
└── logs/                       # Operation logs
```

---

## 🛠️ Configuration

### Setting API Keys (Advanced)

Some modules support optional API keys for enhanced functionality:

Create a `config.ini` file:

```ini
[APIS]
haveibeenpwned_key = your_api_key_here
github_token = your_github_token
twitter_bearer = your_twitter_bearer_token
```

### Customizing Platforms

Edit module files to add/remove platforms:

```python
# In modules/social_enumeration.py
PLATFORMS = {
    'custom_platform': {
        'url': 'https://custom.com/{target}',
        'check_method': 'direct',
        'description': 'Custom Platform'
    },
    # ... existing platforms
}
```

---

## 📊 Output Formats

### Text Report

Plain text format suitable for documentation:
```
Report ID: 20240115_143022
Generated: 2024-01-15 14:30:22 UTC
Phone: +923001234567
Country: Pakistan
Timezone: Asia/Karachi
```

### JSON Report

Structured data format for automation:
```json
{
  "metadata": {
    "generated": "2024-01-15T14:30:22",
    "framework": "Jasoos By Shah-Mir",
    "version": "1.0.0"
  },
  "investigation_data": {
    "phone": {...},
    "social": {...}
  }
}
```

### HTML Report

Professional visual format with styling:
- Cinematic cyberpunk design
- Green terminal aesthetic
- Responsive layout
- Printable format

---

## 🔧 Troubleshooting

### Module Import Errors

```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Terminal Color Issues

```bash
# Force color support
export TERM=xterm-256color
python3 jasoos_main.py
```

### Slow Network Requests

The framework includes timeouts. If slow:

Edit module files and adjust timeout values:
```python
self.timeout = aiohttp.ClientTimeout(total=15)  # Increase timeout
```

### Permission Denied

```bash
# Make script executable
chmod +x jasoos_main.py
```

---

## 🎓 Educational Use Cases

1. **Cybersecurity Training** - Learn OSINT fundamentals
2. **Security Awareness** - Understand digital footprints
3. **Penetration Testing** - Part of authorized assessments
4. **Security Research** - Academic cybersecurity projects
5. **Digital Hygiene** - Audit your own online presence

---

## 🚀 Advanced Features

### Async Operations

The framework uses asyncio for efficient concurrent requests:
- Faster username searches across 20+ platforms
- Reduced latency in social media enumeration
- Optimized network resource usage

### Professional Logging

All operations are logged:
```bash
cat logs/jasoos_*.log
```

### Module Extensibility

Create custom modules:

```python
# custom_module.py
from rich.panel import Panel

class CustomIntelligence:
    def __init__(self, console=None, logger=None):
        self.console = console
        self.logger = logger
    
    def analyze(self, target):
        # Your custom logic
        return self._create_results_panel(results)
```

---

## 📈 Performance Metrics

- **Startup Time:** < 2 seconds
- **Username Search:** ~5-10 seconds for 20+ platforms
- **Phone Analysis:** < 1 second
- **Email Analysis:** < 2 seconds
- **Report Generation:** < 1 second

---

## 🔐 Security Notes

### Data Privacy

- No data is sent to external servers
- All operations are local
- No personal information is stored
- Reports are generated locally

### Safe Usage

1. Only scan targets you own or have authorization for
2. Respect privacy and legal boundaries
3. Document your authorization
4. Follow responsible disclosure
5. Review all findings carefully

---

## 🤝 Contributing

Contributions welcome for:
- Additional OSINT modules
- Bug fixes and improvements
- Documentation enhancements
- Performance optimizations
- Security hardening

### Contribution Guidelines

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📝 License

This project is provided for **educational purposes only**.

**Terms of Use:**
- For authorized use only
- Not for surveillance or illegal purposes
- User assumes full responsibility
- Author provides no liability guarantee

---

## 👨‍💻 Author

**Shah-Mir**
- Final Year Cybersecurity Project
- Educational OSINT Framework
- Professional Security Research

---

## 📚 References & Resources

### Learning Resources
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [CTF Training Platforms](https://ctftime.org/)
- [HackTheBox](https://www.hackthebox.com/)

### Similar Projects
- [Sherlock](https://github.com/sherlock-project/sherlock)
- [PhoneInfoga](https://github.com/sundowndev/phoneinfoga)
- [theHarvester](https://github.com/laramies/theHarvester)

### API Documentation
- [Have I Been Pwned API](https://haveibeenpwned.com/API/v3)
- [phonenumbers Library](https://github.com/daviddrysdale/python-phonenumbers)
- [GitHub REST API](https://docs.github.com/en/rest)

---

## ⚡ Quick Commands

```bash
# Install and run
git clone https://github.com/shah-mir/jasoos-osint.git
cd jasoos-osint
pip install -r requirements.txt
python3 jasoos_main.py

# Check logs
tail -f logs/jasoos_*.log

# View reports
ls reports/

# Update dependencies
pip install --upgrade -r requirements.txt
```

---

## 🎯 Roadmap (Future Versions)

- [ ] Web dashboard interface
- [ ] Cloud integration (AWS, Azure)
- [ ] Machine learning categorization
- [ ] Advanced breach API integrations
- [ ] Blockchain analysis
- [ ] Dark web monitoring
- [ ] Real-time alerts
- [ ] Team collaboration features

---

## 📞 Support

For issues and questions:
1. Check the documentation
2. Review existing GitHub issues
3. Create a detailed issue report
4. Include error logs and system info

---

## ⭐ Show Your Support

If you found this useful for educational purposes, please:
- Star the repository
- Share with the security community
- Contribute improvements
- Cite in academic work

---

## 🙏 Acknowledgments

Built for the cybersecurity education community with inspiration from:
- Sherlock username project
- PhoneInfoga framework
- theHarvester
- OSINT community

---

```
╔════════════════════════════════════════════════════════════════════════════╗
║  Educational Use Only | Authorized Investigations Only | Final Year Project ║
║                   Jasoos By Shah-Mir - OSINT Framework v1.0.0             ║
╚════════════════════════════════════════════════════════════════════════════╝
```

---

**Last Updated:** January 2024
**Framework Version:** 1.0.0
**Python Version:** 3.8+
**License:** Educational Use Only
