from errbot import BotPlugin, botcmd
from config import BAMBOO_URL, ATLASSIAN_USER, ATLASSIAN_PASSWORD

from atlassian import Bamboo

bamboo = Bamboo(url=BAMBOO_URL, username=ATLASSIAN_USER, password=ATLASSIAN_PASSWORD)

class BambooBot(BotPlugin):
    """
    This plugin can be used to interact with the Bamboo server API.
    """

    @botcmd
    def agent_status(self, msg, args):
        """
        Execute to check Bamboo agent status.
        """
        agent_status = bamboo.agent_status(online=True)
        return agent_status

    @botcmd
    def project_plans(self, msg, args):
        """
        Execute to check Bamboo agent status.
        """
        project_plans = bamboo.project_plans('EX')
        print(*project_plans, sep='\n')

    @botcmd  # flags a command
    def tryme(self, msg, args):  # a command callable with !tryme
        """
        Execute to check if Errbot responds to command.
        Feel free to tweak me to experiment with Errbot.
        You can find me in your init directory in the subdirectory plugins.
        """
        return "It *works* !"  # This string format is markdown.
