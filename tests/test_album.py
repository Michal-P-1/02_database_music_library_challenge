from lib.album import Album

"""
Album constructs with id, title, release_year and artist_id
"""
def test_album_constructs():
    album = Album(1, "Test_title", 1990, 1)
    assert album.id == 1
    assert album.title == "Test_title"
    assert album.release_year == 1990
    assert album.artist_id == 1

"""
We can format albums to string 
"""
def test_album_format_to_string():
    album = Album(1, "Test_title", 1990, 1)
    assert str(album) == "Album(1, Test_title, 1990, 1)"

"""
Test if albums are equal
"""
def test_albums_are_equal():
    album_1 = Album(1, "Test_title", 1990, 1)
    album_2 = Album(1, "Test_title", 1990, 1)
    assert album_1 == album_2
