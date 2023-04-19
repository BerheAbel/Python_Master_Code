from nestedTuple import albums 


SONG_TITLE_INDEX = 1
SONG_LIST_INDEX = 3
while True:
    print("please choose your album(invalid choice will exit) ")
    for index, value in enumerate(albums):
        title,artist,year,songs = value
        print(index + 1, title)
    choice = int(input())
    if 1 <= choice <=len(albums):
        songs_list = albums[choice-1][SONG_LIST_INDEX]
    else:
        break
    # print(albums[choice-1])
    # print(songs_list)
    print("please choose your song: ")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
    else:
        break
    print("Playing {}".format(title))
    print("=" * 40)

       