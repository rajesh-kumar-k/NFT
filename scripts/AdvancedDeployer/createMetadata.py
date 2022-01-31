from brownie import advancedNFT, network
from scripts.helpfulscript import breed
from metadata.Basicmetadata import metadata_template
import pathlib
import requests
import json
import os


def main():
    advanced_collectible = advancedNFT[-1]
    numberofcollectible = advanced_collectible.tokenCounter()
    print(f"you have created {numberofcollectible} collectibles")
    for tokenID in range(numberofcollectible):
        breeds = breed(advanced_collectible.tokenIDtobreed(tokenID))
        metadatafile = f"./metadata/{network.show_active()}/{tokenID}-{breeds}.json"
        collectible_metadata = metadata_template
        if pathlib.Path(metadatafile).exists():
            print(f"{metadatafile} is already exists")
        else:
            print(f"Creating Path for {metadatafile}")
            collectible_metadata["name"] = breeds
            collectible_metadata["description"] = f"Hottie Naughtie"
            image_path = "./img/" + breeds + ".png"
            image_uri = upload_to_ipfs(image_path)
            collectible_metadata["image"] = image_uri
            with open(metadatafile, "w") as file:
                json.dump(collectible_metadata, file)
            upload_to_ipfs(metadatafile)


def upload_to_ipfs(file_path):
    with pathlib.Path(file_path).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = file_path.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
