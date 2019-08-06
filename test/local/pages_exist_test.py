import unittest, requests


def exists(url):
    return requests.get(url).status_code == 200


class PagesExist(unittest.TestCase):

    def test_index(self):
        assert exists("http://127.0.0.1:5000/")
        assert exists("http://127.0.0.1:5000/index")

    def test_read_page(self):
        assert exists("http://127.0.0.1:5000/read/page")


if __name__ == '__main__':
    unittest.main()
