def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """
    import os

    # if no environment vars have been set, load the dev.host.env file
    # to allow running test in the host environment instead of the container
    if "ENVIRONMENT" not in os.environ:
        import dotenv

        dotenv.load_dotenv("dev.host.env")
