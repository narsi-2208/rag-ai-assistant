import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from data_collection.collectors.collect_langchain_docs import collect_langchain
from data_collection.collectors.collect_llamaindex_docs import collect_llamaindex
from data_collection.collectors.collect_qdrant_docs import collect_qdrant
from data_collection.collectors.collect_chroma_docs import collect_chroma
from data_collection.collectors.collect_milvus_docs import collect_milvus
from data_collection.collectors.collect_papers import collect_papers
from data_collection.collectors.collect_github_examples import collect_github_examples
from data_collection.collectors.collect_blogs import collect_blogs


def run_all():
    print("\n=== Collecting LangChain Docs ===")
    collect_langchain()

    print("\n=== Collecting LlamaIndex Docs ===")
    collect_llamaindex()

    print("\n=== Collecting Qdrant Docs ===")
    collect_qdrant()

    print("\n=== Collecting Chroma Docs ===")
    collect_chroma()

    print("\n=== Collecting Milvus Docs ===")
    collect_milvus()

    print("\n=== Downloading Research Papers ===")
    collect_papers()

    print("\n=== Collecting GitHub Examples ===")
    collect_github_examples()

    print("\n=== Collecting Blog Articles ===")
    collect_blogs()

    print("\n✅ All data sources collected!")


if __name__ == "__main__":
    run_all()
