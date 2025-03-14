from pytest import mark


def test_environment_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == "https://mydev-env.com"
    assert port == 8080


# @mark.skip(reason="Broken by deploy #448")
@mark.xfail(reason="This is a QA environment")
def test_environment_is_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == "https://myqa-env.com"
    assert port == 80


# @mark.skip(reason="This is a staging environment")
def test_environment_is_staging(app_config):
    base_url = app_config.base_url
    assert base_url == "staging"


# pytest --env=dev
# pytest --env=staging