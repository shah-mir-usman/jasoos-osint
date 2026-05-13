```
╔════════════════════════════════════════════════════════════════════════════╗
║                 JASOOS - QUICK START GUIDE                                ║
║              Get Running in 60 Seconds or Less!                           ║
╚════════════════════════════════════════════════════════════════════════════╝
```

# ⚡ Quick Start: 60 Seconds

## 1️⃣ Clone & Setup (30 seconds)

```bash
# Clone repository
git clone https://github.com/shah-mir/jasoos-osint.git
cd jasoos-osint

# Install dependencies
pip3 install -r requirements.txt
```

## 2️⃣ Run! (30 seconds)

```bash
python3 jasoos_main.py
```

## 3️⃣ You're Live! 🎉

```
        ✓ Ethical warning shown
        ✓ Startup sequence plays
        ✓ System info displayed
        ✓ Interactive menu ready
```

---

# 🎯 First Search (2 minutes)

### Try Phone Intelligence

```bash
Main menu appears → Enter [1] → Phone Number Intelligence
↓
Enter phone number with country code
Example: +923001234567
↓
Get instant results:
  - Country: Pakistan
  - Region: Karachi
  - Timezone: Asia/Karachi
  - Operator: Jazz/Zong
  - Line Type: Mobile
```

### Try Username Search

```bash
Main menu → Enter [3] → Username Reconnaissance
↓
Enter username: john_doe
↓
Get results across 20+ platforms:
  - GitHub: ✓ FOUND
  - Twitter: ✗ Not Found
  - Instagram: ✓ FOUND
  - ... and more
```

---

# 📚 Module Overview

| # | Module | Input | Output |
|---|--------|-------|--------|
| 1 | Phone Intelligence | Phone # | Country, Region, Carrier, Timezone |
| 2 | Social Media | Username | Account links across platforms |
| 3 | Username Recon | Username | 20+ platform search results |
| 4 | Email Intel | Email | Domain info, breach status |
| 5 | Geo Lookup | Phone # | Telecom metadata, region |
| 6 | Breach Check | Email | Compromise status |
| 7 | Report Generator | All data | TXT/JSON/HTML report |

---

# 🚀 Common Use Cases

### Use Case 1: Search Someone's Email

```
[4] Email Intelligence
↓
user@example.com
↓
See: Domain type, linked usernames, breach status
```

### Use Case 2: Find All Social Accounts

```
[2] Social Media Enumeration
↓
username
↓
Get: All accounts found across platforms
```

### Use Case 3: Generate Professional Report

```
[7] Export Investigation Report
↓
Select format: html
↓
Report saved to reports/ folder
```

---

# 🎓 Learning Path

### Beginner (Day 1)
1. Install framework
2. Try [1] Phone Intelligence
3. Try [4] Email Intelligence
4. Read results carefully

### Intermediate (Week 1)
1. Try all 7 modules
2. Practice with different inputs
3. Compare results between modules
4. Generate reports in different formats

### Advanced (Week 2+)
1. Edit module files
2. Add custom platforms
3. Integrate with other tools
4. Contribute improvements

---

# 🔧 Troubleshooting Quick Fixes

### "ModuleNotFoundError"

```bash
pip3 install --upgrade -r requirements.txt
```

### "Permission denied"

```bash
chmod +x jasoos_main.py
python3 jasoos_main.py
```

### "Connection timeout"

Edit module and increase timeout:
```python
# Change in module files:
self.timeout = aiohttp.ClientTimeout(total=30)  # Increase from 10
```

### Colors not showing

```bash
export TERM=xterm-256color
python3 jasoos_main.py
```

---

# 📋 File Locations

```
jasoos-osint/
├── jasoos_main.py          ← RUN THIS
├── requirements.txt        ← Install this
├── README.md              ← Full documentation
├── INSTALL.md             ← Detailed setup
├── CONTRIBUTING.md        ← How to contribute
│
├── modules/               ← Intelligence modules
│   ├── phone_intelligence.py
│   ├── social_enumeration.py
│   ├── username_recon.py
│   ├── email_intelligence.py
│   ├── geo_lookup.py
│   ├── breach_check.py
│   └── report_generator.py
│
├── utils/                 ← Helper utilities
│   ├── startup_manager.py
│   ├── terminal_designer.py
│   ├── ascii_art.py
│   └── logger.py
│
├── core/                  ← Core functionality
│   └── menu_handler.py
│
├── reports/               ← Generated reports (auto-created)
└── logs/                  ← Operation logs (auto-created)
```

---

# ⚠️ Important Reminders

✅ **DO:**
- Use for authorized investigations only
- Research on systems you own
- Learn about cybersecurity
- Use responsibly and ethically
- Document your authorization

❌ **DON'T:**
- Use on systems without permission
- Track real people's locations
- Perform surveillance
- Use for illegal purposes
- Violate privacy laws

---

# 🆘 Help & Support

### Stuck? Try This Order:

1. **Read README.md** - Full documentation
2. **Check INSTALL.md** - Setup troubleshooting
3. **Review code comments** - Docstrings explain functions
4. **Check logs** - `cat logs/jasoos_*.log`
5. **Google the error** - Usually helpful

### Get Help:
- 📖 Documentation: README.md
- 🐛 Report bugs: GitHub Issues
- 💡 Feature requests: GitHub Issues
- 👥 Ask community: Cybersecurity forums

---

# 🎯 Next 30 Minutes

```
0:00 - 1:00   Install framework
1:00 - 2:00   Run and explore menu
2:00 - 5:00   Try each module (1 min per module)
5:00 - 10:00  Generate a report
10:00+        Read documentation and learn more
```

---

# 🚀 Pro Tips

### Tip 1: Combine Multiple Modules
```
Search username → Find email → Check breaches → Generate report
```

### Tip 2: Create Aliases
```bash
# Add to ~/.bashrc
alias jasoos='python3 /path/to/jasoos_main.py'

# Now just type:
jasoos
```

### Tip 3: Schedule Reports
```bash
# Run daily and save report
0 9 * * * python3 /path/to/jasoos_main.py > /tmp/jasoos.log 2>&1
```

### Tip 4: Use in Scripts
```python
# Import and use in your scripts
from modules.phone_intelligence import PhoneIntelligence

pi = PhoneIntelligence()
result = pi.analyze("+923001234567")
```

---

# 📊 Performance Notes

- **Startup:** < 2 seconds
- **Phone lookup:** < 1 second
- **Email analysis:** < 2 seconds
- **Username search:** 5-10 seconds (20+ platforms)
- **Report generation:** < 1 second

---

# 🎉 You're Ready!

```bash
python3 jasoos_main.py
```

Start exploring. Learn. Use responsibly.

---

```
╔════════════════════════════════════════════════════════════════════════════╗
║                 Quick Start Complete!                                     ║
║              For full docs: Read README.md                                 ║
║                 Happy OSINT Learning! 🔍                                   ║
╚════════════════════════════════════════════════════════════════════════════╝
```

**Framework:** Jasoos By Shah-Mir v1.0.0
**Status:** Educational Use Only
**Last Updated:** January 2024
