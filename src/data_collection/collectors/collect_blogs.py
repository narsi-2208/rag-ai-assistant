import requests
from bs4 import BeautifulSoup
from pathlib import Path

def collect_blogs():
    whitelist = [
        "https://www.qdrant.tech/articles/",
        "https://blog.langchain.dev/",
        "https://milvus.io/blog/",
        "https://llamaindex.ai/blog/",
    ]

    output_dir = Path("data/raw/blogs")
    output_dir.mkdir(parents=True, exist_ok=True)

    for url in whitelist:
        print(f"[SCRAPING] {url}")
        
        try:
            html = requests.get(url).text
        except Exception as e:
            print(f"[ERROR] Failed to load {url}: {e}")
            continue

        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(" ", strip=True)

        filename = (
            url.replace("https://", "")
            .replace("http://", "")
            .replace("/", "_")
            + ".txt"
        )

        with open(output_dir / filename, "w", encoding="utf-8") as f:
            f.write(text)

        print("[SAVED]", filename)
