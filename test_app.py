import json

class TestCases():
    def test_home_route(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
