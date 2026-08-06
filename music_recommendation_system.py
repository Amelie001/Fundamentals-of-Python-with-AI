# Music Recommendation System 

playlists = {
    "workout": {"Believer", "Unstoppable", "Hall Of Fame"},
    "travel": {"Perfect", "Believer", "Señorita"},
    "party": {"Señorita", "Levitating", "Unstoppable"},
    "sad": {"Someone Like You", "Let Her Go", "Perfect"},
    "liked": {"Believer", "Levitating", "Perfect", "Hall Of Fame"}
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

# Function to show songs in exactly one of two playlists (symmetric difference)
def songs_in_exactly_one(): 
    playlist1 = input("Enter first playlist name: ").lower()
    playlist2 = input("Enter second playlist name: ").lower()

    if playlist1 in playlists and playlist2 in playlists: 
        result = playlists[playlist1].symmetric_difference(playlists[playlist2])

        if len(result) == 0: 
            print("No such songs found.")
        else: 
            print(
                f"\nSongs in exectly one of {playlist1.capitalize()} or {playlist2.capitalize()} Playlists:"
            )
            for song in result:
                print(song)
    else: 
        print("One or both playlist names are invalid.")

# Function to count songs in a playlist 
def count_songs(): 
    playlist_name = input("Enter playlist name: ").lower()

    if playlist_name in playlists: 
        print( 
            "Total songs in",
            playlist_name.capitalize(),
            "Playlist =",
            len(playlists[playlist_name]),
        )
    else: 
        print("Playlist not found.")

# Function to show all unique songs in all playlists 
def all_unique_songs(): 
    unique_songs = set()

    for playlist in playlists.values(): 
        unique_songs = unique_songs.union(playlist)

    print("\nAll Unique Songs in All Playlists:")
    for song in unique_songs: 
        print(song)

    print("Total unique songs =", len(unique_songs))

# Function to check subset 
def check_subset():
    playlist1 = input("Enter first playlist name: ").lower()
    playlist2 = input("Enter second playlist name: ").lower()

    if playlist1 in playlists and playlist2 in playlists: 
        if playlists[playlist1].issubset(playlists[playlist2]):
            print(
                f"All songs of {playlist1.capitalize()} Playlist are present in {playlist2.capitalize()} Playlist."
            )
        else: 
            print(
                f"{playlist1.capitalize()} Playlist is NOT a subset of {playlist2.capitalize()} Playlist."
            )
    else:
        print("One or both playlist names are invalid.")

# Main menu 
while True:
    print("\n ===== Music Playlist Manager =====")
    print("1. Display all playlists")
    print("2. Display songs of a playlist")
    print("3. Add song to a playlist")
    print("4. Remove song from a playlist")
    print("5. CHeck whether a song is in a playlist")
    print("6. Show common songs between two playlists")
    print("7. Show all songs from two playlists")
    print("8. Show songs only in first playlist")
    print("9. Show songs in exactly one of two playlists")
    print("10. Count songs in a playlist")
    print("11. Show all unique songs in all playlists")
    print("12. Check if one playlist is a subset of another")
    print("13. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_playlists()

    elif choice == 2: 
        display_songs()

    elif choice == 3: 
        add_song()

    elif choice == 4: 
        remove_song()

    elif choice == 5: 
        check_song()

    elif choice == 6: 
        common_songs()

    elif choice == 7: 
        all_songs_two_playlists()

    elif choice == 8:
        only_in_first_playlist()

    elif choice == 9: 
        songs_in_exactly_one()

    elif choice == 10: 
        count_songs()

    elif choice == 11: 
        all_unique_songs()

    elif choice == 12: 
        check_subset()

    elif choice == 13: 
        print("Exiting Music Playlist Manager...")
        break

    else: 
        print("Invalid choice. Please enter a number between 1 and 13.")