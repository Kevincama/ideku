import os
import json

import pytest


@pytest.fixture(autouse=False)
def load_test_data(request):
    file_name = request.param
    env  = request.config.getoption("--env").lower()
    directory_path = f"testdata/{env}"
    file_path = os.path.join(directory_path, file_name)

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                return json.load(file)
            except Exception as e:
                raise Exception(f"File:{file} format is error, Exception :{e}")
    else:
        raise FileNotFoundError(f"TestData is not exist.")

