from analysis import analyze_readwise_articles

def main():
    results = analyze_readwise_articles()
    for result in results:
        print(f"URL: {result['url']}")
        print(f"Analysis: {result['analysis']}\n")

if __name__ == "__main__":
    main()