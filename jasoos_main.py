#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                    JASOOS BY SHAH-MIR - OSINT FRAMEWORK                   ║
║                  Advanced Cybersecurity Intelligence Tool                 ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

This framework is intended strictly for educational purposes,
authorized cybersecurity investigations, and OSINT research only.
Unauthorized or illegal use is strictly prohibited.
"""

import os
import sys
import time
import platform
import subprocess
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Import framework components
from utils.startup_manager import StartupSequence
from utils.terminal_designer import TerminalUI
from core.menu_handler import MainMenuHandler
from utils.ascii_art import ASCII_BANNERS
from utils.logger import Logger

# Colors and styling
from colorama import Fore, Back, Style
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

__version__ = "1.0.0"
__author__ = "Shah-Mir"
__project_type__ = "Educational OSINT Framework"

console = Console()
logger = Logger("JASOOS")


def display_ethical_warning():
    """Display ethical usage warning"""
    warning_text = """
    [!] ETHICAL USAGE WARNING [!]

    This framework is intended STRICTLY for:
    • Educational cybersecurity research
    • Authorized penetration testing engagements
    • Legal cybersecurity investigations
    
    ⚠️  UNAUTHORIZED USE IS ILLEGAL ⚠️
    
    Users are responsible for all actions taken with this tool.
    The author assumes NO liability for misuse.
    """
    
    warning_panel = Panel(
        warning_text,
        title="[bold red]⚠️  LEGAL NOTICE[/bold red]",
        border_style="red",
        style="bold red"
    )
    console.print(warning_panel)
    time.sleep(2)


def display_startup_header():
    """Display the main Jasoos banner and system information"""
    console.clear()
    
    # Display main banner
    banner_text = ASCII_BANNERS['jasoos_main']
    console.print(f"[bold cyan]{banner_text}[/bold cyan]")
    
    # System information panel
    system_info = f"""
[bold cyan]Version:[/bold cyan] {__version__}
[bold cyan]Python:[/bold cyan] {sys.version.split()[0]}
[bold cyan]OS:[/bold cyan] {platform.system()} {platform.release()}
[bold cyan]Architecture:[/bold cyan] {platform.machine()}
[bold cyan]Developer:[/bold cyan] Shah-Mir
[bold cyan]Mode:[/bold cyan] Intelligence Gathering
[bold cyan]Status:[/bold cyan] [bold green]ONLINE[/bold green]
[bold cyan]Project Type:[/bold cyan] {__project_type__}
    """
    
    info_panel = Panel(
        system_info,
        title="[bold green]SYSTEM INFO[/bold green]",
        border_style="green",
        style="dim white"
    )
    console.print(info_panel)


def main():
    """Main entry point with startup sequence"""
    try:
        # Clear terminal (FIXED - safer method)
        subprocess.run(['clear'] if os.name == 'posix' else ['cls'], check=False)
        
        # Display ethical warning
        display_ethical_warning()
        
        # Initialize startup sequence
        startup = StartupSequence(console=console, logger=logger)
        startup.run_sequence()
        
        # Display main header
        display_startup_header()
        
        # Initialize menu handler
        menu_handler = MainMenuHandler(console=console, logger=logger)
        
        # Run main loop
        menu_handler.run()
        
    except KeyboardInterrupt:
        console.print("\n[bold red][!] Framework interrupted by user[/bold red]")
        console.print("[yellow]Shutting down gracefully...[/yellow]")
        time.sleep(1)
        logger.info("Framework shutdown by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Critical error: {str(e)}")
        console.print(f"[bold red][!] FATAL ERROR: {str(e)}[/bold red]")
        sys.exit(1)


if __name__ == "__main__":
    main()