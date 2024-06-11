from pytube import YouTube

url="https://www.youtube.com/watch?v=rJEB-0yCjKw"

yt=YouTube(url)

yt.streams.get_highest_resolution().download()

print("Video downloaded successfully!")