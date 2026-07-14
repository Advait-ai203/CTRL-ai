# tools/crypto_agents/nft_minter.py
import json
import os

def generate_nft_metadata(asset_name: str, description: str, image_ipfs_uri: str, attributes: list) -> str:
    """Generates standard ERC-721 JSON metadata for NFT minting."""
    target_dir = "./generated_assets/web_builds/nft_metadata"
    os.makedirs(target_dir, exist_ok=True)
    
    metadata = {
        "name": asset_name,
        "description": description,
        "image": image_ipfs_uri,
        "attributes": attributes
    }
    
    file_path = os.path.join(target_dir, f"{asset_name.replace(' ', '_').lower()}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)
        
    return f"🖼️ **NFT Metadata Compiled:** Ready for IPFS upload at `{file_path}`"
