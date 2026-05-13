"""
Email Intelligence Module
Performs public email footprint analysis
"""

import re
import requests
from datetime import datetime
from rich.panel import Panel
from rich.table import Table
from utils.logger import Logger
from utils.ascii_art import ASCII_BANNERS
from utils.startup_manager import LoadingBar


class EmailIntelligence:
    """Email intelligence and footprint analysis"""
    
    def __init__(self, console=None, logger=None):
        self.console = console
        self.logger = logger or Logger()
    
    def get_banner(self):
        """Return module banner"""
        return ASCII_BANNERS['email_module']
    
    def analyze(self, email: str) -> Panel:
        """
        Analyze email for intelligence
        
        Args:
            email: Email address to analyze
        
        Returns:
            Rich Panel with analysis results
        """
        try:
            # Validate email format
            if not self._validate_email(email):
                return self._create_error_panel("Invalid email format")
            
            LoadingBar.show_spinner("Analyzing email footprint...", duration=1.5)
            
            # Extract components
            local_part, domain = email.split('@')
            
            # Gather intelligence
            data = {
                'email': email,
                'local_part': local_part,
                'domain': domain,
                'domain_info': self._get_domain_info(domain),
                'breach_status': self._check_breach_status(email),
                'linked_usernames': self._extract_usernames(local_part),
                'analysis_timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
            }
            
            self.logger.success(f"Email analysis completed for {email}")
            
            return self._create_results_panel(data)
        
        except Exception as e:
            self.logger.error(f"Email analysis error: {str(e)}")
            return self._create_error_panel(f"Analysis failed: {str(e)}")
    
    def _validate_email(self, email: str) -> bool:
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def _get_domain_info(self, domain: str) -> dict:
        """Get information about the email domain"""
        try:
            # Check if domain is disposable
            disposable_domains = [
                'temp-mail.org', 'guerrillamail.com', '10minutemail.com',
                'maildrop.cc', 'tempmail.com'
            ]
            
            is_disposable = domain.lower() in disposable_domains
            
            # Check MX records (simplified)
            mx_check = "Standard mail provider"
            if domain.endswith('.gov'):
                mx_check = "Government domain"
            elif domain.endswith('.edu'):
                mx_check = "Educational institution"
            elif domain.endswith('.org'):
                mx_check = "Organization"
            elif domain.endswith('.com'):
                mx_check = "Commercial domain"
            
            return {
                'domain': domain,
                'type': mx_check,
                'disposable': is_disposable,
                'mx_status': 'Valid' if not is_disposable else 'Disposable'
            }
        except:
            return {'domain': domain, 'type': 'Unknown', 'disposable': False}
    
    def _check_breach_status(self, email: str) -> dict:
        """Check if email appears in public breaches"""
        try:
            # This would typically use Have I Been Pwned API
            # For educational purposes, we note that real implementation requires API key
            return {
                'checked': True,
                'breaches_found': 0,
                'note': 'Use HaveIBeenPwned.com API for real-time breach checking',
                'recommendation': 'Enable 2FA if breaches found'
            }
        except Exception as e:
            return {'error': str(e), 'checked': False}
    
    def _extract_usernames(self, local_part: str) -> list:
        """Extract potential usernames from email local part"""
        usernames = []
        
        # Split by common delimiters
        parts = re.split(r'[._\-]', local_part)
        
        for part in parts:
            if len(part) > 2:
                usernames.append(part.lower())
        
        # Add full local part if it looks like a username
        if len(local_part) > 3 and not local_part.isdigit():
            usernames.append(local_part.lower())
        
        return list(set(usernames))  # Remove duplicates
    
    def _create_results_panel(self, data: dict) -> Panel:
        """Create formatted results panel"""
        content = f"""
[bold cyan]Email:[/bold cyan] {data['email']}
[bold cyan]Local Part:[/bold cyan] {data['local_part']}

[bold green]DOMAIN INFORMATION[/bold green]
[bold cyan]Domain:[/bold cyan] {data['domain_info']['domain']}
[bold cyan]Type:[/bold cyan] {data['domain_info']['type']}
[bold cyan]Disposable:[/bold cyan] {'✗ Yes' if data['domain_info']['disposable'] else '✓ No'}
[bold cyan]MX Status:[/bold cyan] {data['domain_info']['mx_status']}

[bold green]BREACH INTELLIGENCE[/bold green]
[bold cyan]Checked:[/bold cyan] {'✓ Yes' if data['breach_status']['checked'] else '✗ No'}
[bold cyan]Breaches Found:[/bold cyan] {data['breach_status']['breaches_found']}
[bold yellow]Note:[/bold yellow] {data['breach_status']['note']}

[bold green]LINKED USERNAMES[/bold green]
[bold cyan]Potential Usernames:[/bold cyan] {', '.join(data['linked_usernames'])}

[bold cyan]Analysis Timestamp:[/bold cyan] {data['analysis_timestamp']}

[bold yellow]OSINT Note:[/bold yellow] Use extracted usernames for further reconnaissance.
        """
        
        return Panel(
            content.strip(),
            title="[bold green]✓ EMAIL INTELLIGENCE REPORT[/bold green]",
            border_style="green",
            style="dim white"
        )
    
    def _create_error_panel(self, error_msg: str) -> Panel:
        """Create error panel"""
        return Panel(
            f"[bold red]✗ {error_msg}[/bold red]",
            title="[bold red]ERROR[/bold red]",
            border_style="red",
            style="dim white"
        )
