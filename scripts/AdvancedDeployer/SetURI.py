from brownie import network, advancedNFT
from scripts.helpfulscript import OPENSEA_URL, breed, getaccount

waifus = {
    "BlindedPink": "https://ipfs.io/ipfs/QmdMijAjT6K8ZXxMY5UdN7S4QfWuXA1s2L8LAWspBSbcsV?filename=0-BlindedPink.json",
    "PurpleBlast": "https://ipfs.io/ipfs/QmZGkNTNt6n6e6pXGYF3MgZHpTTti24W6TwJWHSZgnBiz8?filename=3-PurpleBlast.json",
    "Yellove": "https://ipfs.io/ipfs/QmdGDZUm6Hr9Xm6hEL1VySzXfiK98K9dNSe1nBB1CivU5K?filename=1-Yellove.json",
}


def main():
    print(f"Working on {network.show_active()}")
    advanced_collectible = advancedNFT[-1]
    number_of_collectibles = advanced_collectible.tokenCounter()
    print(f"You have {number_of_collectibles} tokenIds")
    for token_id in range(number_of_collectibles):
        breeds = breed(advanced_collectible.tokenIDtobreed(token_id))
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting tokenURI of {token_id}")
            set_tokenURI(token_id, advanced_collectible, waifus[breeds])


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = getaccount()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"Awesome! You can view your NFT at {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button")
