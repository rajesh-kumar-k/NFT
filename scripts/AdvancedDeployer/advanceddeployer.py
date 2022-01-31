from brownie import accounts, network, advancedNFT, config
from scripts.helpfulscript import deploy_mocks, fund_with_link, getaccount, OPENSEA_URL


def deployer():
    account = getaccount()
    advance_collectible = advancedNFT.deploy(
        config["networks"][network.show_active()]["vrfcoordinator"],
        config["networks"][network.show_active()]["link_token"],
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
    )
    print(advance_collectible.address)
    deploy_mocks()
    fund_with_link(advance_collectible.address)
    tx = advance_collectible.createAdvanced({"from": account})
    tx.wait(1)


def main():
    deployer()
