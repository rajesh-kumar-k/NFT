from brownie import accounts, network, config, Contract, LinkToken
from web3 import Web3

OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"
deven = ["development", "Ganache-Local"]
breeder = {0: "BlindedPink", 1: "PurpleBlast", 2: "Yellove"}


def breed(number):
    return breeder[number]


def getaccount(index=None, id=None):
    if id:
        return accounts.load(id)
    if index:
        return accounts[index]
    if network.show_active() in deven:
        return accounts[0]

    return accounts.add(config["Wallets"]["from_key"])


contract_to_mock = {
    "link_token": LinkToken,
}


def get_contract(contract_name):
    contract_type = contract_to_mock[contract_name]
    if network.show_active() in deven:
        if len(contract_type) <= 0:
            deploy_mocks()
        contract = contract_type[-1]

    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        contract = Contract.from_abi(
            contract_type._name, contract_address, contract_type.abi
        )
    return contract


def deploy_mocks():
    account = getaccount()
    link_token = LinkToken.deploy({"from": account})
    print("Deployed!")


def fund_with_link(
    contract_address, account=None, link_token=None, amount=100000000000000000
):  # 0.1 LINK
    account = account if account else getaccount()
    link_token = link_token if link_token else get_contract("link_token")
    print(f"i think same one{link_token}")
    tx = link_token.transfer(contract_address, amount, {"from": account})
    # link_token_contract = interface.LinkTokenInterface(link_token.address)
    # tx = link_token_contract.transfer(contract_address, amount, {"from": account})
    tx.wait(1)
    print(f"Fund contract!{contract_address}")
    return tx
