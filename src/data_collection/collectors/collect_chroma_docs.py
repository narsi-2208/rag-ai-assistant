from pathlib import Path
from data_collection.utils.github_fetcher import fetch_github_markdown

def collect_chroma():
    output_dir = Path("data/raw/docs/chroma")
    fetch_github_markdown(
        repo="chroma-core/chroma",
        folder="docs",
        output_dir=output_dir
    )
