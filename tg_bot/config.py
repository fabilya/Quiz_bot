import os
import logging

from dotenv import load_dotenv

load_dotenv()

"""Logging levels"""
DEBUG = os.getenv('DEBUG')

"""Tokens"""
BOT_TOKEN = os.getenv('BOT_TOKEN')


logging.basicConfig(level=logging.INFO)
