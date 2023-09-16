from konlpy.tag import Okt

okt = Okt()
tokens = okt.morphs("나는 자연어 처리를 배운다")
print(tokens)

word_to_index = {word : index for index, word in enumerate(tokens)}
print('단어 집합 : ', word_to_index)


def one_hot_encoding(word, word_to_index):
    one_hot_vector = [0]*(len(word_to_index))
    index = word_to_index[word]
    one_hot_vector[index] = 1
    return one_hot_vector


print(one_hot_encoding("자연어", word_to_index))