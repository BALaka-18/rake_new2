# Import libraries
import string
import re
from collections import Counter,defaultdict
from itertools import groupby,product,chain
import nltk
'''nltk.download('stopwords')
nltk.download('punkt')'''
from nltk.tokenize import wordpunct_tokenize
 
'''WHY USE wordpunct_tokenize INSTEAD OF word_tokenize ?
-> Example :
Say, text = "You're silly"
>> word_tokenize(text) --> ["You","'re","silly"]
>> wordpunct_tokenize(text) --> ["You","'","re","silly"]
 
Hence, wordpunct_tokenize > word_tokenize'''

# the Rake() class
class Rake():
  def __init__(self,stopwords=None,punctuations=None,language='english',keep_html_tags = False):
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
    self.ignore_list = list(set(chain(self.stopwords,self.punctuations)))
    # Initializing the calculation metrics
    self.freq_dist = None       # Frequency distribution of each word in the text
    self.word_degree = None     # Degrees of keywords
    self.ranklist = None        # Ranked keywords + their scores
    self.ranked_kw = None       # Only ranked keywords
  
  # Extract keywords
  def get_keywords_from_raw_text(self,text):
    if self.keep_html_tags:
      sentences = nltk.tokenize.sent_tokenize(text)
      self.get_keywords_from_sent(sentences)   # _______(1)
    else:
      cleanr = re.compile('<.*?>')
      cleantext = re.sub(cleanr, '', text)
      sentences = nltk.tokenize.sent_tokenize(cleantext)
      self.get_keywords_from_sent(sentences)   # _______(1)
  # (1)
  def get_keywords_from_sent(self,sentences):
    phrase_list = self.get_keywords(sentences)    # ________(2)
    # Calculation functions
    self.build_freq_dist(phrase_list)             # ________(3)
    self.build_word2word_matrix(phrase_list)      # ________(4)
    self.get_ranklist(phrase_list)                # ________(5)
  # (2)
  def get_keywords(self,sentences):
    words = []
    for sent in sentences:
      words.append([w.lower() for w in wordpunct_tokenize(sent)])
    phrases = self.get_keywords_from_words(words)     # ________(6)
    return phrases
  # (6) --> USER ACCESSIBLE FUNCTION
  def get_keywords_from_words(self,words):
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
    filtered_groups = groupby(word_list,lambda x : x not in ignore_final)
    keywords_list = [list(grp[1]) for grp in filtered_groups if grp[0]]
    return keywords_list
  # (3)
  def build_freq_dist(self,phrase_list):
    self.freq_dist = Counter(chain.from_iterable(phrase_list))      # Why chain ? Remember that, phrase_list contains multiple keywords_list(refer function (6)).
  # (4)
  def build_word2word_matrix(self,phrase_list):
    # Initialize blank graph
    template_graph = defaultdict(lambda : defaultdict(lambda : 0))    # Initialize all score counts to zero
    # Loop through each keyword sequence
    for kw in phrase_list:
      for (w,cw) in product(kw,kw):
        template_graph[w][cw] += 1.0
    # Initialize per word degree
    self.degree = defaultdict(lambda : 0)
    for key in template_graph:
      self.degree[key] = sum(template_graph[key].values())      # For explanation, visit the link memtioned in the README
  # (5)
  def get_ranklist(self,phrase_list):
    self.ranklist = []
    for kw in phrase_list:
      rank = 0.0
      for word in kw:
        rank += self.degree[word]/self.freq_dist[word]
      self.ranklist.append((rank, " ".join(kw)))
    # Sorting in descending order of ranks and preparing keywords + scores
    self.ranked_kw = [kwd[1] for kwd in self.ranklist]


  # USER ACCESSIBLE FUNCTIONS
  # (A)
  def get_ranked_keywords(self):
    return set(self.ranked_kw)
  # (B)
  def get_keywords_with_scores(self):
    return set(self.ranklist)
  # (C)
  def get_word_freq(self):
    return self.freq_dist
  # (D)
  def get_kw_degree(self):
    return self.degree
  @staticmethod
  def p():
    print()


'''# Test run cases
text = "Red apples are good in taste."
rake = Rake()
rake.get_keywords_from_raw_text(text)
kw_s = rake.get_keywords_with_scores()
kw = rake.get_ranked_keywords()
f = rake.get_word_freq()
deg = rake.get_kw_degree()
print(deg)
text = "<h1> Hello world !</h1>"
text2 = "<span> Hi Rahul. Hello rahul, say hi to rahul.</span><p> See, Rahul says hello, you should say hello to rahul !</p>"
text3 = "Keyword extraction is not that difficult after all. There are many libraries that can help you with keyword extraction. Rapid automatic keyword extraction is one of those."

rake1,rake2,rake3,rake4,rake5 = Rake(keep_html_tags=True),Rake(keep_html_tags=False),Rake(keep_html_tags=True),Rake(keep_html_tags=False),Rake(keep_html_tags=False)
print("\nTYPE I : ORIGINAL TEXT : {}".format(text))
# Case 1
rake1.get_keywords_from_raw_text(text)
kw_s1 = rake1.get_keywords_with_scores()
kw1 = rake1.get_ranked_keywords()
print("Keeping the tags : ",kw1)
# Case 2
rake2.get_keywords_from_raw_text(text)
kw_s2 = rake2.get_keywords_with_scores()
kw2 = rake2.get_ranked_keywords()
print("Eliminating the tags : ",kw2)
print("\nTYPE II : ORIGINAL TEXT : {}".format(text2))
# Case 3
rake3.get_keywords_from_raw_text(text2)
kw_s3 = rake3.get_keywords_with_scores()
kw3 = rake3.get_ranked_keywords()
print("Keeping the tags : ",kw3)
# Case 4
rake4.get_keywords_from_raw_text(text2)
kw_s4 = rake4.get_keywords_with_scores()
kw4 = rake4.get_ranked_keywords()
print("Eliminating the tags : ",kw4)'''
