import requests
import json

class TestClass:

    URL = "http://localhost:8001/api/property/"

    POST_DATA = '{"title": "Testando Casa para Venda em Bosque Maia, Guarulhos/SP","state": "SP","city": "Guarulhos", "name": "Bosque Maia","id_json": "1teste1","purpose": "Venda","listing_type": "Casa","published_on": "2014-12-23 03:01:51 BRST-0200"}'

    def test_get_200(self):
        """GET request to url returns a 200."""
        resp = requests.get(self.URL + "list/all")
        assert resp.status_code == 200

    def test_post_delete(self):
        """POST and DELETE request to url returns a 200."""
        print type(self.POST_DATA)
        resp = requests.post(self.URL + "add/", data=json.loads(self.POST_DATA))
        assert resp.status_code == 201

        resp = requests.delete(self.URL + 'remove/1teste1')
        assert resp.status_code == 200
