"""
Logger utility for Jasoos framework
"""

import os
import logging
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.logging import RichHandler


class Logger:
    """Custom logger for the framework"""
    
    def __init__(self, name: str = "JASOOS"):
        self.name = name
        self.console = Console()
        
        # Create logs directory if not exists
        self.log_dir = Path("./logs")
        self.log_dir.mkdir(exist_ok=True)
        
        # Setup logging
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        # File handler
        log_file = self.log_dir / f"jasoos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        
        # Console handler with rich formatting
        console_handler = RichHandler(console=self.console, rich_tracebacks=True)
        console_handler.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        
        # Add handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def info(self, message: str):
        """Log info message"""
        self.logger.info(f"[ℹ️ ] {message}")
    
    def success(self, message: str):
        """Log success message"""
        self.console.print(f"[bold green]✓ {message}[/bold green]")
        self.logger.info(message)
    
    def error(self, message: str):
        """Log error message"""
        self.logger.error(f"[✗] {message}")
    
    def warning(self, message: str):
        """Log warning message"""
        self.logger.warning(f"[⚠️ ] {message}")
    
    def debug(self, message: str):
        """Log debug message"""
        self.logger.debug(f"[🐛] {message}")
    
    def section(self, title: str):
        """Log a section header"""
        self.console.print(f"\n[bold cyan]{'═' * 60}[/bold cyan]")
        self.console.print(f"[bold green]{title}[/bold green]")
        self.console.print(f"[bold cyan]{'═' * 60}[/bold cyan]\n")
