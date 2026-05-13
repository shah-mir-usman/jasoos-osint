"""
Geo Metadata Lookup Module
Provides telecom and metadata-based geographic information
Educational and legal use only - NO live tracking/surveillance
"""

import phonenumbers
from phonenumbers import geocoder, timezone, carrier
from datetime import datetime
from rich.panel import Panel
from rich.table import Table
from utils.logger import Logger
from utils.ascii_art import ASCII_BANNERS
from utils.startup_manager import LoadingBar


class GeoLookup:
    """Geographic metadata lookup"""
    
    def __init__(self, console=None, logger=None):
        self.console = console
        self.logger = logger or Logger()
    
    def get_banner(self):
        """Return module banner"""
        return ASCII_BANNERS['geo_module']
    
    def lookup(self, target: str) -> Panel:
        """
        Lookup geographic metadata for phone number or IP
        
        Args:
            target: Phone number or IP address
        
        Returns:
            Rich Panel with metadata results
        """
        try:
            LoadingBar.show_spinner("Looking up metadata...", duration=1)
            
            # Try as phone number first
            if target.startswith('+') or target[0].isdigit():
                return self._lookup_phone_geo(target)
            else:
                return self._create_error_panel("Please provide phone number with country code")
        
        except Exception as e:
            self.logger.error(f"Geo lookup error: {str(e)}")
            return self._create_error_panel(f"Lookup failed: {str(e)}")
    
    def _lookup_phone_geo(self, phone_number: str) -> Panel:
        """Lookup geographic metadata for phone number"""
        try:
            # Parse phone number
            parsed = phonenumbers.parse(phone_number, None)
            
            if not phonenumbers.is_valid_number(parsed):
                return self._create_error_panel("Invalid phone number")
            
            # Gather metadata
            country = geocoder.country_name_for_number(parsed, "en")
            country_code = geocoder.region_code_for_number(parsed)
            area_description = geocoder.description_for_number(parsed, "en")
            time_zones = timezone.time_zones_for_number(parsed)
            operator = carrier.name_for_number(parsed, "en")
            
            # Compile metadata
            metadata = {
                'phone_number': phone_number,
                'country': country,
                'country_code': country_code,
                'region': area_description if area_description else "N/A",
                'timezone': time_zones[0] if time_zones else "Unknown",
                'operator': operator if operator else "Unknown",
                'provider_region': self._get_provider_region(country),
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
            }
            
            self.logger.success(f"Geo lookup completed for {phone_number}")
            
            return self._create_results_panel(metadata)
        
        except phonenumbers.NumberParseException:
            return self._create_error_panel("Invalid phone number format")
        except Exception as e:
            return self._create_error_panel(f"Analysis failed: {str(e)}")
    
    def _get_provider_region(self, country: str) -> str:
        """Get telecom provider region information"""
        # Simplified provider region mapping
        regions = {
            'United States': 'North America',
            'Canada': 'North America',
            'Mexico': 'North America',
            'United Kingdom': 'Europe',
            'Germany': 'Europe',
            'France': 'Europe',
            'China': 'Asia',
            'India': 'Asia',
            'Japan': 'Asia',
            'Australia': 'Oceania',
            'Pakistan': 'South Asia',
            'Brazil': 'South America',
        }
        return regions.get(country, 'International')
    
    def _create_results_panel(self, metadata: dict) -> Panel:
        """Create formatted results panel"""
        content = f"""
[bold cyan]Phone Number:[/bold cyan] {metadata['phone_number']}

[bold green]GEOGRAPHIC INFORMATION[/bold green]
[bold cyan]Country:[/bold cyan] {metadata['country']}
[bold cyan]Country Code:[/bold cyan] {metadata['country_code']}
[bold cyan]Region/Area:[/bold cyan] {metadata['region']}
[bold cyan]Provider Region:[/bold cyan] {metadata['provider_region']}

[bold green]NETWORK INFORMATION[/bold green]
[bold cyan]Timezone:[/bold cyan] {metadata['timezone']}
[bold cyan]Operator:[/bold cyan] {metadata['operator']}

[bold green]METADATA DETAILS[/bold green]
[bold cyan]Analysis Timestamp:[/bold cyan] {metadata['timestamp']}

[bold cyan]╔════════════════════════════════════════════╗[/bold cyan]
[bold cyan]║  IMPORTANT: EDUCATIONAL USE ONLY          ║[/bold cyan]
[bold cyan]║  This provides country/region level data  ║[/bold cyan]
[bold cyan]║  NO real-time location tracking           ║[/bold cyan]
[bold cyan]║  NO GPS/surveillance capabilities         ║[/bold cyan]
[bold cyan]╚════════════════════════════════════════════╝[/bold cyan]

[bold yellow]Note: Data based on telecom registrations only.
Based on public databases and country/region assignment.[/bold yellow]
        """
        
        return Panel(
            content.strip(),
            title="[bold green]✓ GEO METADATA REPORT[/bold green]",
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
