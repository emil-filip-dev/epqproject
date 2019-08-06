import unittest, requests


def exists(url):
    return requests.get(url).status_code == 200


class PagesExist(unittest.TestCase):

    def test_index(self):
        assert exists("http://52.56.146.169/")
        assert exists("http://52.56.146.169/index")

    def test_read_page(self):
        assert exists("http://52.56.146.169/read/page")


if __name__ == '__main__':
    unittest.main()
