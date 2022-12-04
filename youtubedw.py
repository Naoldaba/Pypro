

""""
NAME- NAOL DABA
ID- UGR/4777/14
"""
import pytube
link ="https://youtu.be/F9sw9z8PTYI"
ui=pytube.YouTube(link)
ui.streams.get_highest_resolution().download()




