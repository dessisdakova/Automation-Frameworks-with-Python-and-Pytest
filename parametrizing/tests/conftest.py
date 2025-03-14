import json

from pytest import fixture


test_data_file_path = "test_data.json"

def load_test_data(path):
    """Load test data."""
    with open(path) as data_file:
        data = json.load(data_file)
        return data


@fixture(params=load_test_data(test_data_file_path))
def tv_brand(request):
    """Fixture that returns the data and parametrize it."""
    return request.param



