import requests
from pathlib import Path

def download_pdf(url, output_dir, filename=None):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if not filename:
        filename = url.split("/")[-1] + ".pdf"

    output_path = output_dir / filename

    print(f"[INFO] Downloading paper {url}")
    r = requests.get(url)
    with open(output_path, "wb") as f:
        f.write(r.content)

    print(f"[SAVED] {output_path}")
    return output_path
