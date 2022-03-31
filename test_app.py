import json

class TestCases():
    def test_home_route(self, api):
        res = api.get('/')
        assert res.status == '200 OK'

    def test_post_url(self, api):
        mock_form_data = {'url':'http://www.google.com'}
        resp = api.post('/', data=mock_form_data, follow_redirects=True)
        assert resp.status == '200 OK'
  