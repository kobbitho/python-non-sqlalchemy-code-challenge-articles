import unittest 
class Article:
     def __init__(self, author, magazine, title):
         if not isinstance(title, str) or not 5 <= len(title) <= 50:
           raise ValueError("Title must be a string between 5 and 50 characters inclusive.")
         if not isinstance(author, Author):
           raise ValueError("Author must be of type Author.")
         if not isinstance(magazine, Magazine):
           raise ValueError("Magazine must be of type Magazine.")
         self.author = author
         self.magazine = magazine
         self.title = title  
        
         
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self.name = name
        self.articles = set()
        self.magazines = set()

    def name(self):
        return self.name
    def articles(self):
        return self.articles

    def magazines(self):
        return self.magazines

    def add_article(self, magazine, title):
        if magazine not in self.magazines:
            raise ValueError('The specified magazine is not associated with this author')
        article = Article(self, magazine, title)
        self.articles.append(article)
        magazine.add_article(article)

    def topic_areas(self):
        return set(article.topic_areas for article in self.articles)

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self.name = name

        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self.category = category

        self.articles = []
        self.contributors = []
        
    def articles(self):
        pass

    def add_article(self, article):
        if article.magazine != self:
            raise ValueError("The specified article is not associated with this magazine.")
        self.articles.append(article)
        article.magazine = self

    def article_titles(self):
        return [article.title for article in self.articles]

    def contributing_authors(self):
        return [author.name for author in self.contributors]
        
    
class TestMagazine(unittest.TestCase):
    def test_contributing_authors(self):
        """returns author list who have written more than 2 articles for the magazine"""
        from classes.many_to_many import Author, Magazine, Article

        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_1, "How to be single and happy")
        Article(author_1, magazine_1, "Dating life in NYC")
        Article(author_1, magazine_2, "Carrara Marble is so 2020")
        Article(author_2, magazine_2, "2023 Eccentric Design Trends")

        self.assertEqual(magazine_1.contributing_authors(), {"Carry Bradshaw"})
        self.assertEqual(magazine_2.contributing_authors(), {"Nathaniel Hawthorne"})

if __name__ == '__main__':
    unittest.main()