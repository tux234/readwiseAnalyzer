from readwise import fetch_source_urls
from scraper import scrape_content
from fabric_integration import analyze_with_fabric

def analyze_readwise_articles(location='feed', pattern='rate_content'):
    """Main function to analyze articles from Readwise."""
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