class Article:
    # List to keep track of all articles
    all = []

    def __init__(self, author, magazine, title):
        # Initialize an article with author, magazine, and title
        if not (5 <= len(title) <= 50):
            print("Error: Title must be between 5 and 50 characters")
            return  
        self.author = author  # Set the author of the article
        self.magazine = magazine  # Set the magazine of the article
        self._title = title  # Set the title of the article (this cannot be changed later)
        magazine._articles.append(self)  # Add the article to the magazine's article list
        author._articles.append(self)  # Add the article to the author's article list
        Article.all.append(self)  # Add the article to the global list of articles


    def __str__(self):
        return f"Article: {self.title}"

    @property
    def title(self):
        # Get the title of the article
        return self._title

    @title.setter
    def title(self, value):
        # Prevent changing the title after initialization
        print("Error: Title cannot be changed after initialization")


class Author:
    def __init__(self, name):
        # Initialize the author with a name
        if not isinstance(name, str) or len(name) == 0:
            print("Error: Author's name must be a non-empty string")
            return  
        self._name = name  # Set the author's name
        self._articles = []  # Initialize an empty list to hold the author's articles

    @property
    def name(self):
        # Get the author's name
        return self._name

    @name.setter
    def name(self, value):
        # Prevent changing the author's name after it's set
        print("Error: Author's name cannot be changed once set")

    def __str__(self):
        return f"Author: {self.name}"

    def articles(self):
        # Return a list of all the author's articles
        return self._articles

    def magazines(self):
        # Return a list of unique magazines the author has written for
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        # Create and return a new article written by this author
        return Article(self, magazine, title)
    
    def topic_areas(self):
    # Return a list of unique topic areas (magazine categories) for all articles by the author
        return list(set(article.magazine.category for article in self._articles)) if self._articles else None



class Magazine:
    # List to keep track of all magazines
    all = []

    def __init__(self, name, category):
        # Initialize the magazine with a name and category
        if len(name) < 2 or len(name) > 16:
            print("Error: Magazine name must be between 2 and 16 characters")
            return  
        if not isinstance(name, str):
            print("Error: Magazine name must be a string")
            return  
        if len(category) == 0:
            print("Error: Category cannot be empty")
            return  
        self._name = name  # Set the magazine's name
        self._category = category  # Set the magazine's category
        self._articles = []  # Initialize an empty list to hold the magazine's articles
        Magazine.all.append(self)  # Add this magazine to the global list of magazines


    def __str__(self):
        return f"Magazine: {self.name}"

    @property
    def name(self):
        # Get the magazine's name
        return self._name

    @name.setter
    def name(self, value):
        # Allow changing the magazine's name (with validation)
        if not isinstance(value, str):
            print("Error: Name must be a string")
            return
        if len(value) < 2 or len(value) > 16:
            print("Error: Magazine name must be between 2 and 16 characters")
            return
        self._name = value

    @property
    def category(self):
        # Get the magazine's category
        return self._category

    @category.setter
    def category(self, value):
        # Allow changing the magazine's category (with validation)
        if not isinstance(value, str):
            print("Error: Category must be a string")
            return
        if value == "":
            print("Error: Category cannot be empty")
            return
        self._category = value

    def articles(self):
        # Return a list of all articles in this magazine
        return self._articles

    def contributors(self):
        # Return a list of unique authors who have contributed to the magazine
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        # Return a list of all article titles in this magazine
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        # Return a list of authors who have written more than 2 articles for this magazine
        if not self._articles:
            return None
        authors_count = {}
        for article in self._articles:
            authors_count[article.author] = authors_count.get(article.author, 0) + 1
        contributing_authors = [author for author, count in authors_count.items() if count > 2]
        return contributing_authors if contributing_authors else None

    @classmethod
    def top_publisher(cls):
        # Return the magazine with the most articles published
        if not cls.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine._articles), default=None)



# Creating Author instances  
author1 = Author("Alice Smith")  
author2 = Author("Bob Johnson")  

# Creating Magazine instances  
magazine1 = Magazine("Tech Weekly", "Technology")  
magazine2 = Magazine("Foodie Magazine", "Food")  

# Adding articles for authors  
author1.add_article(magazine1, "The Future of AI")  
author1.add_article(magazine2, "Top Vegan Recipes")  
author2.add_article(magazine1, "Gadgets of 2024")  

# Print out the details  
print("Authors:")  
print(author1)  # What articles Alice has written  
print(author2)  # What articles Bob has written  

print("\nMagazines:")  
print(magazine1)  # Details of Tech Weekly  
print(magazine2)  # Details of Foodie Magazine  

print("\nArticles:")  
for article in Article.all:  # List all articles created  
    print(article)  



# Article titles in Foodie Magazine  
print("\nArticle titles in Foodie Magazine:")  
print(magazine2.article_titles())  

# Top publisher with the most articles  
print("\nTop publisher magazine with the most articles:")  
print(Magazine.top_publisher())

    


   