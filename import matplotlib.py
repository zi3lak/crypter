from pytube import YouTube

# Wprowadź link do filmu
link = input("https://www.youtube.com/embed/-XrRG_8wNg4")

# Załaduj film i wybierz najwyższą jakość dźwięku i obrazu
video = YouTube(link).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# Pobierz film
video.download()