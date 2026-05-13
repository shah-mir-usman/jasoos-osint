"""
Terminal UI designer with hacker-style panels and animations
"""

import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich.layout import Layout
from colorama import Fore, Style
import sys


class TerminalUI:
    """Advanced terminal UI with hacker aesthetics"""
    
    # Color scheme
    PRIMARY_COLOR = "cyan"
    ACCENT_COLOR = "green"
    WARNING_COLOR = "yellow"
    ERROR_COLOR = "red"
    
    # Border styles
    BORDER_SOLID = "thick"
    BORDER_DOUBLE = "double"
    BORDER_ROUNDED = "rounded"
    
    def __init__(self, console: Console = None):
        self.console = console or Console()
    
    def create_panel(self, content: str, title: str = "", 
                     border_style: str = "cyan", style: str = "dim white") -> Panel:
        """Create a styled panel"""
        return Panel(
            content,
            title=f"[bold {border_style}]{title}[/bold {border_style}]" if title else "",
            border_style=border_style,
            style=style,
            padding=(1, 2)
        )
    
    def create_menu_panel(self, items: list, title: str = "MENU") -> str:
        """Create a formatted menu panel"""
        menu_text = f"[bold {self.ACCENT_COLOR}]{title}[/bold {self.ACCENT_COLOR}]\n\n"
        
        for item in items:
            menu_text += f"[bold cyan]{item}[/bold cyan]\n"
        
        return menu_text
    
    def create_table(self, headers: list, rows: list = None) -> Table:
        """Create a styled data table"""
        table = Table(title="", style="cyan", border_style="green")
        
        for header in headers:
            table.add_column(header, style="bold cyan")
        
        if rows:
            for row in rows:
                table.add_row(*row, style="white")
        
        return table
    
    def divider(self, char: str = "═", length: int = 80) -> str:
        """Create a styled divider"""
        return f"[bold cyan]{char * length}[/bold cyan]"
    
    def typing_print(self, text: str, speed: float = 0.02, color: str = "green"):
        """Print text with typing animation"""
        for char in text:
            sys.stdout.write(f"{Fore.GREEN if color == 'green' else Fore.CYAN}{char}{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(speed)
        sys.stdout.write("\n")
    
    def print_status(self, status: str, message: str, status_type: str = "info"):
        """Print a status message"""
        status_colors = {
            "success": "green",
            "error": "red",
            "warning": "yellow",
            "info": "cyan"
        }
        
        color = status_colors.get(status_type, "white")
        self.console.print(f"[bold {color}][{status}][/bold {color}] {message}")
    
    def print_header(self, text: str):
        """Print a styled header"""
        self.console.print(f"\n[bold cyan]{'═' * 80}[/bold cyan]")
        self.console.print(f"[bold green]{text}[/bold green]")
        self.console.print(f"[bold cyan]{'═' * 80}[/bold cyan]\n")
    
    def print_separator(self):
        """Print a separator line"""
        self.console.print(f"[bold cyan]{'-' * 80}[/bold cyan]")
    
    def create_data_display(self, data_dict: dict, title: str = "DATA") -> Panel:
        """Create a panel displaying key-value data"""
        content = ""
        for key, value in data_dict.items():
            content += f"[bold cyan]{key}:[/bold cyan] {value}\n"
        
        return self.create_panel(content.strip(), title=title, border_style="green")


class HackerInput:
    """Get user input with hacker-style prompts"""
    
    @staticmethod
    def get_input(prompt: str = "> ", show_cursor: bool = True) -> str:
        """Get user input with custom prompt"""
        prompt_text = f"[bold green]{prompt}[/bold green]"
        return input(prompt_text)
    
    @staticmethod
    def get_choice(prompt: str = "Select option", choices: list = None) -> str:
        """Get a choice from user"""
        if choices:
            choices_text = " | ".join([f"[bold cyan]{c}[/bold cyan]" for c in choices])
            prompt = f"{prompt} [{choices_text}]"
        
        return HackerInput.get_input(prompt)


class TerminalEffects:
    """Special terminal effects and animations"""
    
    @staticmethod
    def flash_message(console: Console, message: str, times: int = 3, delay: float = 0.2):
        """Flash a message on/off"""
        for _ in range(times):
            console.print(f"[bold red]{message}[/bold red]", end="\r")
            time.sleep(delay)
            console.print(" " * len(message), end="\r")
            time.sleep(delay)
        console.print(f"[bold red]{message}[/bold red]")
    
    @staticmethod
    def success_animation(console: Console):
        """Show success animation"""
        console.print("[bold green]✓ SUCCESS[/bold green]")
        time.sleep(0.5)
    
    @staticmethod
    def loading_dots(console: Console, message: str = "Processing", duration: float = 2.0):
        """Show loading animation with dots"""
        start = time.time()
        while time.time() - start < duration:
            for dots in [".", "..", "..."]:
                console.print(f"[bold cyan]{message}{dots}[/bold cyan]", end="\r")
                time.sleep(0.3)
