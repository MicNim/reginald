import logging
import os

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Slack'  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_IDENTITY = {
  'token': '' # REQUIRED: add new token here https://www.youtube.com/watch?v=ImEYYI25Nxg
}


# Change these paths
BOT_DATA_DIR = r'/Users/samholden/Git/reginald/data' 
BOT_EXTRA_PLUGIN_DIR = r'/Users/samholden/Git/reginald/plugins'

BOT_LOG_FILE = r'/Users/samholden/Git/reginald/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('@holdens.uk', )  # !! Don't leave that to "@CHANGE_ME" if you connect your errbot to a chat system !!

# Bamboo Configuration
BAMBOO_URL = os.environ.get("BAMBOO_URL", "http://localhost:8085")
ATLASSIAN_USER = os.environ.get("ATLASSIAN_USER", "bamboo")
ATLASSIAN_PASSWORD = os.environ.get("ATLASSIAN_PASSWORD", "bamboo")