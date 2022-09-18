import re
# from sklearn.feature_extraction.text import CountVectorizer
import nltk
class CountVectorizer:
    def __init__(self) -> None:
        global corpus
        self.corpus = corpus
    def get_feature_names(self)->list[str]:
        str_corpus = ".".join(self.corpus)
        list_word = re.findall(r"[a-zA-z]+", str_corpus)
        dictAnswer = {}
        dictHelp = {}
        if list_word:
            for elem in list_word:
                if not elem.lower() in dictAnswer:
                    dictAnswer[elem.lower()] = 0
                    dictHelp[elem.lower()] = False
                dictAnswer[elem.lower()] += 1
        else:
            return ["The sentence does not contain words"]
        answer_list = []
        for key in dictAnswer:
            if not dictHelp[key]:
                answer_list.append(key)
                dictHelp[key] = True
        return answer_list if answer_list else ["The sentence does not contain unique words"]
    def fit_transform(self, corpus)->list[list[int]]:
        self.corpus = corpus
        answer = []
        uniquWord = self.get_feature_names()
        count = 0
        for item in corpus:
            answer.append([])
            for elem in uniquWord:
                temp_list = [a.lower() for a in re.findall(r"[a-zA-z]+", item)]
                answer[count].append(temp_list.count(elem))
            count += 1
        return answer
'''
 не понятно откуда брать корпус если первым вызовем get_feature_names метод, поэтому берем его из глобальной переменной
 и потом при вызове fit_transform метода перезатируем corpus
'''
corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste',
    'Pasta promodo fresh ingredients parmesan to adsad'
]
vectorizer = CountVectorizer()
# -
print(vectorizer.get_feature_names())
print(vectorizer.fit_transform(corpus))
# vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(corpus)
# print(X.toarray())
