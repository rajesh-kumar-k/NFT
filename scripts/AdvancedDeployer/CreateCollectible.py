from brownie import advancedNFT, accounts
from scripts.helpfulscript import getaccount, fund_with_link
from web3 import Web3


def main():
    account = getaccount()
    advanced_collectible = advancedNFT[-1]
    fund_with_link(advanced_collectible.address, amount=Web3.toWei(0.1, "ether"))
    create_tx = advanced_collectible.createAdvanced({"from": account})
    create_tx.wait(1)
    print("collectible created")
    print(advanced_collectible.tokenCounter())
