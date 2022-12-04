from pytube import YouTube
link="https://youtu.be/eSEuhqVy2iI?list=RDQMe0WSIY2rGnM"
dw=YouTube(link)
mar=dw.streams.get_highest_resolution()
mar.download()
print(mar.title)