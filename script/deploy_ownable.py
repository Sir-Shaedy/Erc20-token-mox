from lib.pypi.snekmate.auth import ownable


def deploy_ownable():
    erc20_contract = ownable.deploy()
    print(f"Deploying erc20 at {erc20_contract.address}")
    return erc20_contract


def moccasin():
    return deploy_ownable()
