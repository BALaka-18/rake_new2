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

  <img src="https://latex.codecogs.com/svg.latex?IDF(w,D)=\log\frac{|D|}{|\{d:w \in d \} | }" title="IDF(w,D)=\log\frac{|D|}{|\{d:w \in d \} | }"/>

We obtain the TF-IDF by multiplying these two elements:

<img src="https://latex.codecogs.com/svg.latex?TFIDF(w,d)=TF(w,d) \times IDF(w,D)" title="TFIDF(w,d)=TF(w,d) \times IDF(w,D)"/>

This measure gives insight into words that appears often in a specific document, but not in the other documents of the set. Indeed, words that are frequent in each document are often not very relevant; they are not selected with TF-IDF. But when there is only one document in <img src="https://latex.codecogs.com/svg.latex?D" title="D"/>, TF-IDF simply consists in choosing keyword on their frequency, which may not be bery relevant.

### RAKE

RAKE stands for Rapid Automatic Keyword Extraction. It was introduced in 2010 by _Rose, Stuart, et al. "Automatic keyword extraction from individual documents."_ [[1]](#references).

Let's consider the following text:

_Keyword extraction is not that difficult after all. There are many libraries that can help you with keyword extraction. Rapid automatic keyword extraction is one of those._

1. First, let's split the text using its **stopwords** to produce some **candidate keywords**. The text becomes 
    
    `Keyword extraction` _is not that_ `difficult` _after all. There are_ `many libraries` _that can_ `help` _you with_ `keyword extraction`. `Rapid automatic keyword extraction` _is one of those._
    
    The candidate keywords (`keyword extraction`, `difficult`...) are sequences composed of **content words** (here `keyword`, `extraction`, `difficult`...).
    
2. Splitting the text highlighted the words co-occurences. We can therefore build the **co-occurence matrix** <img src="https://latex.codecogs.com/svg.latex?M=(n_{i,j})_{i,j\leq p}" title="M=(n_{i,j})_{i,j\leq p}"/>, where <img src="https://latex.codecogs.com/svg.latex?n_{i,j}" title="n_{i,j}"/> is the number of co-occurences of the content words i and j.

    |            | keyword | extraction | difficult | many | libraries | help | rapid | automatic |
    |------------|---------|------------|-----------|------|-----------|------|-------|-----------|
    | keyword    | 3       | 3          |           |      |           |      | 1     | 1         |
    | extraction | 3       | 3          |           |      |           |      | 1     | 1         |
    | difficult  |         |            | 1         |      |           |      |       |           |
    | many       |         |            |           | 1    | 1         |      |       |           |
    | libraries  |         |            |           | 1    | 1         |      |       |           |
    | help       |         |            |           |      |           | 1    |       |           |
    | rapid      | 1       | 1          |           |      |           |      | 1     | 1         |
    | automatic  | 1       | 1          |           |      |           |      | 1     | 1         |
    
3. Then, we compute a **score for each word**. This score can take various forms, such as 
    - the **degree** <img src="https://latex.codecogs.com/svg.latex?d_i" title="d_i"/> of the word in the co-occurence matrix (the sum of the number of co-occurences the word has with any other context word);
    - the **frequency** <img src="https://latex.codecogs.com/svg.latex?f_i" title="f_i"/> of the word (the number of occurences of the word in <img src="https://latex.codecogs.com/svg.latex?t" title="t"/>);
    - the ratio of degree to frequency, <img src="https://latex.codecogs.com/svg.latex?d_i \/ f_i" title="d_i \/ f_i"/>;

    |           | keyword | extraction | difficult | many | libraries | help | rapid | automatic |
    |-----------|---------|------------|-----------|------|-----------|------|-------|-----------|
    | degree    | 8       | 8          | 1         | 2    | 2         | 1    | 4     | 4         |
    | frequency | 3       | 3          | 1         | 1    | 1         | 1    | 1     | 1         |
    | ratio     | 2.7     | 2.7        | 1         | 2    | 2         | 1    | 4     | 4         |

4. The word scores are then used to attribute a score to each **expression** of the text (here `keyword extraction`, `many libraries`...) by summing the scores of its words.

5. Finally, the best ranked expressions can be used to summarize the text.

_Sentence of the example was taken from [Keyword Extraction](https://monkeylearn.com/keyword-extraction/), MonkeyLearn_ [[2]](#references)

## 2. Linguistic approaches


## 3. Graph-based approaches

### Building a graph

To represent a text as a graph, we can consider its words as vertices. The edges (connections between the vertices) can be labelled, for instance with the relation that those words have in the text. Edges can be **directed** (signifying a unilateral dependency between the words) or **undirected** (co-occurences for instance).

![Graphs](./.github/img/graphs.png)
_An undirected graph (left) and a directed one (right)._

Next, we want to measure how important a word is based on the information contained in the graph and its structure. To do so, we can compute the **degree** of each vertice of the graph, being for a directed graph

<img src="https://latex.codecogs.com/svg.latex?D_v=D_v^{in}+D_v^{out}" title="D_v=D_v^{in}+D_v^{out}"/>

where <img src="https://latex.codecogs.com/svg.latex?D_v^{in}" title="D_v^{in}"/> is the number of edges whose end is <img src="https://latex.codecogs.com/svg.latex?v" title="v"/> and <img src="https://latex.codecogs.com/svg.latex?D_v^{out}" title="D_v^{out}"/> the number of edges starting from <img src="https://latex.codecogs.com/svg.latex?v" title="v"/>. For an undirected graph, <img src="https://latex.codecogs.com/svg.latex?D_v" title="D_v"/> is simply the number of edges that have an endpoint in <img src="https://latex.codecogs.com/svg.latex?v" title="v"/>. It is then possible to normalize this number between 0 and 1 using a division by the maximum degree in the graph.


### TextRank

The TextRank algorithm was introduced in 2004 by [[3]](#references). The basic idea is to attribute a score for each vertex, as we did above, taking into account the number of in and out edges linked to it. We define the score of a vertex <img src="https://latex.codecogs.com/svg.latex?v_i" title="v_i"/> by

<img src="https://latex.codecogs.com/svg.latex?S(v_i)=(1-d)+d*\sum_{j\in In(v_i)}\frac{1}{\vert Out(v_j)\vert}S(v_j)" title="S(v_i)=(1-d)+d*\sum_{j\in In(v_i)}\frac{1}{\vert Out(v_j)\vert}S(v_j)"/>

where <img src="https://latex.codecogs.com/svg.latex?In(v)" title="In(v)"/> is the set of vertices that point to <img src="https://latex.codecogs.com/svg.latex?v" title="v"/>, <img src="https://latex.codecogs.com/svg.latex?Out(v)" title="Out(v)"/> the set of vertices that <img src="https://latex.codecogs.com/svg.latex?v" title="v"/> points to, and <img src="https://latex.codecogs.com/svg.latex?d\in[0,1]" title="d\in[0,1]"/> a **damping factor**. This algorithm actually derives from Google's PageRank [[4]](#references) and implements the "random surfer model" in the field of web surfing, where a user clicks on links at random with a probability <img src="https://latex.codecogs.com/svg.latex?d" title="d"/> and jumps to a completely different page with a probability <img src="https://latex.codecogs.com/svg.latex?1-d" title="1-d"/>. The factor <img src="https://latex.codecogs.com/svg.latex?d" title="d"/> is usually set to 0.85.

Starting from arbitrary values assigned to each node in the graph, the **computation** iterates until convergence below a given threshold is achieved.

For **weighted graphs**, we only need to slightly change the equation:

<img src="https://latex.codecogs.com/svg.latex?WS(v_i)=(1-d)+d*\sum_{j\in In(v_i)}\frac{w_{ji}}{\sum_{v_k\in Out(v_j)}w_{jk}}WS(v_j)" title="WS(v_i)=(1-d)+d*\sum_{j\in In(v_i)}\frac{w_{ji}}{\sum_{v_k\in Out(v_j)}w_{jk}}WS(v_j)"/>


## 4. Machine Learning approaches



### References

**[1]**&emsp;Ramos, Juan. _"Using tf-idf to determine word relevance in document queries."_ Proceedings of the first instructional conference on machine learning. Vol. 242. 2003.\
**[2]**&emsp;_"Keyword Extraction: A Guide to Finding Keywords in Text."_ Monkeylearn, [https://monkeylearn.com/keyword-extraction/](https://monkeylearn.com/keyword-extraction/)\
**[3]**&emsp;Mihalcea, Rada, Paul Tarau, and Elizabeth Figa. _"PageRank on semantic networks, with application to word sense disambiguation."_ COLING 2004: Proceedings of the 20th International Conference on Computational Linguistics. 2004.\
**[4]**&emsp;Brin, Sergey, and Lawrence Page. _"The anatomy of a large-scale hypertextual web search engine."_. 1998.\
