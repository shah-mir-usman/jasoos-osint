"""
Username Reconnaissance Module
Searches usernames across multiple public websites (Sherlock-style)
"""

import asyncio
import aiohttp
from datetime import datetime
from rich.panel import Panel
from rich.table import Table
from utils.logger import Logger
from utils.ascii_art import ASCII_BANNERS
from utils.startup_manager import LoadingBar


class UsernameRecon:
    """Username reconnaissance across platforms"""
    
    # Comprehensive platform list (Sherlock-style)
    PLATFORMS = {
        'github': {'url': 'https://api.github.com/users/{username}', 'method': 'json'},
        'twitter': {'url': 'https://twitter.com/{username}', 'method': 'status'},
        'instagram': {'url': 'https://instagram.com/{username}', 'method': 'status'},
        'facebook': {'url': 'https://facebook.com/{username}', 'method': 'status'},
        'linkedin': {'url': 'https://linkedin.com/in/{username}', 'method': 'status'},
        'youtube': {'url': 'https://youtube.com/@{username}', 'method': 'status'},
        'reddit': {'url': 'https://reddit.com/user/{username}', 'method': 'status'},
        'tumblr': {'url': 'https://{username}.tumblr.com', 'method': 'status'},
        'pinterest': {'url': 'https://pinterest.com/{username}', 'method': 'status'},
        'tiktok': {'url': 'https://tiktok.com/@{username}', 'method': 'status'},
        'snapchat': {'url': 'https://snapchat.com/add/{username}', 'method': 'status'},
        'twitch': {'url': 'https://twitch.tv/{username}', 'method': 'status'},
        'steam': {'url': 'https://steamcommunity.com/search/users/{username}', 'method': 'status'},
        'minecraft': {'url': 'https://namemc.com/profile/{username}', 'method': 'status'},
        'roblox': {'url': 'https://roblox.com/user.aspx?username={username}', 'method': 'status'},
        'discord': {'url': 'https://discord.com/users/{username}', 'method': 'status'},
        'telegram': {'url': 'https://t.me/{username}', 'method': 'status'},
        'flickr': {'url': 'https://flickr.com/photos/{username}', 'method': 'status'},
        'medium': {'url': 'https://medium.com/@{username}', 'method': 'status'},
        'dev.to': {'url': 'https://dev.to/{username}', 'method': 'status'},
    }
    
    def __init__(self, console=None, logger=None):
        self.console = console
        self.logger = logger or Logger()
        self.timeout = aiohttp.ClientTimeout(total=8)
    
    def get_banner(self):
        """Return module banner"""
        return ASCII_BANNERS['username_module']
    
    def search(self, username: str) -> Panel:
        """
        Search for username across platforms
        
        Args:
            username: Username to search for
        
        Returns:
            Rich Panel with search results
        """
        try:
            LoadingBar.show_spinner(f"Searching for username: {username}...", duration=2)
            
            # Run async search
            results = asyncio.run(self._async_search(username))
            
            self.logger.success(f"Username search completed for {username}")
            
            return self._create_results_panel(username, results)
        
        except Exception as e:
            self.logger.error(f"Username search error: {str(e)}")
            return self._create_error_panel(f"Search failed: {str(e)}")
    
    async def _async_search(self, username: str) -> list:
        """Asynchronously search across platforms"""
        results = []
        
        tasks = [
            self._check_username(platform, username, config)
            for platform, config in self.PLATFORMS.items()
        ]
        
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        
        for response in responses:
            if isinstance(response, dict) and 'error' not in response:
                results.append(response)
        
        return sorted(results, key=lambda x: x['found'], reverse=True)
    
    async def _check_username(self, platform: str, username: str, config: dict) -> dict:
        """Check if username exists on platform"""
        try:
            url = config['url'].format(username=username)
            
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                try:
                    async with session.head(url, allow_redirects=True, ssl=False) as resp:
                        found = resp.status in [200, 301, 302]
                        
                        return {
                            'platform': platform.upper(),
                            'url': url,
                            'status_code': resp.status,
                            'found': found,
                            'timestamp': datetime.now().isoformat()
                        }
                except asyncio.TimeoutError:
                    return {
                        'platform': platform.upper(),
                        'url': url,
                        'status_code': 'TIMEOUT',
                        'found': False,
                        'timestamp': datetime.now().isoformat()
                    }
                except Exception:
                    return {
                        'platform': platform.upper(),
                        'url': url,
                        'status_code': 'ERROR',
                        'found': False,
                        'timestamp': datetime.now().isoformat()
                    }
        except Exception as e:
            return {'error': str(e)}
    
    def _create_results_panel(self, username: str, results: list) -> Panel:
        """Create formatted results panel"""
        # Create table
        table = Table(title="Username Search Results", style="cyan")
        table.add_column("Platform", style="bold cyan", width=15)
        table.add_column("Status", style="bold green", width=15)
        table.add_column("URL", style="blue")
        
        found_count = sum(1 for r in results if r['found'])
        
        for result in results:
            status = "✓ FOUND" if result['found'] else "✗ Not Found"
            status_color = "green" if result['found'] else "red"
            
            table.add_row(
                result['platform'],
                f"[bold {status_color}]{status}[/bold {status_color}]",
                result['url']
            )
        
        content = f"""
[bold cyan]Username:[/bold cyan] {username}
[bold cyan]Platforms Checked:[/bold cyan] {len(results)}
[bold green]Profiles Found:[/bold green] {found_count}
[bold cyan]Scan Timestamp:[/bold cyan] {datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")}

{self.console.render_str(str(table))}

[bold yellow]Note: False positives possible. Verify findings manually.[/bold yellow]
        """
        
        return Panel(
            content.strip(),
            title=f"[bold green]✓ USERNAME RECONNAISSANCE - {username}[/bold green]",
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
