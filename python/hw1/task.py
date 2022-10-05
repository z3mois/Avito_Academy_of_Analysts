import re


class CountVectorizer:
    def __init__(self) -> None:
        pass

    def get_feature_names(self) -> list[str]:
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
        if answer_list:
            return answer_list
        else:
            return ["The sentence does not contain unique words"]

    def fit_transform(self, corpus) -> list[list[int]]:
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


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    print(vectorizer.fit_transform(corpus))
    print(vectorizer.get_feature_names())
