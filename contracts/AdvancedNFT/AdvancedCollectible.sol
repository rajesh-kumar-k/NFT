// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract advancedNFT is ERC721, VRFConsumerBase {
    enum Breed {
        BlindedPink,
        PurpleBlast,
        Yellove
    }
    uint256 public tokenCounter;
    bytes32 public keyhash;
    uint256 public fee;
    mapping(bytes32 => address) public requestIDtosender;
    mapping(uint256 => Breed) public tokenIDtobreed;
    event CollectorsID(bytes32 indexed requestID, address requestor);
    event breedAssigned(uint256 indexed tokenid, Breed breed);

    constructor(
        address _vrfCoordinator,
        address _link,
        bytes32 _keyHash,
        uint256 _fee
    ) public ERC721("Meta", "WILD") VRFConsumerBase(_vrfCoordinator, _link) {
        tokenCounter = 0;
        keyhash = _keyHash;
        fee = _fee;
    }

    function createAdvanced() public returns (bytes32) {
        bytes32 requestID = requestRandomness(keyhash, fee);
        requestIDtosender[requestID] = msg.sender;
        emit CollectorsID(requestID, msg.sender);
    }

    function fulfillRandomness(bytes32 requestID, uint256 randomNumber)
        internal
        override
    {
        Breed breed = Breed(randomNumber % 3);
        uint256 tokenID = tokenCounter;
        tokenIDtobreed[tokenID] = breed;
        emit breedAssigned(tokenID, breed);
        address owner = requestIDtosender[requestID];
        _safeMint(owner, tokenID);
        tokenCounter += 1;
    }

    function setTokenURI(uint256 tokenID, string memory tokenURI) public {
        require(_isApprovedOrOwner(_msgSender(), tokenID), "Not Authorized!!");
        _setTokenURI(tokenID, tokenURI);
    }
}
