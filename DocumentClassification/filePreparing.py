from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string


class FilePreparing:

    file_name = ''

    def on(self, file_name):
        self.file_name = file_name
        return self

    def make_cleanup(self):
        self.__remove_header__(self.file_name)
        text = self.__get_raw_text_from_file__(self.file_name)
        self.__refactor__(text)


    def __remove_header__(self, file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
            if not "From:" in lines[0]:
                return
        with open(file_name, "w") as f:
            for index,line in enumerate(lines):
                if index != 0 and index != 1:
                    f.write(line)

    def __get_raw_text_from_file__(self, file_name):
        file = open(file_name, 'rt')
        text = file.read()
        file.close()
        return text

    def __refactor__(self, text):
        # split into words
        tokens = word_tokenize(text)

        # convert to lower case
        tokens = [w.lower() for w in tokens]

        # remove punctuation from each word
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in tokens]

        # remove remaining tokens that are not alphabetic
        words = [word for word in stripped if word.isalpha()]

        # filter out stop words
        stop_words = set(stopwords.words('english'))
        words = [w for w in words if not w in stop_words]
        print(words)

        # stemming of words
        from nltk.stem.porter import PorterStemmer
        porter = PorterStemmer()
        stemmed = [porter.stem(word) for word in words]
        print(stemmed)

fileprepere = FilePreparing()
fileprepere.on("99971").make_cleanup()
