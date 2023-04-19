class song:

    def __init__(self, tilte, article, duration):
        """
        song init method
        args:
        title:
        article:
        duration:
        
        """
        self.title = tilte
        self.article = article
        self.duration = duration
class Album:
    def __init__(self, name, year, artist=None):
        self.name= name
        self.year = year
        if artist is None:
            self.artist = artist("various artist")
        else:
            self.artist = artist

    def add_song(self, sonf, position=None):
        """add songs to the trsack list"""
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)