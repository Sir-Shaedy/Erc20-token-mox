import pytest
from script.deploy import deploy
from script.deploy_ownable import deploy_ownable


@pytest.fixture(scope="session")
def snek_contract():
    return deploy()


@pytest.fixture(scope="session")
def ownable_contract():
    return deploy_ownable()
