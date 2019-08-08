import unittest, requests

remote = False
url = ""
if remote:
    url = "http://52.56.146.169/"
else:
    url = "http://127.0.0.1:5000/"


def exists(page):
    return requests.get(url + page).status_code == 200


class PagesExist(unittest.TestCase):

    def test_index(self):
        assert exists("")
        assert exists("index")


if __name__ == '__main__':
    unittest.main()
