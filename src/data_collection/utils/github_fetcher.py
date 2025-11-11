import requests
import os
from pathlib import Path

def fetch_github_markdown(repo, folder, output_dir):
    """
    Fetch markdown files from a GitHub repository folder.
    """
    api_url = f"https://api.github.com/repos/{repo}/contents/{folder}"
    response = requests.get(api_url)

    if response.status_code != 200:
        print(f"[ERROR] GitHub API returned {response.status_code}: {response.text}")
        return

    try:
        data = response.json()
    except Exception:
        print("[ERROR] Unable to parse GitHub JSON response.")
        return

    if not isinstance(data, list):
        print(f"[ERROR] Unexpected response format: {data}")
        return

    os.makedirs(output_dir, exist_ok=True)

    for item in data:
        if "name" not in item:
            continue

        if not item["name"].endswith(".md"):
            continue

        download_url = item.get("download_url")
        if not download_url:
            print(f"[WARN] No download_url for {item['name']}")
            continue

        file_content = requests.get(download_url).text
        output_path = Path(output_dir) / item["name"]

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(file_content)

        print(f"[DOWNLOAD] {item['name']}")
