# Music Recommendation System 

playlists = {
    "workout": {"Believer", "Unstoppable", "Hall of Fame"},
    "travel": {"Perfect", "Believer", "Señorita"},
    "party": {"Señorita", "Levitating", "Unstoppable"},
    "sad": {"Someone Like You", "Let Her Go", "Perfect"},
    "liked": {"Believer", "Levitating", "Perfect", "Hall of Fame"}
}

# Function to display all playlist names 
def display_playlists(): 
    print("\nAvailable playlists:")
    for playlist in playlists: 
        print("-", playlist.capitalize())

# Function to display songs of a playlist 
def display_songs(): 
    playlist_name = input("Enter playlist name: ").lower()

    if playlist_name in playlists: 
        if len(playlists[playlist_name]) == 0: 
            print("This playlist has no songs.")
        else: 
            print(f"\nSongs in {playlist_name.capitalize()} Playlist:")
            for song in playlists[playlist_name]: 
                print(song)
    else: 
        print("Playlist not found.")

# Function to add a song to a playlist 
def add_song(): 
    playlist_name = input("Enter playlist name: ").lower()

    if playlist_name in playlists: 
        song_name = input("Enter song name to add: ").title()

        if song_name in playlists[playlist_name]: 
            print("Song already exists in this playlist.")
        else: 
            playlists[playlist_name].add(song_name)
            print(song_name, "added to", playlist_name.capitalize(), "Playlist successfully.")
    else: 
        print("PLaylist not found.")

# Function to remove a song from a playlist
def remove_song(): 
    playlist_name = input("Enter playlist name: ").lower()

    if playlist_name in playlists: 
        song_name = input("Enter song name to remove: ").title()

        if song_name in playlists[playlist_name]: 
            playlists[playlist_name].remove(song_name)
            print(song_name, "removed from", playlist_name.capitalize(), "Playlist successfully.")
        else: 
            print("Song not found in this playlist.")
    else: 
        print("Playlist not found.")

# Function to check if a song exists in a playlist 
def check_song(): 
    playlist_name = input("Enter playlist name: ").lower()

    if playlist_name in playlists: 
        song_name = input("Enter song name to check: ").title()

        if song_name in playlists[playlist_name]: 
            print(song_name, "is present in", playlist_name.capitalize(), "Playlist.")
        else: 
            print(song_name, "is NOT present in", playlist_name.capitalize(), "Playlist.")
    else: 
        print("Playlist not found.")

# Function to show common songs between two playlists
def common_songs(): 
    playlist1 = input("Enter first playlist name: ").lower()
    playlist2 = input("Enter second playlist name: ").lower()

    if playlist1 in playlists and playlist2 in playlists: 
        common = playlists[playlist1].intersection(playlists[playlist2])

        if len(common) == 0: 
            print("No common songs in both playlists.")
        else: 
            print(f"\nCommon songs in {playlist1.capitalize()} and {playlist2.capitalize()} Playlists:")
            for song in common: 
                print(song)
    else: 
        print("One or both playlist names are invalid.")

# Function to show all songs from two playlists (union) 
def all_songs_two_playlists(): 
    playlist1 = input("Enter first playlist name: ").lower()
    playlist2 = input("Enter second playlist name: ").lower()

    if playlist1 in playlists and playlist2 in playlists: 
        all_songs = playlists[playlist1].union(playlists[playlist2])

        print(f"\nAll songs in {playlist1.capitalize()} and {playlist2.capitalize()} Playlists:")
        for song in all_songs: 
            print(song)
    else: 
        print("One or both playlist names are invalid.")

# Function to show songs only in first playlist (difference)
def only_in_first_playlist(): 
    playlist1 = input("Enter first playlist name: ").lower()
    playlist2 = input("Enter second playlist name: ").lower()

    if playlist1 in playlists and playlist2 in playlists: 
        diff = playlists[playlist1].difference(playlists[playlist2])

        if len(diff) == 0: 
            print(f"No songs are exclusively in {playlist1.capitalize()} Playlist.")
        else: 
            print(f"\nSongs only in {playlist1.capitalize()} Playlist:")
            for song in diff: 
                print(song)
    else:
        print("One or both playlist names are invalid.")