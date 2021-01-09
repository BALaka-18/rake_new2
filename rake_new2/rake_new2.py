# Import libraries
import string
import re
from constants import TEST_TEXT
from collections import Counter, defaultdict
from itertools import groupby, product, chain
import nltk
from nltk.tokenize import wordpunct_tokenize

'''
nltk.download('stopwords')
nltk.download('punkt')
'''

# the Rake() class


class Rake():
    def __init__(self, stopwords=None, punctuations=None, language='english', keep_html_tags=False):
        # Stopwords
        self.stopwords = stopwords
        if self.stopwords is None:
            self.stopwords = nltk.corpus.stopwords.words(language)
        # Punctuations
        self.punctuations = punctuations
        if self.punctuations is None:
            self.punctuations = string.punctuation
        # HTML Tags : If a sentence contains HTML tags, you may choose whether to keep the tag names as keywords.
        # Default : False
        self.keep_html_tags = keep_html_tags

        # Clubbing all together into one list of indicators where text will be split
        self.ignore_list = list(set(chain(self.stopwords, self.punctuations)))
        # Initializing the calculation metrics
        self.freq_dist = None       # Frequency distribution of each word in the text
        self.word_degree = None     # Degrees of keywords
        self.ranklist = None        # Ranked keywords + their scores
        self.ranked_kw = None       # Only ranked keywords

    # Extract keywords
    def get_keywords_from_raw_text(self, text):
        if self.keep_html_tags:
            sentences = nltk.tokenize.sent_tokenize(text)
            self.get_keywords_from_sent(sentences)   # _______(1)
        else:
            cleanr = re.compile('<.*?>')
            cleantext = re.sub(cleanr, '', text)
            sentences = nltk.tokenize.sent_tokenize(cleantext)
            self.get_keywords_from_sent(sentences)   # _______(1)
    # (1)

    def get_keywords_from_sent(self, sentences):
        phrase_list = self.get_keywords(sentences)    # ________(2)
        # Calculation functions
        self.build_freq_dist(phrase_list)             # ________(3)
        self.build_word2word_matrix(phrase_list)      # ________(4)
        self.get_ranklist(phrase_list)                # ________(5)
    # (2)

    def get_keywords(self, sentences):
        words = []
        for sent in sentences:
            words.append([w.lower() for w in wordpunct_tokenize(sent)])
        phrases = self.get_keywords_from_words(words)     # ________(6)
        return phrases
    # (6) --> USER ACCESSIBLE FUNCTION

    def get_keywords_from_words(self, words):
        word_list = list(chain.from_iterable(words))
        ignore_final = []
        for elem in word_list:
            temp = list(elem)
            for val in temp:
                if val in string.punctuation:
                    ignore_final.append(elem)
                    break
                continue
        ignore_final = ignore_final + self.ignore_list
        filtered_groups = groupby(word_list, lambda x: x not in ignore_final)
        keywords_list = [list(grp[1]) for grp in filtered_groups if grp[0]]
        return keywords_list
    # (3)

    def build_freq_dist(self, phrase_list):
        # Why chain ? Remember that, phrase_list contains multiple keywords_list(refer function (6)).
        self.freq_dist = Counter(chain.from_iterable(phrase_list))
    # (4)

    def build_word2word_matrix(self, phrase_list):
        # Initialize blank graph
        template_graph = defaultdict(lambda: defaultdict(lambda: 0))
        # Loop through each keyword sequence
        for kw in phrase_list:
            for (w, cw) in product(kw, kw):
                template_graph[w][cw] += 1.0
        # Initialize per word degree
        self.degree = defaultdict(lambda: 0)
        for key in template_graph:
            self.degree[key] = sum(template_graph[key].values())
    # (5)

    def get_ranklist(self, phrase_list):
        self.ranklist = []
        for kw in phrase_list:
            rank = 0.0
            for word in kw:
                rank += self.degree[word]/self.freq_dist[word]
            rank = round(rank, 1)
            self.ranklist.append((rank, " ".join(kw)))
        # Return keywords in descending order of their ranks
        self.ranklist = sorted(self.ranklist, key=lambda x: x[0], reverse=True)
        self.ranked_kw = [kwd[1] for kwd in self.ranklist]

    # USER ACCESSIBLE FUNCTIONS
    # (A)
    def get_ranked_keywords(self):
        final_keywords = []
        for keyword in self.ranked_kw:
            if keyword in final_keywords:
                continue
            else:
                final_keywords.append(keyword)
        return final_keywords
    # (B)

    def get_keywords_with_scores(self):
        final_scored_keywords = []
        for score_tuple in self.ranklist:
            if score_tuple in final_scored_keywords:
                continue
            else:
                final_scored_keywords.append(score_tuple)
        return final_scored_keywords
    # (C)

    def get_word_freq(self):
        return self.freq_dist
    # (D)

    def get_kw_degree(self):
        return self.degree

    @staticmethod
    def p():
        print()


# Test run
if __name__ == '__main__':
    test_text = TEST_TEXT
    rake_obj = Rake(keep_html_tags=False)
    # Fit the algorithm on the text
    rake_obj.get_keywords_from_raw_text(test_text)

    # Showing the actual working of the library
    # Get only keywords, arranged in descending order of their importance
    print("RANKED KEYWORDS : \n{}".format(rake_obj.get_ranked_keywords()))
    # Get scores along with keywords, sorted in descending order of degree scores
    print("\n\nRANKED KEYWORDS WITH SCORES : \n{}".format(
        rake_obj.get_keywords_with_scores()))
