import cv2
import pytesseract
from os import listdir
from os.path import isfile, join

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


# 이미지가 저장된 디렉토리와 FPS 설정
images_path = 'C:\\Users\\SSAFY\\Desktop\\frames\\Coldplay - Viva la Vida (Lyrics)'
fps = 60

# 이미지 파일 목록 가져오기
image_files = [f for f in listdir(images_path) if isfile(join(images_path, f))]

# OCR 결과와 재생 시간을 저장할 리스트
ocr_results = []

for image_file in sorted(image_files):
    image_path = join(images_path, image_file)
    image = cv2.imread(image_path)

    text = pytesseract.image_to_string(image)
    frame_number = int(image_file.replace('frame', '').replace('.jpg', ''))
    timestamp = frame_number / fps
    ocr_results.append((timestamp, text))

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    millis = int((seconds - int(seconds)) * 1000)
    formatted_time = f"{hours:02}:{minutes:02}:{int(seconds):02}.{millis:03}"
    return formatted_time


lyrics_data = []

# 정렬된 OCR 결과를 기반으로 중복 제거 및 시간 범위 설정
prev_text = ""
start_time = 0.0
end_time = 0.0

for timestamp, text in sorted(ocr_results, key=lambda x: x[0]):
    cleaned_text = text.strip().replace("\n", " ")

    # 동일한 가사가 연속될 경우, 끝 시간만 업데이트
    if cleaned_text == prev_text and cleaned_text != "":
        end_time = timestamp
    else:
        # 새로운 가사 부분 시작 시, 이전 가사 정보 저장
        if prev_text != "":
            lyrics_data.append((start_time, end_time, prev_text))
        start_time = timestamp
        end_time = timestamp
        prev_text = cleaned_text

# 마지막 가사 부분 추가
if prev_text != "":
    lyrics_data.append((start_time, end_time, prev_text))

# 정제된 데이터 출력
for start, end, text in lyrics_data:
    formatted_start = format_time(start)
    formatted_end = format_time(end)
    print(f"[{formatted_start} --> {formatted_end}] {text}")