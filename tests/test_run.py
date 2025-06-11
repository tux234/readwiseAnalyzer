from run import categorize_articles_by_rating


def test_categorize_articles_by_rating():
    articles = [
        {'url': 'surl', 'analysis': 'Something\nTier: S Tier\nExtra'},
        {'url': 'aurl', 'analysis': 'Tier: A Tier'},
        {'url': 'burl', 'analysis': 'Tier: B Tier'},
        {'url': 'curl', 'analysis': 'Tier: C Tier'},
        {'url': 'durl', 'analysis': 'Tier: D Tier'},
        {'url': 'nurl', 'analysis': 'No tier here'},
    ]
    shortlist, read_this_week, weekend_list, archive = categorize_articles_by_rating(articles)
    assert shortlist == [('surl', 'Something\nTier: S Tier\nExtra')]
    assert read_this_week == [('aurl', 'Tier: A Tier')]
    assert weekend_list == [('burl', 'Tier: B Tier'), ('curl', 'Tier: C Tier')]
    assert archive == [('durl', 'Tier: D Tier')]