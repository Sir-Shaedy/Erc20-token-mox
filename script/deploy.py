from src import snek_token
from eth_utils import to_wei

INITIAL_SUPPLY = to_wei(1000, "ether")


def deploy():
    snek_contract = snek_token.deploy(INITIAL_SUPPLY)
    print(f"SNEK contract deployed to: {snek_contract.address}")
    return snek_contract


def moccasin_main():
    return deploy()
