import unittest

from itheima.API.ArticlesAPI import Article


class TestArticles(unittest.TestCase):

    def setUp(self):
        self.articles=Article()

    def test_articles(self):
        result=self.articles.get_articles_id("1")

        print(result.text)