import nltk
from nltk.corpus import stopwords
import heapq

def summarizer(inputstr, output_size):

    sentence_list = nltk.sent_tokenize(inputstr)

    words = nltk.word_tokenize(inputstr.lower())

    without_punctuations = [x for x in words if x.isalnum()]
    stop_words = stopwords.words('english')
    without_stopwords = []
    for word in without_punctuations:
        #append the word to list if it is not a stopword
        if word not in set(stop_words):
            without_stopwords.append(word)

    word_frequencies = {}   #get frequency of all words in the document
    for word in without_stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

    maximum_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        #get relative frequency of each word w.r.t word with max frequency
        word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

    sentence_scores = {}
    #calculate sentence score of each sentence in document by summing the relative frequency of the words in that sentence
    #considers sentences which are less than 30 words
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    #Summarization
    summary_sentences = heapq.nlargest(output_size, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)

    return summary