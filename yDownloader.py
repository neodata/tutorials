from pytube import YouTube

link = input("Entrez le lien de la video Youtube: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()