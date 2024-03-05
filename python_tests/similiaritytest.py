
# 문장 내 단어 중요도
# 단어 단어 유사도
    # 단어장에 있는 단어와 유사도
    # 오답 단어와 유사도
# 단어 난이도


import nltk
from nltk.corpus import wordnet as wn

# nltk.download('wordnet')

def word_similarity(word1, word2):
    word1_synsets = wn.synsets(word1)
    word2_synsets = wn.synsets(word2)
    if word1_synsets and word2_synsets:
        similarity = word1_synsets[0].path_similarity(word2_synsets[0])
        return similarity
    else:
        return None

# 예시 단어로 유사도를 측정해봅니다.
similarity_score = word_similarity('cookie', 'muffin')
print(f"Similarity score: {similarity_score}")
similarity_score = word_similarity('banana', 'apple')
print(f"Similarity score: {similarity_score}")
similarity_score = word_similarity('dog', 'wolf')
print(f"Similarity score: {similarity_score}")


# 레벤슈타인 거리 계산 예시
def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    # 길이가 0인 경우, 다른 문자열의 길이가 거리가 됩니다.
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


# 예시 단어로 유사도를 측정해봅니다.
distance = levenshtein_distance('kitten', 'sitting')
print(f"Levenshtein distance: {distance}")
distance = levenshtein_distance('cookie', 'muffin')
print(f"Levenshtein distance: {distance}")