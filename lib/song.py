class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}


    def __init__(self,name,artist,genre):
        self.artist = artist
        self.name = name
        self.genre = genre
        self.add_song_to_count()
        Song.add_to_genres(self.genres)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls,genre):
        if genre not in cls.genres:
            # cls.genre_count[genre] = 1
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls,artist):
        if artist not in cls.artists:
            # cls.artist_count[artist] = 1
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls,genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 0
        cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 0
        cls.artist_count[artist] += 1












class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.genres.add(genre)
        Song.artists.add(artist)
        if genre not in Song.genre_count:
            Song.genre_count[genre] = 0
        Song.genre_count[genre] += 1
        if artist not in Song.artist_count:
            Song.artist_count[artist] = 0
        Song.artist_count[artist] += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def get_genres(cls):
        return cls.genres

    @classmethod
    def get_artists(cls):
        return cls.artists

    @classmethod
    def get_genre_count(cls):
        return cls.genre_count

    @classmethod
    def get_artist_count(cls):
        return cls.artist_count
