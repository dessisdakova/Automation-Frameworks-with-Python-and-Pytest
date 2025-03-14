# STEP 1: Create a class with configuration for desired environments.

class Config:
    """A class representing configuration based on the environment."""

    def __init__(self, env):
        self.base_url = {
            "dev": "https://mydev-env.com",
            "qa": "https://myqa-env.com"
        }[env]

        self.app_port = {
            "dev": 8080,
            "qa": 80
        }[env]