class Book:
    count = 0
    def __init__(self, title, author, reviews_list):
        self.title = title
        self.author = author
        self.reviews_list = reviews_list
        self.count+=1


    def add_review(self,review):
        self.reviews_list+="\n"+review
        self.count+=1

    def count_reviews(self):
        return self.count
    
    def display_reviews(self):
        return self.reviews_list
    
b1 = Book("Atomic habit", "James Clear","Good")
b1.add_review("Nice")
print(b1.count_reviews())
print(b1.display_reviews())