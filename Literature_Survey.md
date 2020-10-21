# Literature Survey

## Table of contents

1. [ Simple statistical approaches ](#1-simple-statistical-approaches)
2. [ Linguistic approaches ](#2-linguistic-approaches)
3. [ Graph-based approaches ](#3-graph-based-approaches)
4. [ Machine Learning approaches ](#4-machine-learning-approaches)


## 1. Simple statistical approaches

Some keyword extraction methods simply rely on some statistical measures on the words or groups of words.

### Word Frequency

Word frequency consists in computing the number of occurences of each word in a document. Once this done, it is easy to find the recurrent words by taking the ones that reached the top of the frequency list. This approach does not take into account any **order** and **link** between the words, especially synonyms, even though it might be a key to understand and summarize a document. However, it may be sufficient enough to grasp the **recurrent themes** in a specific set of documents.

### Word collocations and co-occurences

Analyzing the occurence dependencies between the words in a document may be a good idea to extract its content. To that end, two notions can be used:

- **Collocations** are words that frequently go together, such as 'customer service', 'music video'. Relevant collocations are often composed of 2 (bi-grams) or 3 (tri-grams) words. More generally, the word <img src="https://latex.codecogs.com/svg.latex?n" title="n"/>-grams is used.
- **Co-occurences** are words that tend to co-occur: they can be adjacent or not, but always have a semantic proximity and are often used in the same context.

### TF-IDF

TF-IDF [1] stands for **term frequency - inverse document frequency**. It is a measure of how important a word <img src="https://latex.codecogs.com/svg.latex?w" title="w"/> is to a document <img src="https://latex.codecogs.com/svg.latex?d" title="d"/> in a collection of documents <img src="https://latex.codecogs.com/svg.latex?D" title="D"/>. To define the TF-IDF, we need to define **term frequency** and **inverse document frequency**:

- The **term frequency** is the number of times <img src="https://latex.codecogs.com/svg.latex?w" title="w"/> appears in <img src="https://latex.codecogs.com/svg.latex?d" title="d"/> divided by the occurences of all terms in <img src="https://latex.codecogs.com/svg.latex?d" title="d"/>:

  <img src="https://latex.codecogs.com/svg.latex?TF(w,d)=\frac{n_{w,d}}{\sum_kn_{k,d}}" title="TF(w,d)=\frac{n_{w,d}}{\sum_kn_{k,d}}"/>

  and it can be normalized taking <img src="https://latex.codecogs.com/svg.latex?\log(1+TF(w,d))" title="\log(1+TF(w,d))"/>.

- the **inverse document frequency** measures how rare this word is in the whole collection <img src="https://latex.codecogs.com/svg.latex?D" title="D"/>, comparing the number of documents to the number of documents where <img src="https://latex.codecogs.com/svg.latex?w" title="w"/> appears:

  <img src="https://latex.codecogs.com/svg.latex?IDF(w,D)=\log\frac{\vert D\vert}{\vert \{d:w\in d\}\vert}" title="IDF(w,D)=\log\frac{\vert D\vert}{\vert \{d:w\in d\}\vert}"/>

We obtain the TF-IDF by multiplying these two elements:

<img src="https://latex.codecogs.com/svg.latex?TFIDF(w,d)=TF(w,d)\times IDF(w,D)" title="TFIDF(w,d)=TF(w,d)\times IDF(w,D)"/>

This measure gives insight into words that appears often in a specific document, but not in the other documents of the set. Indeed, words that are frequent in each document are often not very relevant; they are not selected with TF-IDF. But when there is only one document in <img src="https://latex.codecogs.com/svg.latex?D" title="D"/>, TF-IDF simply consists in choosing keyword on their frequency, which may not be bery relevant.

### RAKE


## 2. Linguistic approaches



## 3. Graph-based approaches



## 4. Machine Learning approaches



### References

**[1]**&emsp;Ramos, Juan. _"Using tf-idf to determine word relevance in document queries."_ Proceedings of the first instructional conference on machine learning. Vol. 242. 2003.\
