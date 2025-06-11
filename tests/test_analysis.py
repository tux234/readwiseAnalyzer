import pytest

from analysis import analyze_readwise_articles


def test_analyze_readwise_articles(monkeypatch):
    urls = ["u1", "u2"]

    def fake_fetch(location):
        assert location == 'feed'
        return urls

    def fake_scrape(url):
        return f"text-{url}"

    def fake_analyze(content, pattern):
        return f"{content}-{pattern}"

    import analysis
    monkeypatch.setattr(analysis, 'fetch_source_urls', fake_fetch)
    monkeypatch.setattr(analysis, 'scrape_content', fake_scrape)
    monkeypatch.setattr(analysis, 'analyze_with_fabric', fake_analyze)
    results = analyze_readwise_articles(location='feed', pattern='pat', max_workers=2)
    expected = [
        {'url': 'u1', 'analysis': 'text-u1-pat'},
        {'url': 'u2', 'analysis': 'text-u2-pat'}
    ]
    assert results == expected