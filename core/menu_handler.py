"""
Main menu handler for Jasoos framework
"""

import time
import os
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from utils.terminal_designer import TerminalUI, HackerInput
from utils.logger import Logger
from modules.phone_intelligence import PhoneIntelligence
from modules.social_enumeration import SocialEnumeration
from modules.username_recon import UsernameRecon
from modules.email_intelligence import EmailIntelligence
from modules.geo_lookup import GeoLookup
from modules.breach_check import BreachCheck
from modules.report_generator import ReportGenerator


class MainMenuHandler:
    """Handles the main menu and navigation"""
    
    def __init__(self, console: Console = None, logger: Logger = None):
        self.console = console or Console()
        self.logger = logger or Logger()
        self.ui = TerminalUI(console=self.console)
        self.running = True
        
        # Initialize modules
        self.phone_intel = PhoneIntelligence(console=self.console, logger=self.logger)
        self.social_enum = SocialEnumeration(console=self.console, logger=self.logger)
        self.username_recon = UsernameRecon(console=self.console, logger=self.logger)
        self.email_intel = EmailIntelligence(console=self.console, logger=self.logger)
        self.geo_lookup = GeoLookup(console=self.console, logger=self.logger)
        self.breach_check = BreachCheck(console=self.console, logger=self.logger)
        self.report_gen = ReportGenerator(console=self.console, logger=self.logger)
        
        # Collected data for report generation
        self.investigation_data = {}
    
    def display_main_menu(self):
        """Display the main menu"""
        menu_content = """
[bold green][1][/bold green]  Phone Number Intelligence
[bold green][2][/bold green]  Social Media Enumeration
[bold green][3][/bold green]  Username Reconnaissance
[bold green][4][/bold green]  Email Intelligence
[bold green][5][/bold green]  Geo Metadata Lookup
[bold green][6][/bold green]  Public Breach Check
[bold green][7][/bold green]  Export Investigation Report
[bold cyan][0][/bold cyan]  Exit Framework

[bold cyan]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold cyan]
        """
        
        menu_panel = Panel(
            menu_content,
            title="[bold green]⚙️  MAIN CONTROL PANEL[/bold green]",
            border_style="green",
            style="dim white"
        )
        
        self.console.print(menu_panel)
    
    def handle_option_1(self):
        """Handle Phone Number Intelligence"""
        self.logger.section("PHONE NUMBER INTELLIGENCE")
        self.console.print(self.phone_intel.get_banner())
        
        phone_number = HackerInput.get_input(
            "Enter phone number (with country code, e.g., +1234567890): "
        )
        
        if phone_number:
            result = self.phone_intel.analyze(phone_number)
            self.investigation_data['phone'] = result
            self.console.print(result)
    
    def handle_option_2(self):
        """Handle Social Media Enumeration"""
        self.logger.section("SOCIAL MEDIA ENUMERATION")
        self.console.print(self.social_enum.get_banner())
        
        target = HackerInput.get_input("Enter phone number or username: ")
        
        if target:
            result = self.social_enum.enumerate(target)
            self.investigation_data['social'] = result
            self.console.print(result)
    
    def handle_option_3(self):
        """Handle Username Reconnaissance"""
        self.logger.section("USERNAME RECONNAISSANCE")
        self.console.print(self.username_recon.get_banner())
        
        username = HackerInput.get_input("Enter username to search: ")
        
        if username:
            result = self.username_recon.search(username)
            self.investigation_data['username'] = result
            self.console.print(result)
    
    def handle_option_4(self):
        """Handle Email Intelligence"""
        self.logger.section("EMAIL INTELLIGENCE")
        self.console.print(self.email_intel.get_banner())
        
        email = HackerInput.get_input("Enter email address: ")
        
        if email:
            result = self.email_intel.analyze(email)
            self.investigation_data['email'] = result
            self.console.print(result)
    
    def handle_option_5(self):
        """Handle Geo Metadata Lookup"""
        self.logger.section("GEO METADATA LOOKUP")
        self.console.print(self.geo_lookup.get_banner())
        
        phone_or_ip = HackerInput.get_input("Enter phone number or IP address: ")
        
        if phone_or_ip:
            result = self.geo_lookup.lookup(phone_or_ip)
            self.investigation_data['geo'] = result
            self.console.print(result)
    
    def handle_option_6(self):
        """Handle Public Breach Check"""
        self.logger.section("PUBLIC BREACH CHECK")
        self.console.print(self.breach_check.get_banner())
        
        target = HackerInput.get_input("Enter email or username for breach check: ")
        
        if target:
            result = self.breach_check.check(target)
            self.investigation_data['breach'] = result
            self.console.print(result)
    
    def handle_option_7(self):
        """Handle Report Generation"""
        self.logger.section("INVESTIGATION REPORT GENERATOR")
        self.console.print(self.report_gen.get_banner())
        
        if not self.investigation_data:
            self.ui.print_status(
                "WARNING",
                "No investigation data collected yet!",
                status_type="warning"
            )
            return
        
        report_format = HackerInput.get_input(
            "Select format (txt/json/html) [default: txt]: "
        ).lower() or "txt"
        
        filename = self.report_gen.generate(
            self.investigation_data,
            report_format=report_format
        )
        
        self.ui.print_status(
            "SUCCESS",
            f"Report exported to: {filename}",
            status_type="success"
        )
    
    def run(self):
        """Run the main menu loop"""
        menu_options = {
            '1': self.handle_option_1,
            '2': self.handle_option_2,
            '3': self.handle_option_3,
            '4': self.handle_option_4,
            '5': self.handle_option_5,
            '6': self.handle_option_6,
            '7': self.handle_option_7,
            '0': self.exit_framework,
        }
        
        while self.running:
            try:
                self.display_main_menu()
                
                choice = HackerInput.get_input("Enter your choice: ")
                
                if choice in menu_options:
                    self.console.clear()
                    menu_options[choice]()
                    input("\n[bold cyan]Press Enter to continue...[/bold cyan]")
                    self.console.clear()
                else:
                    self.ui.print_status(
                        "ERROR",
                        "Invalid option. Please try again.",
                        status_type="error"
                    )
                    time.sleep(1.5)
                    self.console.clear()
            
            except KeyboardInterrupt:
                self.console.clear()
                self.exit_framework()
            except Exception as e:
                self.logger.error(f"Menu error: {str(e)}")
                self.ui.print_status("ERROR", str(e), status_type="error")
                time.sleep(2)
                self.console.clear()
    
    def exit_framework(self):
        """Exit the framework gracefully"""
        self.console.clear()
        exit_message = """
[bold cyan]╔════════════════════════════════════════════╗[/bold cyan]
[bold cyan]║[/bold cyan]    [bold green]JASOOS FRAMEWORK SHUTDOWN[/bold green]         [bold cyan]║[/bold cyan]
[bold cyan]║[/bold cyan]    [bold yellow]Thank you for using Jasoos[/bold yellow]      [bold cyan]║[/bold cyan]
[bold cyan]║[/bold cyan]    [bold cyan]Educational Use Only[/bold cyan]           [bold cyan]║[/bold cyan]
[bold cyan]╚════════════════════════════════════════════╝[/bold cyan]
        """
        self.console.print(exit_message)
        self.logger.info("Framework shutdown gracefully")
        self.running = False
        time.sleep(1)
        os._exit(0)
