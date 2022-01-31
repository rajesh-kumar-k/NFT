from brownie import accounts, network, simpleNFT
from scripts.helpfulscript import getaccount, OPENSEA_URL

URIlink = "https://ipfs.io/ipfs/QmdMijAjT6K8ZXxMY5UdN7S4QfWuXA1s2L8LAWspBSbcsV?filename=0-BlindedPink.json"


def deployer():
    account = getaccount()
    simple_collectible = simpleNFT.deploy({"from": account})
    tx = simple_collectible.createCollectible(URIlink, {"from": account})
    tx.wait(1)
    print(
        f"You can view the NFT using this link : {OPENSEA_URL.format(simple_collectible.address,simple_collectible.tokenCounter()-1)}"
    )
    return simple_collectible


def main():
    deployer()
