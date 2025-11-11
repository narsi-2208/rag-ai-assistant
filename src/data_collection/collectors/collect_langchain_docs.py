from pathlib import Path
from data_collection.utils.github_fetcher import fetch_github_markdown


def collect_langchain():
    output_dir = Path("data/raw/docs/langchain")
    fetch_github_markdown(
        repo="langchain-ai/langchain",
        folder="docs",
        output_dir=output_dir
    )
