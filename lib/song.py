class Song:
    songs = []
    artist_count = {}
    genre_count = {}
    artists = []
    genres = []
    count = 0

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1
        Song.songs.append(self)

        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()
    pass
    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)
    pass
    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)
    pass
    def add_to_genre_count(self):
        if self.genre not in Song.genre_count:
            Song.genre_count[self.genre] = 0
        Song.genre_count[self.genre] += 1
    pass
    def add_to_artist_count(self):
        if self.artist not in Song.artist_count:
            Song.artist_count[self.artist] = 0
        Song.artist_count[self.artist] += 1
    pass