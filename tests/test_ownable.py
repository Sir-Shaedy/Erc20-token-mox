import boa

RANDOM_USER = boa.env.generate_address("random_user")
RANDOM_USER_TWO = boa.env.generate_address("random_user")


def test_transfer_ownership(ownable_contract):
    with boa.env.prank(ownable_contract.owner()):
        ownable_contract.transfer_ownership(RANDOM_USER)

    assert ownable_contract.owner() == RANDOM_USER


def test_renounce_ownership(ownable_contract):
    with boa.env.prank(ownable_contract.owner()):
        ownable_contract.renounce_ownership()
