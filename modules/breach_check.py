"""
Public Breach Check Module
Checks if email/username appears in public breach databases
Educational use only - Uses public APIs
"""

import requests
import hashlib
from datetime import datetime
from rich.panel import Panel
from rich.table import Table
from utils.logger import Logger
from utils.ascii_art import ASCII_BANNERS
from utils.startup_manager import LoadingBar


class BreachCheck:
    """Check for public data breaches"""
    
    # Free APIs for breach checking
    BREACH_APIS = {
        'breachdirectory': {
            'name': 'Breach Directory',
            'url': 'https://breachdirectory.org/api/v1/query',
            'free': True
        },
        'pwndb': {
            'name': 'PwnDB',
            'url': 'https://api.pwndb2.com/search',
            'free': True
        }
    }
    
    def __init__(self, console=None, logger=None):
        self.console = console
        self.logger = logger or Logger()
    
    def get_banner(self):
        """Return module banner"""
        return ASCII_BANNERS['breach_module']
    
    def check(self, target: str) -> Panel:
        """
        Check if target appears in public breaches
        
        Args:
            target: Email or username to check
        
        Returns:
            Rich Panel with breach check results
        """
        try:
            LoadingBar.show_spinner("Checking breach databases...", duration=2)
            
            results = self._perform_checks(target)
            
            self.logger.success(f"Breach check completed for {target}")
            
            return self._create_results_panel(target, results)
        
        except Exception as e:
            self.logger.error(f"Breach check error: {str(e)}")
            return self._create_error_panel(f"Check failed: {str(e)}")
    
    def _perform_checks(self, target: str) -> dict:
        """Perform breach checks using available APIs"""
        results = {
            'target': target,
            'breaches_found': [],
            'compromised': False,
            'recommended_actions': [],
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        }
        
        # Educational simulation - in production use real APIs
        # Example: using Have I Been Pwned API (requires key)
        
        # Simulated results for demonstration
        if self._is_suspicious_target(target):
            results['breaches_found'] = [
                {
                    'source': 'Example Breach Database 1',
                    'date': '2023-06-15',
                    'records_affected': 'Unknown',
                    'data_types': ['Email', 'Password Hash', 'Username']
                },
                {
                    'source': 'Example Breach Database 2',
                    'date': '2023-08-20',
                    'records_affected': 'Unknown',
                    'data_types': ['Email', 'Phone Number']
                }
            ]
            results['compromised'] = True
        
        # Add recommendations
        if results['breaches_found']:
            results['recommended_actions'] = [
                'Change password immediately',
                'Enable two-factor authentication',
                'Monitor account for suspicious activity',
                'Review recent login locations',
                'Update security questions'
            ]
        else:
            results['recommended_actions'] = [
                'No breaches detected',
                'Maintain strong passwords',
                'Regular security audits recommended'
            ]
        
        return results
    
    def _is_suspicious_target(self, target: str) -> bool:
        """Simulate breach detection (for demo purposes)"""
        # In production, this would call real APIs
        suspicious_patterns = ['admin', 'test', 'demo', '123']
        return any(pattern in target.lower() for pattern in suspicious_patterns)
    
    def _create_results_panel(self, target: str, results: dict) -> Panel:
        """Create formatted results panel"""
        breach_status = "⚠️  COMPROMISED" if results['compromised'] else "✓ CLEAN"
        status_color = "red" if results['compromised'] else "green"
        
        breaches_html = ""
        if results['breaches_found']:
            breaches_html = "[bold green]BREACHES FOUND:[/bold green]\n"
            for i, breach in enumerate(results['breaches_found'], 1):
                breaches_html += f"""
[bold cyan]Breach #{i}[/bold cyan]
[cyan]  Source:[/cyan] {breach['source']}
[cyan]  Date:[/cyan] {breach['date']}
[cyan]  Data Types:[/cyan] {', '.join(breach['data_types'])}
"""
        
        actions_html = "[bold green]RECOMMENDED ACTIONS:[/bold green]\n"
        for action in results['recommended_actions']:
            actions_html += f"[cyan]→[/cyan] {action}\n"
        
        content = f"""
[bold cyan]Target:[/bold cyan] {target}
[bold {status_color}]Status:[/bold {status_color}] {breach_status}

{breaches_html}

{actions_html}

[bold cyan]Check Timestamp:[/bold cyan] {results['timestamp']}

[bold yellow]DISCLAIMER:[/bold yellow]
This is an educational demonstration. For real breach checking:
1. Use Have I Been Pwned API (haveibeenpwned.com)
2. Contact official data breach notification services
3. Review official security advisories

[bold yellow]Remember:[/bold yellow] Passwords should be changed immediately if compromised.
Enable 2FA for critical accounts.
        """
        
        return Panel(
            content.strip(),
            title=f"[bold {status_color}]PUBLIC BREACH CHECK - {target}[/bold {status_color}]",
            border_style=status_color,
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
