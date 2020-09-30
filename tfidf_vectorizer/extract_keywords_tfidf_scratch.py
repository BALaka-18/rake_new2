import string
import sys
import math
import nltk
from nltk.tokenize import wordpunct_tokenize


class TF_IDF_Scratch:
    """
    Initializes the algorithm with preferred language,
    a list of stopwords, and a list of punctuations

    If language is unspecified, it defaults to English
    If stopwords is unspecified, it defaults to the list of stopwords provided by NLTK
    If punctuations is unspecified, it defaults to Python's string.punctuation
    """

    def __init__(self, language="english", stopwords=None, punctuations=None):
        # Using the NLTK stopwords if not specified
        self.stopwords = stopwords
        if self.stopwords is None:
            self.stopwords = nltk.corpus.stopwords.words(language)

        # Using Python's string.punctuation if not specified
        self.punctuations = punctuations
        if self.punctuations is None:
            self.punctuations = string.punctuation

        # Building the ignored set by joining the stopwords and punctuations list
        # Constructing a set to remove duplicates and fast lookup
        self.ignored = set(self.stopwords + list(self.punctuations))

        # Member attributes
        self.num_docs = 0
        self.word_freq_docs = {}
        self.tf_idf = {}
        self.tf = {}
        self.idf = {}

    """
    Cleans a document by removing stopwords and punctuation

    Returns a string which represents the cleaned document
    """

    def clean_document(self, doc):
        # Tokenizing and converting to lowercase
        tokens = wordpunct_tokenize(doc)
        cleaned_doc = " ".join(
            [token.lower() for token in tokens if not token.lower() in self.ignored]
        )
        return cleaned_doc

    """
    Digests a single document and counts the unique words that appear in it
    """

    def digest_doc(self, doc):
        cleaned_doc = self.clean_document(doc)
        for word in set(cleaned_doc.split()):
            if word in self.word_freq_docs:
                self.word_freq_docs[word] += 1
            else:
                self.word_freq_docs[word] = 1

        self.num_docs += 1

    """
    Builds a frequency counter of words from a corpus of docs
    """

    def digest_docs(self, docs):
        for doc in docs:
            self.digest_doc(doc)

    """
    Calculates the tf (term frequency) for each word in a document
    """

    def compute_tf(self, doc):
        # The number of words in the document
        n = len(doc.split())

        # Counting the number of times a word is present in the document
        for word in doc.split():
            if word in self.tf:
                self.tf[word] += 1
            else:
                self.tf[word] = 1

        # Dividing every count by the number of words in the document
        # to get the term frequency of each word
        for word, count in self.tf.items():
            self.tf[word] = count / n

    """
    Calculates the idf (inverse document frequency) for each word in the document
    """

    def compute_idf(self, doc):
        # The number of documents in the corpus
        N = self.num_docs

        for word in doc.split():
            if word in self.word_freq_docs:
                self.idf[word] = math.log10(N / self.word_freq_docs[word])

    """
    Calculates the tf-idf score for each word in the document by multiplying
    the tf and idf scores
    """

    def compute_tf_idf(self):
        for word, _ in self.tf.items():
            self.tf_idf[word] = self.tf[word] * self.idf[word]

    """
    Performs the tf-idf algorithm on a specified document
    Accepts a corpus of documents, the zero based index of the document to perform tf-idf on,
    and the maximum number of keywords to extract (extracts all keywords if not specified)

    Returns a list of 2-tuples containing (word, tf-idf score) sorted in decreasing order
    Words with tf-idf scores of 0 are filtered out
    Exits with error if invalid index is specified 
    """

    def get_keywords(self, docs, doc_idx, max_num=None):
        if doc_idx > len(docs) - 1 or doc_idx < 0:
            print("ERROR: Invalid index specified!")
            sys.exit(1)

        # Cleaning up so that whenever this function is called,
        # everything starts afresh
        # If you would like to keep the old corpus,
        # comment out the lines below
        self.num_docs = 0
        self.word_freq_docs = {}
        self.tf = {}
        self.idf = {}
        self.tf_idf = {}

        self.digest_docs(docs)

        doc = docs[doc_idx]
        cleaned_doc = self.clean_document(doc)

        # Computing the tf-idf scores
        self.compute_tf(cleaned_doc)
        self.compute_idf(cleaned_doc)
        self.compute_tf_idf()

        # Sorting by highest to lowest tf-idf scores, filtering out zeroes
        sorted_keywords_scores = [
            x
            for x in sorted(self.tf_idf.items(), key=lambda x: x[1], reverse=True)
            if not x[1] == 0
        ]

        # Return upto max_num keywords or all of them,
        # depending on whether or not max_num is specified
        if max_num is None:
            return sorted_keywords_scores
        return sorted_keywords_scores[:max_num]


"""
Test run cases

docs = [
    'This is a test document',
    'This is another test document',
    'These are too small to be called documents'
]

tfidf_obj = TF_IDF_Scratch()

# Set the index of the document to be extracted
doc_idx = 0
# Set the maximum number of keywords, or don't pass it in
# to extract all the keywords
max_num = 10

print(tfidf_obj.get_keywords(docs, doc_idx, max_num))

"""
