from readwise import fetch_source_urls
from scraper import scrape_content
from fabric_integration import analyze_with_fabric
from concurrent.futures import ThreadPoolExecutor

def analyze_readwise_articles(location='feed', pattern='rate_content', max_workers=8):
    """
    Analyze articles from Readwise, scraping and rating them using Fabric in parallel.

    Args:
        location (str): The location parameter to filter documents. Defaults to 'feed'.
        pattern (str): The pattern used by Fabric for analysis. Defaults to 'rate_content'.
        max_workers (int): Number of threads for parallel processing. Defaults to 8.

    Returns:
        list: A list of dictionaries containing URLs and their analyses.
    """
    urls = fetch_source_urls(location)
    results = []

    def _process(url):
        try:
            content = scrape_content(url)
            analysis = analyze_with_fabric(content, pattern)
            return {'url': url, 'analysis': analysis}
        except Exception as e:
            print(f"Error processing {url}: {e}")
            return None

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for result in executor.map(_process, urls):
            if result:
                results.append(result)

    return results