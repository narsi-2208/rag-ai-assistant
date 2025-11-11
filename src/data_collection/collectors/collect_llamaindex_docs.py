from pathlib import Path
from data_collection.utils.github_fetcher import fetch_github_markdown

def collect_llamaindex():
    output_dir = Path("data/raw/docs/llamaindex")
    fetch_github_markdown(
        repo="run-llama/llama_index",
        folder="docs",
        output_dir=output_dir
    )
