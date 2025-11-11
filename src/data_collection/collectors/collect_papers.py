from data_collection.utils.pdf_downloader import download_pdf

def collect_papers():
    paper_urls = [
        "https://arxiv.org/pdf/2005.11401.pdf",
        "https://arxiv.org/pdf/2312.10997.pdf",
    ]

    for url in paper_urls:
        download_pdf(url, output_dir="data/raw/papers")
