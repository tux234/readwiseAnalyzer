import pytest

from readwise import fetch_source_urls


class DummyResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self._json_data = json_data

    def json(self):
        return self._json_data


def test_fetch_source_urls_success(monkeypatch):
    dummy_documents = {'results': [
        {'source_url': 'http://example.com/article1'},
        {'source_url': 'mailto:reader-forwarded-email@example.com'},
        {'source_url': 'https://example.org/article2'}
    ]}

    def fake_get(url, headers, params, timeout):
        assert 'list/' in url
        assert params['location'] == 'feed'
        return DummyResponse(200, dummy_documents)

    import readwise
    monkeypatch.setattr(readwise._session, 'get', fake_get)
    urls = fetch_source_urls('feed')
    assert urls == ['http://example.com/article1', 'https://example.org/article2']


def test_fetch_source_urls_invalid_location():
    with pytest.raises(ValueError):
        fetch_source_urls('invalid')


def test_fetch_source_urls_http_error(monkeypatch):
    def fake_get(url, headers, params, timeout):
        return DummyResponse(500, {})

    import readwise
    monkeypatch.setattr(readwise._session, 'get', fake_get)
    with pytest.raises(Exception) as excinfo:
        fetch_source_urls('feed')
    assert 'Failed to fetch documents' in str(excinfo.value)