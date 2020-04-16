import os

from pytube import Playlist, YouTube

def run(p1) :
    filepath = input("Location download (Use '/' for split folder) : ")
    if filepath[-1] != "/" :
        filepath = filepath + "/"

    links = p1.parse_links()

    for link in links :
        yt = YouTube(link)
        music = yt.streams.filter(only_audio=True).first()
        default_filename = music.default_filename
        while default_filename == "YouTube.mp4" :
            default_filename = music.default_filename
        if os.path.exists(filepath + default_filename[:-3] + "mp3") :
            print("Check : " + default_filename[:-4] + " Already ...")
            continue
        print("Downloading : " + default_filename[:-4])
        music.download(output_path = filepath)
        base, ext = os.path.splitext(default_filename)
        name_file_mp3 = base + ".mp3"
        os.rename(filepath + default_filename, filepath + name_file_mp3)
    print("Download finished.")

if __name__ == "__main__" :
    url = input("Input URL : ")
    p1 = Playlist(url)
    run(p1)


