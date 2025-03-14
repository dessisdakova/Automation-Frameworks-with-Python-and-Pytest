from pytest import fixture

from config import Config


# STEP 2: Create a function that adds the custom option to the command line.
# using argparse library - passing arguments from the console will change how the program works
def pytest_addoption(parser):
    """
    This function is called by pytest to add custom command-line options.
    It adds the '--env' option, allowing the user to specify the environment
    for the tests (e.g., 'qa', 'prod').
    """
    parser.addoption("--env",
                     # The value for '--env' will be stored
                     action="store",
                     # Description which can be viewed using -h marker for pytest
                     help="Environment to run tests against")


# STEP 3: Create a fixture that retrieves the selected environment from the console.
@fixture(scope="session")
def env(request):
    """
    Fixture to retrieve the value of the '--env' command-line option.
    This makes the environment available in the tests.
    The value is obtained using request.config.getoption() method.
    """
    return request.config.getoption("--env")


# STEP 4: Create a fixture that returns an instance of the Config class
# with the selected environment and use it in tests
@fixture(scope="session")
def app_config(env):
    """
    Fixture to create and provide the app configuration based on the environment.
    It uses the 'env' fixture to initialize the 'Config' class with the selected environment.
    This allows the configuration to be used in tests.
    """
    return Config(env)  # Return Config instance
