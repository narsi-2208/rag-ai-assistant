import requests
from pathlib import Path

def collect_github_examples():
    repos = [
        "langchain-ai/langchain",
        "run-llama/llama_index",
        "qdrant/qdrant"
    ]

    output_dir = Path("data/raw/github_examples")
    output_dir.mkdir(parents=True, exist_ok=True)

    for repo in repos:
        print(f"[INFO] Fetching examples from: {repo}")

        url = f"https://api.github.com/repos/{repo}/contents/examples"
        response = requests.get(url).json()

        # Skip if examples folder not found
        if isinstance(response, dict) and response.get("message"):
            print(f"[WARN] No examples folder found for {repo}")
            continue

        for file in response:
            if file["name"].endswith((".py", ".ipynb", ".md")):
                content = requests.get(file["download_url"]).text
                path = output_dir / f"{repo.replace('/', '_')}_{file['name']}"
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                print("[DOWNLOAD]", path.name)
