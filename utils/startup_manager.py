"""
Startup sequence manager with Matrix-style effects and animated loading
"""

import time
import sys
from typing import Optional
from rich.console import Console
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.align import Align
from colorama import Fore, Style
import random


class StartupSequence:
    """Manages the cinematic startup sequence with Matrix effects"""
    
    def __init__(self, console: Console, logger=None):
        self.console = console
        self.logger = logger
        self.startup_messages = [
            "Initializing Jasoos Framework...",
            "Loading OSINT Modules...",
            "Connecting Intelligence Engine...",
            "Starting Recon Services...",
            "Accessing Public Intelligence Sources...",
            "Preparing Investigation Environment...",
            "Calibrating Neural Networks...",
            "Syncing Global Databases...",
            "Encrypting Communication Channels...",
            "System Status: ONLINE"
        ]
    
    def matrix_rain(self, duration: float = 2):
        """Display Matrix-style falling characters effect"""
        chars = "ｦｯｼ亜唖娃阿哀愛挨旭穴写九九九"
        width = 80
        height = 10
        
        start_time = time.time()
        while time.time() - start_time < duration:
            lines = []
            for _ in range(height):
                line = "".join(random.choices(chars, k=width))
                lines.append(f"[bold green]{line}[/bold green]")
            
            # Clear and print
            sys.stdout.flush()
            time.sleep(0.1)
    
    def typing_animation(self, text: str, speed: float = 0.02):
        """Animate text typing effect"""
        for char in text:
            sys.stdout.write(f"{Fore.GREEN}{char}{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(speed)
        sys.stdout.write("\n")
    
    def run_sequence(self):
        """Run the complete startup sequence"""
        self.console.clear()
        
        # Matrix rain effect
        self.console.print("[bold cyan]" + "=" * 80 + "[/bold cyan]")
        self.console.print("[bold green]INITIALIZING JASOOS OSINT FRAMEWORK[/bold green]")
        self.console.print("[bold cyan]" + "=" * 80 + "[/bold cyan]\n")
        
        time.sleep(0.5)
        
        # Animated startup messages with progress bar
        with Progress(
            SpinnerColumn(style="bold green"),
            TextColumn("[bold cyan]{task.description}[/bold cyan]"),
            BarColumn(bar_width=30, style="green"),
            transient=True
        ) as progress:
            task = progress.add_task("[bold green]Loading framework...", total=len(self.startup_messages))
            
            for message in self.startup_messages:
                time.sleep(0.3)
                self.console.print(f"[bold green]→[/bold green] {message}", soft_wrap=True)
                progress.update(task, advance=1)
                time.sleep(0.2)
        
        time.sleep(0.5)
        
        # System ready indicator
        self.console.print("\n[bold cyan]" + "=" * 80 + "[/bold cyan]")
        self.console.print("[bold green]✓ FRAMEWORK LOADED SUCCESSFULLY[/bold green]")
        self.console.print("[bold cyan]" + "=" * 80 + "[/bold cyan]\n")
        
        time.sleep(1)
        
        if self.logger:
            self.logger.info("Startup sequence completed successfully")


class LoadingBar:
    """Custom loading bar for module operations"""
    
    @staticmethod
    def show_progress(operation: str, duration: float = 2.0):
        """Display a progress bar for an operation"""
        with Progress(
            SpinnerColumn(style="bold green"),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(style="green", bar_width=20),
            transient=True
        ) as progress:
            task = progress.add_task(f"[bold cyan]{operation}[/bold cyan]", total=100)
            
            steps = 100
            for i in range(steps):
                time.sleep(duration / steps)
                progress.update(task, advance=1)
    
    @staticmethod
    def show_spinner(operation: str, duration: float = 1.5):
        """Display a spinner for an operation"""
        with Progress(
            SpinnerColumn(style="bold green"),
            TextColumn("[bold cyan]{task.description}[/bold cyan]"),
            transient=True
        ) as progress:
            task = progress.add_task(operation, total=None)
            time.sleep(duration)
