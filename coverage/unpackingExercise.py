from nestedTuple import albums
for index, value in enumerate(albums):
        title,artist,year,songs = value
        print(index + 1, value)
