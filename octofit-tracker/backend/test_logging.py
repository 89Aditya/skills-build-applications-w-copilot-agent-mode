import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("/workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/logs/debug.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Test logging
logger.debug("This is a test log entry.")