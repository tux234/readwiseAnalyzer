import pytest

from scraper import scrape_content


class DummyResponse:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content


def test_scrape_content_valid(monkeypatch):
    html = '<html><body><p>First</p><p>Second</p></body></html>'

    def fake_get(url, headers, timeout):
        assert url.startswith('http://')
        return DummyResponse(200, html.encode('utf-8'))

    import scraper
    monkeypatch.setattr(scraper._session, 'get', fake_get)
    text = scrape_content('http://example.com')
    assert text == 'First Second'


def test_scrape_content_unsupported_scheme():
    with pytest.raises(ValueError):
        scrape_content('ftp://example.com')


def test_scrape_content_private_ip():
    # 192.168.x.x is private and should be blocked
    with pytest.raises(ValueError):
        scrape_content('http://192.168.0.1/resource')


def test_scrape_content_http_error(monkeypatch):
    def fake_get(url, headers, timeout):
        return DummyResponse(404, b'')

    import scraper
    monkeypatch.setattr(scraper._session, 'get', fake_get)
    with pytest.raises(Exception) as excinfo:
        scrape_content('http://example.com')
    assert 'Failed to scrape URL' in str(excinfo.value)