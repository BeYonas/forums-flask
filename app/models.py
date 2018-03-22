import datetime


class Member:
    def __init__(self, name, age):
        self.id = 0
        self.name = name
        self.age = age
        self.posts = []

    def __str__(self):
        return "Name: {name}, Age: {age}".format(name=self.name, age=self.age)

    def __dict__(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "posts": self.posts,
        }


class Post:
    def __init__(self, title, content, member_id=0):
        self.id = 0
        self.title = title
        self.content = content
        self.member_id = member_id
        self.date = datetime.datetime.now()

    def __str__(self):
        return "Title: {title}, Content: {content}".format(title=self.title, content=self.content)


    def __dict__(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "member_id": self.member_id,
        }