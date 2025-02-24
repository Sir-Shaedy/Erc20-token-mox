# pragma version 0.4.0
"""
@license MIT
@title snek_token
@notice This is my ERC20 token!
@author Sir...Shady
"""

# ------------------------------------------------------------------
#                             IMPORTS
# ------------------------------------------------------------------
from snekmate.auth import ownable
from snekmate.tokens import erc20
from ethereum.ercs import IERC20


# ------------------------------------------------------------------
#                            IMPLEMENTS
# ------------------------------------------------------------------
implements: IERC20


# ------------------------------------------------------------------
#                            INITIALIZE
# ------------------------------------------------------------------
initializes: ownable
initializes: erc20[ownable := ownable]


# ------------------------------------------------------------------
#                             EXPORTS
# ------------------------------------------------------------------
exports: (erc20.__interface__,)

NAME: constant(String[25]) = "Snek_token"
SYMBOL: constant(String[5]) = "SNEK"
DECIMALS: constant(uint8) = 18
NAME_EIP712: constant(String[50]) = "Snek_token"
EIP712_VERSION: constant(String[20]) = "1"


@deploy
def __init__(_initial_supply: uint256):
    ownable.__init__()
    erc20.__init__(NAME, SYMBOL, DECIMALS, NAME_EIP712, EIP712_VERSION)
    erc20._mint(msg.sender, _initial_supply)
