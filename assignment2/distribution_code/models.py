from datetime import date


class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, year, month, day, contributors):
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        # TODO: Delete the following line and replace it with a line
        # that stores the year, month, and day (hint: check out datetime.date)
        self.creation_date = date(year, month, day)

        # list of contirbutors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        raise NotImplementedError


# TODO: Define an Article class that extends the Content class
class Article(Content):

    def __init__(self, year, month, day, headline, content, contributors):
        self.headline = headline
        self.content = content
        super(Article, self).__init__(year, month, day, contributors)

    def show (self):
        print "headline: " + self.headline
        print "content: " + self.content
        print "contributors: "
        for contributor in self.contributors:
            print contributor + " "
        print "date created " + self.creation_date.isoformat()


# TODO: Define a Picture class that extends the Content class
from PIL import Image

class Picture(Content):

    def __init__(self, year, month, day, title, caption, path, contributors):
        self.title = title
        self.caption = caption
        self.path = path
        super(Picture, self).__init__(year, month, day, contributors)

    def show (self):
        print "title: " + self.title
        print "caption: " + self.caption
        for contributor in self.contributors:
            print contributor + " "
        print "date created " + self.creation_date.isoformat()
        im = Image.open(self.path)
        im.show()

