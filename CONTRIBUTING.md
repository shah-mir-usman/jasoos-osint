# Contributing to Jasoos OSINT Framework

Thank you for considering contributing to Jasoos! This document provides guidelines and instructions for contributing.

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive.

### Expected Behavior

- Use welcoming and inclusive language
- Be respectful of differing opinions
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Started

### Prerequisites

- Python 3.8+
- Git
- pip/pip3
- Virtual environment (recommended)

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/shah-mir/jasoos-osint.git
cd jasoos-osint

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install flake8 black pylint pytest
```

## Types of Contributions

### 1. Bug Reports

Found a bug? Please report it!

**Include:**
- Clear description of the bug
- Steps to reproduce
- Expected behavior
- Actual behavior
- Python version
- Operating system
- Relevant error logs

**Create an issue with:**

```
Title: [BUG] Brief description

Description:
- What were you doing?
- What happened?
- What should have happened?

Error Message:
[Paste error output here]

System Info:
- OS: 
- Python: 
- Framework Version:
```

### 2. Feature Requests

Have an idea for improvement?

**Include:**
- Clear use case
- Expected behavior
- Why it would be useful
- Example implementation (if possible)

**Example:**

```
Title: [FEATURE] Add DNS enumeration module

Description:
I'd like to add DNS records lookup for domains...
This would help with...
```

### 3. Code Improvements

- Performance optimizations
- Code refactoring
- Error handling improvements
- Documentation updates

### 4. Documentation

- README improvements
- Code example additions
- Tutorial creation
- Comment clarification

## Development Workflow

### 1. Create a Branch

```bash
# Update main branch
git checkout main
git pull origin main

# Create feature branch
git checkout -b feature/amazing-feature

# Or for bug fixes
git checkout -b bugfix/issue-description
```

### Naming Conventions

- Features: `feature/short-description`
- Bugs: `bugfix/issue-number-description`
- Docs: `docs/update-name`
- Tests: `test/what-is-tested`

### 2. Make Changes

```bash
# Edit files
nano modules/my_module.py

