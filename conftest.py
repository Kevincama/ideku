

def pytest_addoption(parser):
    # Store info to choose testdata file
    parser.addoption(
        "--env", action="store", default="Debug", help="Test Env", choices=('debug', 'prod')
    )
    # Define the browser
    parser.addoption(
        "--browser", action="store", default="chrome", help="The browser which use to test", choices=('chrome', 'edge')
    )

