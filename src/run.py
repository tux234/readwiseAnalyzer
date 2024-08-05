from analysis import analyze_readwise_articles

def categorize_articles_by_rating(articles):
    """
    Categorize articles based on their Fabric analysis rating.

    Args:
        articles (list): A list of articles with URLs and analyses.

    Returns:
        tuple: Categorized lists of articles for shortlist, read this week, weekend list, and archive.
    """
    shortlist = []
    read_this_week = []
    weekend_list = []
    archive = []

    for article in articles:
        url = article['url']
        analysis = article['analysis']

        # Extract the rating tier from the analysis
        rating_line = next((line for line in analysis.splitlines() if "Tier:" in line), None)
        if not rating_line:
            continue

        # Determine the category based on the rating tier
        if "S Tier" in rating_line:
            shortlist.append((url, analysis))
        elif "A Tier" in rating_line:
            read_this_week.append((url, analysis))
        elif "B Tier" in rating_line or "C Tier" in rating_line:
            weekend_list.append((url, analysis))
        elif "D Tier" in rating_line:
            archive.append((url, analysis))

    return shortlist, read_this_week, weekend_list, archive

def main():
    """
    Main function to analyze and categorize Readwise articles.
    """
    results = analyze_readwise_articles()

    # Categorize articles based on their ratings
    shortlist, read_this_week, weekend_list, archive = categorize_articles_by_rating(results)

    # Print categorized results
    print("\nShortlist (S Tier):")
    for url, analysis in shortlist:
        print(f"URL: {url}")

    print("\nRead This Week (A Tier):")
    for url, analysis in read_this_week:
        print(f"URL: {url}")

    print("\nWeekend List (B & C Tier):")
    for url, analysis in weekend_list:
        print(f"URL: {url}")

    print("\nArchive (D Tier):")
    for url, analysis in archive:
        print(f"URL: {url}")

if __name__ == "__main__":
    main()