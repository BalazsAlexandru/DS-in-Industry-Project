from django import forms
from django.shortcuts import render
import re
from transformers import pipeline
import nltk
from nltk.corpus import twitter_samples
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Create your views here.
from .models import Tweet


def index(request):
    all_tweets = Tweet.objects.all()
    return render(request, 'tweets.html', {'tweets': all_tweets})


class TweetSearchForm(forms.Form):
    search_date = forms.DateField()


def tweet_search(request):
    if request.method == 'POST':
        form = TweetSearchForm(request.POST)
        if form.is_valid():
            search_date = form.cleaned_data['search_date']
            tweets = Tweet.objects.filter(tweet_date=search_date)
            return render(request, 'tweet_search.html', {'tweets': tweets})
    else:
        form = TweetSearchForm()
    return render(request, 'tweet_search.html', {'form': form})


def tweet_search_sumarised(request):
    if request.method == 'POST':
        form = TweetSearchForm(request.POST)
        if form.is_valid():
            search_date = form.cleaned_data['search_date']
            tweets = Tweet.objects.filter(tweet_date=search_date)
            text = text_summarisation(tweets)
            return render(request, 'tweet_summarize.html', {'text': text, 'tweets': tweets})
    else:
        form = TweetSearchForm()
    return render(request, 'tweet_summarize.html', {'form': form})


def text_summarisation(tweets):
    text = ''
    for tweet in tweets:
        text += tweet.tweet_text

    text = re.sub(r"http\S+", "", text)
    text = text.replace("@", "")
    text = text.replace("#", "")
    text = text.replace(".", ".<eos>")
    text = text.replace("!", ".<eos>")
    text = text.replace("?", ".<eos>")
    sentences = text.split("<eos>")
    new_sentences = []
    for sen in sentences:
        if len(sen) < 5:
            continue
        else:
            new_sentences.append(re.sub(' +', ' ', sen))
    summarizer = pipeline("summarization")

    max_chunk = 500
    current_chunk = 0
    chunks = []
    for sentence in new_sentences:
        if len(chunks) == current_chunk + 1:
            if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            print(current_chunk)
            chunks.append(sentence.split(' '))

    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])
    result = summarizer(chunks, max_length=120, min_length=30, do_sample=False)
    Summary = ''
    for i in range(len(result)):
        Summary += result[i]['summary_text']
    return Summary


def tweet_sentiment(request):
    corpus_tweet = []
    all_tweets = Tweet.objects.all()
    for tweet in all_tweets:
        corpus_tweet.append(tweet.tweet_text)
    korpus = []
    for tweet in corpus_tweet:
        korpus.append(tweet_process(tweet))
    nltk.download('twitter_samples')
    all_positive_tweets = twitter_samples.strings('positive_tweets.json')
    all_negative_tweets = twitter_samples.strings('negative_tweets.json')
    test_pos = all_positive_tweets[4000:]
    train_pos = all_positive_tweets[:4000]
    test_neg = all_negative_tweets[4000:]
    train_neg = all_negative_tweets[:4000]

    train_x = train_pos + train_neg
    test_x = test_pos + test_neg

    train_y = np.append(np.ones(len(train_pos)), np.zeros(len(train_neg)))
    test_y = np.append(np.ones(len(test_pos)), np.zeros(len(test_neg)))

    freqs = create_frequency(train_x, train_y)

    logprior, loglikelihood = train_naive_bayes(freqs, train_x, train_y)

    myList = []

    for tweet in all_tweets:
        myList.append(tweet.tweet_text)

    p_list = []
    for tweet in myList:
        p = naive_bayes_predict(tweet, logprior, loglikelihood)
        p_list.append(p)

    df = pd.Series(p_list)
    ndf = df.to_frame(name='p')

    data = pd.DataFrame()

    data['sentiment'] = p_list
    fig = plt.figure(figsize=(14, 6))
    sns.histplot(data['sentiment'], kde=True, color='cadetblue')
    plt.savefig("./static/sentimentPlot.png")

    return render(request, 'tweet_sentiment.html' ,{})


def tweet_process(tweet):
    tweet = re.sub(r"http\S+", "", tweet)
    tweet = tweet.replace("@", "")
    tweet = tweet.replace("#", "")
    return(tweet)


def create_frequency(tweets, ys):
    freq_d = {}

    for tweet, y in zip(tweets, ys):
        for word in tweet_process(tweet):

            pair = (word, y)

            if pair in freq_d:
                freq_d[pair] += 1
            else:
                freq_d[pair] = freq_d.get(pair, 1)

    return freq_d


def train_naive_bayes(freqs, train_x, train_y):
    '''
    Input:
        freqs: dictionary from (word, label) to how often the word appears
        train_x: a list of tweets
        train_y: a list of labels correponding to the tweets (0,1)
    Output:
        logprior: the log prior. (equation 3 above)
        loglikelihood: the log likelihood of you Naive bayes equation. (equation 6 above)
    '''

    loglikelihood = {}
    logprior = 0

    # calculate the number of unique words in vocab
    unique_words = set([pair[0] for pair in freqs.keys()])
    V = len(unique_words)

    # calculate N_pos and N_neg
    N_pos = N_neg = 0
    for pair in freqs.keys():

        # TODO: get N_pos and N_get
        if pair[1] > 0:
            N_pos += freqs[(pair)]

        else:
            N_neg += freqs[(pair)]

    # TODO: calculate the number of documents (tweets)
    D = train_y.shape[0]

    # TODO: calculate D_pos, the number of positive documents (tweets)
    D_pos = sum(train_y)

    # TODO: calculate D_neg, the number of negative documents (tweets)
    D_neg = D - sum(train_y)

    # TODO: calculate logprior
    logprior = np.log(D_pos) - np.log(D_neg)

    # for each unqiue word
    for word in unique_words:
        # get the positive and negative frequency of the word
        freq_pos = freqs.get((word, 1), 0)
        freq_neg = freqs.get((word, 0), 0)

        # calculate the probability that word is positive, and negative
        p_w_pos = (freq_pos + 1) / (N_pos + V)
        p_w_neg = (freq_neg + 1) / (N_neg + V)

        # calculate the log likelihood of the word
        loglikelihood[word] = np.log(p_w_pos / p_w_neg)

    return logprior, loglikelihood

def naive_bayes_predict(tweet, logprior, loglikelihood):
    '''
    Input:
        tweet: a string
        logprior: a number
        loglikelihood: a dictionary of words mapping to numbers
    Output:
        p: the sum of all the logliklihoods of each word in the tweet (if found in the dictionary) + logprior (a number)

    '''

    # TODO: process the tweet to get a list of words
    word_l = tweet_process(tweet)

    # TODO: initialize probability to zero
    p = 0

    # TODO: add the logprior
    p += logprior

    for word in word_l:

        # TODO: get log likelihood of each keyword
        if  word in loglikelihood:
            p += loglikelihood[word]

    return p

from rest_framework import generics
from .models import Tweet
from .serializers import TweetSerializer

class TweetList(generics.ListAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer