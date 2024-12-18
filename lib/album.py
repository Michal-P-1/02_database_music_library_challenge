class Album:
    def __init__(self, id, title, release_year, artist_id):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    # magic method - default method python calls when 2 objects are compared (==) is __eq__ magic method, 
    # we change this built-in method here to our liking
    # this is waht python basically does behind the scenes - object1.__eq__(object2)
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"