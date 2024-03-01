import whisper
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

model = whisper.load_model('large', device="cpu")
result = model.transcribe("C:\\Users\\SSAFY\\Desktop\\audios\\Coldplay - Viva La Vida (Official Video)\\vocals.wav", verbose=True, language="English")

# 전체 텍스트를 문장으로 분리
sentences = sent_tokenize(result["text"])

# 각 문장의 시작 시간과 종료 시간을 저장할 리스트
sentence_times = []

# 현재 문장의 시작 인덱스
sentence_start_index = 0

for sentence in sentences:
    words = sentence.split()
    start_time = result["segments"][sentence_start_index]["start"]
    sentence_end_index = sentence_start_index + len(words) - 1
    end_time = result["segments"][sentence_end_index]["end"]
    sentence_times.append((start_time, end_time, sentence))
    sentence_start_index += len(words)

# 결과 출력
for start_time, end_time, sentence in sentence_times:
    print(f"시작 시간: {start_time}, 종료 시간: {end_time}, 문장: {sentence}")