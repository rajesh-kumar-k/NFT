from brownie import advancedNFT, network, accounts
from scripts.helpfulscript import breed, getaccount, OPENSEA_URL

waifus = {
    "BlindedPink": "https://ipfs.io/ipfs/QmdMijAjT6K8ZXxMY5UdN7S4QfWuXA1s2L8LAWspBSbcsV?filename=0-BlindedPink.json",
    "PurpleBlast": "https://ipfs.io/ipfs/QmZGkNTNt6n6e6pXGYF3MgZHpTTti24W6TwJWHSZgnBiz8?filename=3-PurpleBlast.json",
    "Yellove": "https://ipfs.io/ipfs/QmdGDZUm6Hr9Xm6hEL1VySzXfiK98K9dNSe1nBB1CivU5K?filename=1-Yellove.json",
}


def main():
    advanced_collectible = advancedNFT[-1]
    numberofcollectible = advanced_collectible.tokenCounter()
    print(f"you have created {numberofcollectible} collectibles")
    for tokenID in range(numberofcollectible):
        breeds = breed(advanced_collectible.tokenIDtobreed(tokenID))
        if not advanced_collectible.tokenURI(tokenID).startswith("https://"):
            print(f"Setting tokenURI of {tokenID}")

            print(breeds)
            set_tokenURI(tokenID, advanced_collectible, waifus[breeds])


def set_tokenURI(token_ID, nftcontract, tokenuri):
    account = getaccount()
    tx = nftcontract.setTokenURI(token_ID, tokenuri, {"from": account})
    tx.wait(1)
    print(
        f"Awesome! You can view your NFT at {OPENSEA_URL.format(nftcontract.address, token_ID)}"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button")
