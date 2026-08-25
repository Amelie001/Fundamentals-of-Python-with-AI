# Music Playlist Manager (OOP)

class Playlist: 

    def __init__(self, name):
        self.name = name 
        self.songs = []

    def add_song(self, song): 
        self.songs.append(song)
        print(song, "added to the playlist.")

    def remove_song(self, song):
        self.songs.remove(song)
        print(song, "removed from playlist.")

    def search_song(self, song): 
        if song in self.songs:
            print(song, "is in the playlist.")
        else: 
            print(song, "is not in the playlist.")

    def display(self): 
        print("\nPlaylist:", self.name)

        for song in self.songs: 
            print("-", song)

playlist = Playlist("My Playlist")

playlist.add_song("7 rings")
playlist.add_song("Sports car")
playlist.add_song("drivers license")
playlist.add_song("dying on the inside")
playlist.add_song("Manchild")
playlist.add_song("All Too Well")
playlist.add_song("Born to Die")
playlist.add_song("Escapism")
playlist.add_song("bad guy")
playlist.add_song("Ain't In LA")
playlist.add_song("Gimme More")
playlist.add_song("Levitating")
playlist.add_song("That's So True")
playlist.add_song("Von dutch")
playlist.add_song("Fantasy")
playlist.add_song("Rehab")
playlist.add_song("back to friends")
playlist.add_song("Midnight Sun")
playlist.add_song("Girlfriend")

playlist.display()

playlist.remove_song("Von dutch")
playlist.remove_song("Girlfriend")

playlist.display()

playlist.search_song("7 rings")
playlist.search_song("Espresso")