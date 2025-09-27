import os
import re
import httpx

BASE_URL = "https://ftp.ncbi.nlm.nih.gov/blast/db/"
OUT_DIR = "metadata_jsons"

def download_metadata_jsons():
    os.makedirs(OUT_DIR, exist_ok=True)

    # Fetch directory listing
    with httpx.Client(follow_redirects=True, timeout=60.0) as client:
        resp = client.get(BASE_URL)
        resp.raise_for_status()
        html = resp.text

        # Regex to find all .json links
        json_links = re.findall(r'href="([^"]+\.json)"', html)
        print(f"Found {len(json_links)} JSON files")

        for link in json_links:
            url = BASE_URL + link
            local_path = os.path.join(OUT_DIR, link)

            # Skip if already downloaded
            if os.path.exists(local_path):
                print(f"Skipping {link}, already exists")
                continue

            print(f"Downloading {url}")
            r = client.get(url)
            r.raise_for_status()
            with open(local_path, "wb") as f:
                f.write(r.content)

    print("✅ All JSON files downloaded")

if __name__ == "__main__":
    download_metadata_jsons()
