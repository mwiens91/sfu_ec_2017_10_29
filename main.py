#!/usr/bin/env python3
"""Safetrain v9.0"""

from safetrain import logging
from safetrain import controller
from safetrain import train

def main():
    """Main function for Safetrain."""
    initialize_log()
    logger = logging.getLogger('safetrain')

if __name__ == '__main__':
    main()
