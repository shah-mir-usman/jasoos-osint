"""
Social Media Enumeration Module
Searches for accounts across multiple platforms
"""

import asyncio
import aiohttp
from datetime import datetime
from rich.panel import Panel
from rich.table import Table
from utils.logger import Logger
from utils.ascii_art import ASCII_BANNERS
from utils.startup_manager import LoadingBar


class SocialEnumeration:
    """Social media account enumeration"""
    
    # Platform configurations
    PLATFORMS = {
        'telegram': {
            'url': 'https://t.me/{target}',
            'check_method': 'direct',
            'description': 'Telegram'
        },
        'instagram': {
            'url': 'https://instagram.com/{target}',
            'check_method': 'api',
            'description': 'Instagram'
        },
        'facebook': {
            'url': 'https://facebook.com/{target}',
            'check_method': 'direct',
            'description': 'Facebook'
        },
        'twitter': {
            'url': 'https://twitter.com/{target}',
            'check_method': 'api',
            'description': 'Twitter/X'
        },
        'github': {
            'url': 'https://github.com/{target}',
            'check_method': 'api',
            'description': 'GitHub'
        },
        'linkedin': {
            'url': 'https://linkedin.com/in/{target}',
            'check_method': 'direct',
            'description': 'LinkedIn'
        },
        'snapchat': {
            'url': 'https://snapchat.com/add/{target}',
            'check_method': 'direct',
            'description': 'Snapchat'
        },
        'youtube': {
            'url': 'https://youtube.com/@{target}',
            'check_method': 'direct',
            'description': 'YouTube'
        },
        'tiktok': {
            'url': 'https://tiktok.com/@{target}',
            'check_method': 'direct',
            'description': 'TikTok'
        },
        'reddit': {
            'url': 'https://reddit.com/user/{target}',
            'check_method': 'api',
            'description': 'Reddit'
        },
    }
    
    def __init__(self, console=None, logger=None):
        self.console = console
        self.logger = logger or Logger()
        self.found_accounts = []
        self.timeout = aiohttp.ClientTimeout(total=10)
    
    def get_banner(self):
        """Return module banner"""
        return ASCII_BANNERS['social_module']
    
    def enumerate(self, target: str) -> Panel:
        """
        Enumerate social media accounts for a target
        
        Args:
            target: Username or phone number to search
        
        Returns:
            Rich Panel with enumeration results
        """
        try:
            LoadingBar.show_spinner(f"Searching for {target} across platforms...", duration=2)
            
            # Run async enumeration
            results = asyncio.run(self._async_enumerate(target))
            
            self.logger.success(f"Social enumeration completed for {target}")
            
            return self._create_results_panel(target, results)
        
        except Exception as e:
            self.logger.error(f"Social enumeration error: {str(e)}")
            return self._create_error_panel(f"Enumeration failed: {str(e)}")
    
    async def _async_enumerate(self, target: str) -> list:
        """Asynchronously search for accounts"""
        results = []
        
        tasks = [
            self._check_platform(platform, target, config)
            for platform, config in self.PLATFORMS.items()
        ]
        
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        
        for response in responses:
            if isinstance(response, dict):
                results.append(response)
        
        return results
    
    async def _check_platform(self, platform: str, target: str, config: dict) -> dict:
        """Check if account exists on a platform"""
        try:
            url = config['url'].format(target=target)
            
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                try:
                    async with session.head(url, allow_redirects=True, ssl=False) as resp:
                        found = resp.status in [200, 301, 302, 404]  # Account may exist
                        
                        return {
                            'platform': config['description'],
                            'url': url,
                            'status': resp.status,
                            'found': found,
                            'timestamp': datetime.now().isoformat()
                        }
                except:
                    return {
                        'platform': config['description'],
                        'url': url,
                        'status': 'timeout',
                        'found': False,
                        'timestamp': datetime.now().isoformat()
                    }
        except Exception as e:
            return {
                'platform': platform,
                'error': str(e),
                'found': False
            }
    
    def _create_results_panel(self, target: str, results: list) -> Panel:
        """Create formatted results panel"""
        # Create table
        table = Table(title="Social Media Enumeration Results", style="cyan")
        table.add_column("Platform", style="bold cyan")
        table.add_column("Status", style="bold green")
        table.add_column("URL", style="blue")
        
        found_count = 0
        for result in results:
            if 'error' not in result:
                status = "✓ FOUND" if result['found'] else "✗ Not Found"
                status_color = "green" if result['found'] else "red"
                table.add_row(
                    result['platform'],
                    f"[bold {status_color}]{status}[/bold {status_color}]",
                    result['url']
                )
                if result['found']:
                    found_count += 1
        
        content = f"""
[bold cyan]Target:[/bold cyan] {target}
[bold cyan]Total Platforms Checked:[/bold cyan] {len(results)}
[bold green]Accounts Found:[/bold green] {found_count}
[bold cyan]Scan Timestamp:[/bold cyan] {datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")}

{self.console.render_str(str(table))}

[bold yellow]Note: This is enumeration only. Verify accounts through direct access.[/bold yellow]
        """
        
        return Panel(
            content.strip(),
            title=f"[bold green]✓ SOCIAL MEDIA ENUMERATION - {target}[/bold green]",
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
