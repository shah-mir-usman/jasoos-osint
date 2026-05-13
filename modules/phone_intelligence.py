"""
Phone Number Intelligence Module
Analyzes international phone numbers for intelligence gathering
"""

import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from datetime import datetime
from rich.panel import Panel
from rich.table import Table
from utils.logger import Logger
from utils.ascii_art import ASCII_BANNERS, ICONS


class PhoneIntelligence:
    """Phone number analysis and intelligence gathering"""
    
    def __init__(self, console=None, logger=None):
        self.console = console
        self.logger = logger or Logger()
        self.analyzed_numbers = {}
    
    def get_banner(self):
        """Return module banner"""
        return ASCII_BANNERS['phone_module']
    
    def analyze(self, phone_number: str) -> Panel:
        """
        Analyze a phone number for intelligence
        
        Args:
            phone_number: International phone number (e.g., +1234567890)
        
        Returns:
            Rich Panel with analysis results
        """
        try:
            # Parse the phone number
            parsed = phonenumbers.parse(phone_number, None)
            
            # Validate
            if not phonenumbers.is_valid_number(parsed):
                return self._create_error_panel("Invalid phone number format")
            
            # Extract information
            country = geocoder.country_name_for_number(parsed, "en")
            region = geocoder.region_code_for_number(parsed)
            area_code = geocoder.description_for_number(parsed, "en")
            operator = carrier.name_for_number(parsed, "en")
            time_zones = timezone.time_zones_for_number(parsed)
            line_type = self._get_line_type(parsed)
            
            # Create data dictionary
            data = {
                'phone_number': phone_number,
                'country': country,
                'region_code': region,
                'area': area_code if area_code else "N/A",
                'timezone': time_zones[0] if time_zones else "Unknown",
                'carrier': operator if operator else "Unknown",
                'line_type': line_type,
                'valid': "✓ YES",
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
            }
            
            self.analyzed_numbers[phone_number] = data
            self.logger.success(f"Phone analysis completed for {phone_number}")
            
            return self._create_result_panel(data)
        
        except phonenumbers.NumberParseException as e:
            return self._create_error_panel(f"Parse error: {str(e)}")
        except Exception as e:
            self.logger.error(f"Phone analysis error: {str(e)}")
            return self._create_error_panel(f"Analysis failed: {str(e)}")
    
    def _get_line_type(self, parsed_number) -> str:
        """Determine the line type (mobile/fixed/voip)"""
        try:
            from phonenumbers import number_type
            types = {
                number_type.FIXED_LINE: "Fixed Line",
                number_type.MOBILE: "Mobile",
                number_type.FIXED_LINE_OR_MOBILE: "Fixed Line/Mobile",
                number_type.TOLL_FREE: "Toll Free",
                number_type.PREMIUM_RATE: "Premium Rate",
                number_type.SHARED_COST: "Shared Cost",
                number_type.VOIP: "VoIP",
                number_type.PERSONAL_NUMBER: "Personal Number",
                number_type.PAGER: "Pager",
                number_type.UAN: "UAN",
                number_type.VOICEMAIL: "Voicemail",
                number_type.UNKNOWN: "Unknown"
            }
            line_type = number_type.number_type(parsed_number)
            return types.get(line_type, "Unknown")
        except:
            return "Unknown"
    
    def _create_result_panel(self, data: dict) -> Panel:
        """Create a formatted result panel"""
        content = f"""
[bold cyan]Phone Number:[/bold cyan] {data['phone_number']}
[bold cyan]Valid:[/bold cyan] {data['valid']}

[bold green]LOCATION INTELLIGENCE[/bold green]
[bold cyan]Country:[/bold cyan] {data['country']}
[bold cyan]Region Code:[/bold cyan] {data['region_code']}
[bold cyan]Area/City:[/bold cyan] {data['area']}
[bold cyan]Timezone:[/bold cyan] {data['timezone']}

[bold green]NETWORK INFORMATION[/bold green]
[bold cyan]Carrier/Operator:[/bold cyan] {data['carrier']}
[bold cyan]Line Type:[/bold cyan] {data['line_type']}

[bold green]METADATA[/bold green]
[bold cyan]Analysis Timestamp:[/bold cyan] {data['timestamp']}
[bold yellow]Note: Location based on country/region only. No real-time tracking.[/bold yellow]
        """
        
        return Panel(
            content.strip(),
            title="[bold green]✓ PHONE INTELLIGENCE REPORT[/bold green]",
            border_style="green",
            style="dim white"
        )
    
    def _create_error_panel(self, error_msg: str) -> Panel:
        """Create an error panel"""
        return Panel(
            f"[bold red]✗ {error_msg}[/bold red]",
            title="[bold red]ERROR[/bold red]",
            border_style="red",
            style="dim white"
        )