# Test your changes
python3 jasoos_main.py
```

### Code Style

Follow PEP 8:

```bash
# Format code with black
black *.py modules/*.py utils/*.py

# Check style
flake8 . --max-line-length=100

# Lint with pylint
pylint modules/my_module.py
```

### 3. Commit Changes

```bash
# Stage changes
git add .

# Commit with clear message
git commit -m "Add feature: description

- Specific change 1
- Specific change 2
- Fixes issue #123"
```

### Commit Message Guidelines

Format: `<type>: <subject>`

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style
- `refactor`: Code refactor
- `test`: Tests
- `chore`: Maintenance

Example:
```
feat: Add DNS enumeration module

- Implement DNS record lookup
- Add public DNS API integration
- Create comprehensive tests
```

### 4. Push and Create Pull Request

```bash
# Push branch
git push origin feature/amazing-feature

# Create pull request on GitHub
```

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update

## Changes Made
- Change 1
- Change 2

## Testing
- [ ] Tested on Python 3.8
- [ ] Tested on Python 3.10
- [ ] All modules load correctly

## Related Issues
Fixes #123

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] No new warnings generated
```

## Module Development

### Creating New Module

```python
"""
Email Intelligence Module
Description of what the module does
"""

from rich.panel import Panel
from utils.logger import Logger
from utils.ascii_art import ASCII_BANNERS

class NewIntelligence:
    """Module description"""
    
    def __init__(self, console=None, logger=None):
        self.console = console
        self.logger = logger or Logger()
    
    def get_banner(self):
        """Return module banner"""
        return ASCII_BANNERS['module_name']
    
    def analyze(self, target: str) -> Panel:
        """
        Analyze target
        
        Args:
            target: Target to analyze
        
        Returns:
            Rich Panel with results
        """
        try:
            # Implementation
            result = self._analyze(target)
            return self._create_results_panel(result)
        
        except Exception as e:
            self.logger.error(f"Error: {str(e)}")
            return self._create_error_panel(f"Failed: {str(e)}")
    
    def _create_results_panel(self, data: dict) -> Panel:
        """Format results"""
        return Panel(
            content,
            title="[bold green]✓ RESULTS[/bold green]",
            border_style="green"
        )
    
    def _create_error_panel(self, msg: str) -> Panel:
        """Format error"""
        return Panel(
            f"[bold red]✗ {msg}[/bold red]",
            title="[bold red]ERROR[/bold red]",
            border_style="red"
        )
```

### Add to Menu Handler

Edit `core/menu_handler.py`:

```python
# Import
from modules.new_module import NewIntelligence

# Initialize in __init__
self.new_intel = NewIntelligence(console=self.console, logger=self.logger)

# Add menu option
def handle_option_8(self):
    """Handle new module"""
    self.logger.section("NEW MODULE")
    self.console.print(self.new_intel.get_banner())
    
    target = HackerInput.get_input("Enter target: ")
    if target:
        result = self.new_intel.analyze(target)
        self.investigation_data['new'] = result
        self.console.print(result)

# Add to menu_options
menu_options = {
    # ... existing
    '8': self.handle_option_8,
}

# Update main menu display
menu_content += "[bold green][8][/bold green]  New Module\n"
```

## Testing

### Run Tests

```bash
# Test imports
python3 -c "import modules.phone_intelligence"

# Run framework
python3 jasoos_main.py

# Check specific module
python3 -c "from modules.phone_intelligence import PhoneIntelligence"
```

### Create Tests

```python
# test_phone_intelligence.py
import pytest
from modules.phone_intelligence import PhoneIntelligence

def test_valid_phone():
    """Test valid phone number"""
    pi = PhoneIntelligence()
    result = pi.analyze("+923001234567")
    assert result is not None

def test_invalid_phone():
    """Test invalid phone number"""
    pi = PhoneIntelligence()
    result = pi.analyze("invalid")
    assert "error" in str(result).lower()
```

## Documentation

### Code Comments

```python
def analyze(self, phone_number: str) -> Panel:
    """
    Analyze phone number for intelligence.
    
    Args:
        phone_number (str): International phone number with country code
        
    Returns:
        Panel: Rich Panel with analysis results
        
    Raises:
        phonenumbers.NumberParseException: If number format invalid
        
    Example:
        >>> analyzer = PhoneIntelligence()
        >>> result = analyzer.analyze("+923001234567")
    """
```

### Update README

- Add feature to feature list
- Add usage example
- Document return values
- Include output example

## Review Process

### What Reviewers Look For

1. **Code Quality**
   - Follows PEP 8
   - Clear variable names
   - Proper error handling
   - No code duplication

2. **Functionality**
   - Works as intended
   - No breaking changes
   - Handles edge cases
   - Performance acceptable

3. **Documentation**
   - Comments clear
   - README updated
   - Examples provided
   - Docstrings complete

4. **Testing**
   - Code tested
   - Edge cases covered
   - No regressions
   - Works on multiple Python versions

## Legal & Ethical

### Before Contributing

1. Ensure your code is for educational use only
2. No illegal functionality
3. No surveillance features
4. Respect privacy
5. Follow responsible disclosure

### Code License

By contributing, you agree your code is under the same license as the project (Educational Use).

## Community

### Ask Questions

- Create an issue
- Use GitHub Discussions
- Check documentation first
- Be specific and clear

### Share Ideas

- Open feature request
- Discuss in issues
- Contribute improvements
- Help others

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in documentation
- Recognized in community

## Questions?

- 📖 Check README.md
- 🔍 Search existing issues
- 💬 Create new discussion
- 📧 Reach out respectfully

---

## Development Checklist

Before submitting PR:

- [ ] Code works locally
- [ ] No errors or warnings
- [ ] Follows PEP 8
- [ ] Comments added
- [ ] README updated
- [ ] No API keys in code
- [ ] Imports organized
- [ ] Tests pass
- [ ] Commit messages clear
- [ ] Branch up to date with main

---

## Code Review Tips

### As a Contributor

- Respond to feedback promptly
- Ask clarifying questions
- Implement suggestions
- Be open to criticism
- Update based on review

### As a Reviewer

- Be constructive
- Suggest improvements
- Ask questions
- Approve when ready
- Thank contributors

---

Thank you for contributing to Jasoos! 🎉

Your efforts help improve OSINT education for everyone.

---

**Last Updated:** January 2024
**Framework:** Jasoos By Shah-Mir v1.0.0
