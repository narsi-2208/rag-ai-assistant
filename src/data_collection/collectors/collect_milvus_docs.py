from pathlib import Path
from data_collection.utils.github_fetcher import fetch_github_markdown

def collect_milvus():
    output_dir = Path("data/raw/docs/milvus")
    fetch_github_markdown(
        repo="milvus-io/milvus",
        folder="docs",
        output_dir=output_dir
    )
