from readwise import fetch_source_urls
from scraper import scrape_content
from fabric_integration import analyze_with_fabric

def analyze_readwise_articles(location='feed', pattern='rate_content'):
    """
    Analyze articles from Readwise, scraping and rating them using Fabric.

    Args:
        location (str): The location parameter to filter documents. Defaults to 'new'.
        pattern (str): The pattern used by Fabric for analysis. Defaults to 'rate_content'.

    Returns:
        list: A list of dictionaries containing URLs and their analyses.
    """
    urls = fetch_source_urls(location)
    analysis_results = []

    for url in urls:
        try:
            content = scrape_content(url)
            analysis = analyze_with_fabric(content, pattern)
            analysis_results.append({'url': url, 'analysis': analysis})
        except Exception as e:
            print(f"Error processing {url}: {e}")

    return analysis_results