import time # to use sleep function


available_lyrics = ["songs/huwag ipagsabi.txt", "songs/dati by tj.txt"]


while True:
    print("Available lyrics:\n")
    for song in available_lyrics:   
        print(song + "\n")
    selected_song = input("Enter the path of the song you want to load: ")
    if selected_song in available_lyrics:
        break
    else:
        print("Song not found. Please try again.\n\n\n\n\n")

lyric_file = open(selected_song, "r")

for line in lyric_file.readlines():
    length = len(line)
    print(line.strip())            # strip removes the new lines 
    time.sleep(length / 10)

lyric_file.close()