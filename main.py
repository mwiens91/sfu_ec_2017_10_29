#!/usr/bin/env python3
"""Safetrain v9.0"""
import logging
from safetrain import logger
from safetrain import GUI
from safetrain import controller
from safetrain import train

def main():
    """Main function for Safetrain."""
    logger.initialize_log()
    safetrain_log = logging.getLogger('safetrain')
    
    app = GUI.Application()
    app.master.title('Safe Train V9.0')
    app.mainloop()

if __name__ == '__main__':
    main()
