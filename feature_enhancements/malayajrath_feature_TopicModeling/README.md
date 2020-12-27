# Topic Modelling
## OVERVIEW 
#### Implementation of Topic Modelling using sklearn , nltk and Latent Dirichlet Allocation algorithm
### 21 Dec 2020
#### Ideas , method of implementation and expectations from the model were discussed with the mentor .
#### A new folder was made in the feature addition branch named as Malayaj_feature_TopicModelling .
### 22 Dec 2020
 #### Some research on topic modelling and Latent Dirichlet Allocation algorithm was done .
#### A basic algorithm was prepared for the code . 
#### Algorithm:
    1. Preprocessing the text with NLTK (removal of stopword and special character of words) the occurring 90% of time 
       was removed and threshold to keep a word is decided as 2 i.e if word occurs at least twice it will be kept. 
       
    2. Vectorize each word using count vectorizer.
    
    3. Pass the entire  matrix of vectors (document term matrix )to the LDA function in sklearn.
    
    4. Obtain topics and top words related to  the topics by sorting it according to the probability of belonging to the topic.

### 24 Dec 2020
#### Pseudo code was prepared and a preliminary model containing 3 functions  main( ) , preprocessing( ) and topic_modelling( ) was made .
#### main( ) mainly take basic input like document text  and the number of topics to  be displayed .
#### preprocessing( ) preprocess the text like removing the stopwords and special characters. 
#### topic_modelling( ) vectorize the text and form document term  matrix and pass it to  LDA function to  produce topics and top word belonging to  the topic. 
 
### 26 Dec 2020 
#### Final model was made . 
#### Requirements.txt file is updated  accordingly.
### 27 Dec 2020 
#### Second PR is sent for evaluation.
## how to  use
### install requirements.txt using the command
    pip install -r requirements.txt
### run the file using the command 
    python TopicModelling.py
##### then  write the text which topic to be found and press enter
##### enter the number of topics to be found and press enter again
