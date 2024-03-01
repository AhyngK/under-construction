from pytube import YouTube

video_url = 'https://www.youtube.com/watch?v=dvgZkm1xWPE'
video_url_vivalavida = 'https://www.youtube.com/watch?v=y4zdDXPYo0I'

youtube = YouTube(video_url_vivalavida)
audio_stream = youtube.streams.get_highest_resolution()

download_dir_audio = 'C:\\Users\\SSAFY\\Desktop\\audios'
download_dir_video = 'C:\\Users\\SSAFY\\Desktop\\lyrics_video'
audio_stream.download(output_path=download_dir_video)

