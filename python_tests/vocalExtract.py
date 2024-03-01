from spleeter.separator import Separator

def main():
    separator = Separator('spleeter:2stems')

    audio_file = "C:\\Users\\SSAFY\\Desktop\\audios\\Coldplay - Viva La Vida (Official Video).mp4"
    output_dir = 'C:\\Users\\SSAFY\\Desktop\\audios'

    separator.separate_to_file(audio_file, output_dir)

if __name__ == '__main__':
    main()