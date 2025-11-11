from pathlib import Path
from data_collection.utils.github_fetcher import fetch_github_markdown

def collect_qdrant():
    output_dir = Path("data/raw/docs/qdrant")
    fetch_github_markdown(
        repo="qdrant/qdrant",
        folder="docs",
        output_dir=output_dir
    )
