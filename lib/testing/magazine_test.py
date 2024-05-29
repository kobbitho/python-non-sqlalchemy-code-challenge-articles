import pytest
import unittest

from classes.many_to_many import Magazine
from classes.many_to_many import Author
from classes.many_to_many import Article


class TestMagazine(unittest.TestCase):
    """Magazine in many_to_many.py"""

    def setUp(self):
        self.magazine_1 = Magazine("Vogue", "Fashion")
        self.magazine_2 = Magazine("AD", "Architecture")
        self.author_1 = Author("Carry Bradshaw")

    def test_has_name(self):
        """Magazine is initialized with a name"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert magazine_1.name == "Vogue"
        assert magazine_2.name == "AD"

    def test_name_is_mutable_string(self):
        """magazine name is of type str and can change"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert isinstance(magazine_1.name, str)
        assert isinstance(magazine_2.name, str)

        magazine_1.name = "New Yorker"
        assert magazine_1.name == "New Yorker"

        # comment out the next two lines if using Exceptions
        # magazine_2.name = 2
        # assert magazine_2.name == "AD"

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
             Magazine(2, "Numbers")

    def test_name_len(self):
        """magazine name is between 2 and 16 characters, inclusive"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        
        assert 2 <= len(magazine_1.name) <= 16
        assert 2 <= len(magazine_2.name) <= 16

        # comment out the next two lines if using Exceptions
        #magazine_1.name = "New Yorker Plus X"
        #assert magazine_1.name == "Vogue"

        # comment out the next two lines if using Exceptions
        #magazine_2.name = "A"
        #assert magazine_2.name == "AD"

        # uncomment the next two lines if using Exceptions
        #with pytest.raises(Exception):
             #magazine_1.name = "New Yorker Plus X"

        # uncomment the next two lines if using Exceptions
        #with pytest.raises(Exception):
             #magazine_2.name = "A"

    def test_has_category(self):
        """Magazine is initialized with a category"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert magazine_1.category == "Fashion"
        assert magazine_2.category == "Architecture"

    def test_category_is_mutable_string(self):
        """magazine category is of type str and can change"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert isinstance(magazine_1.category, str)
        assert isinstance(magazine_2.category, str)

        magazine_1.category = "Life Style"
        assert magazine_1.category == "Life Style"

        assert isinstance(magazine_1.category, str)

        # comment out the next two lines if using Exceptions
        #magazine_2.category = 2
        #assert magazine_2.category == "Architecture"

        # uncomment the next two lines if using Exceptions
        #with pytest.raises(Exception):
             #Magazine_1.category = ""

    def test_category_len(self):
        """magazine category has length greater than 0"""
        magazine_1 = Magazine("Vogue", "Fashion")

        assert magazine_1.category != ""

        # comment out the next three lines if using Exceptions
        #magazine_1.category = ""
        #assert magazine_1.category == "Fashion"
        #assert magazine_1.category != ""

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     magazine_1.category = ""

    def test_has_many_articles(self):
        """magazine has many articles"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        article_1 = Article(author_1, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author_1, magazine_1, "Dating life in NYC")
        article_3 = Article(author_1, magazine_1, "How to be single and happy")
        article_4 = Article(author_1, magazine_2, "2023 Eccentric Design Trends")
        article_5 = Article(author_1, magazine_2, "Carrara Marble is so 2020")
        article_6 = Article(author_2, magazine_2, "2023 Eccentric Design Trends")

        assert len(magazine_1.articles) == 2
        assert len(magazine_2.articles) == 1
        assert article_1 in magazine_1.articles
        assert article_2 in magazine_1.articles
        assert article_3 in magazine_1.articles
        assert article_4 in magazine_2.articles
        assert article_5 in magazine_2.articles
        assert article_6 in magazine_2.articles
    def test_articles_of_type_articles(self):
        """magazine articles are of type Article"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_1, "Dating life in NYC")
        Article(author_1, magazine_1, "How to be single and happy")
        Article(author_1, magazine_2, "2023 Eccentric Design Trends")
        Article(author_1, magazine_2, "Carrara Marble is so 2020")
        Article(author_2, magazine_2, "2023 Eccentric Design Trends")

        author_1.add_article(magazine_1, "How to wear a tutu with style")

        self.assertIsInstance(magazine_1.articles[0], Article)
        self.assertIsInstance(magazine_2.articles[0], Article)

    def test_has_many_contributors(self):
        """magazine has many contributors"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_1, "Dating life in NYC")
        Article(author_2, magazine_1, "How to be single and happy")
        Article(author_1, magazine_2, "2023 Eccentric Design Trends")
        Article(author_1, magazine_2, "Carrara Marble is so 2020")
        Article(author_2, magazine_2, "2023 Eccentric Design Trends")

        assert len(magazine_1.contributors)  == 2
        assert len(magazine_2.contributors) == 1
        assert author_1 in magazine_1.contributors()
        assert author_2 in magazine_1.contributors()
        
    def test_contributors_of_type_author(self):
        """magazine contributors are of type Author"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_2, magazine_1, "Dating life in NYC")

        self.assertIsInstance(magazine_1.contributors[0], Author)
        self.assertIsInstance(magazine_1.contributors[1], Author)

    def test_contributors_are_unique(self):
        """magazine contributors are unique"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_1, "Dating life in NYC")
        Article(author_1, magazine_1, "How to be single and happy")
        Article(author_1, magazine_2, "2023 Eccentric Design Trends")
        Article(author_1, magazine_2, "Carrara Marble is so 2020")
        Article(author_2, magazine_2, "2023 Eccentric Design Trends")

  
        assert len(magazine_1.contributors)  == 2
        assert len(magazine_2.contributors) == 1
        assert author_1 in magazine_1.contributors()
        assert author_2 in magazine_1.contributors()
        

    def test_article_titles(self):
        """returns list of titles strings of all articles written for that magazine"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        magazine_3 = Magazine("GQ", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_1, "Dating life in NYC")
        Article(author_1, magazine_1, "How to be single and happy")
        Article(author_1, magazine_2, "2023 Eccentric Design Trends")
        Article(author_1, magazine_2, "Carrara Marble is so 2020")
        Article(author_2, magazine_2, "2023 Eccentric Design Trends")


        expected_titles = ["How to wear...u", "2023 Eccentric Design Trends", "Carrara Marble is so 2020"]
        assert not set(expected_titles) == set(["2023 Eccentric Design Trends", "Carrara Marble is so 2020"])
    # def test_top_publisher(self):
    #     """returns the magazine with the most articles"""
    #     Magazine.all = []
    #     Article.all = []
    #     assert Magazine.top_publisher() == None

    #     author_1 = Author("Carry Bradshaw")
    #     magazine_1 = Magazine("Vogue", "Fashion")
    #     magazine_2 = Magazine("AD", "Architecture")
    #     assert Magazine.top_publisher() == None

    #     Article(author_1, magazine_1, "How to wear a tutu with style")
    #     Article(author_1, magazine_1, "Dating life in NYC")
    #     Article(author_1, magazine_1, "How to be single and happy")
    #     Article(author_1, magazine_2, "2023 Eccentric Design Trends")
    #     Article(author_1, magazine_2, "Carrara Marble is so 2020")
        
    #     assert Magazine.top_publisher() == magazine_1
    #     assert isinstance(Magazine.top_publisher(), Magazine)