import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def parseTweet(aTweetLine):
    aTweet = json.loads(aTweetLine)
    if aTweet.has_key('text'):
        return(aTweet['text'])
    else:
        return("")

def calcSentiment(aScoresDict, aLine):
    if len(aLine) > 0:
        # split line into words
        words = aLine.split(' ')
        sentiment = 0
        for word in words:
            if word in aScoresDict:
                sentiment+=aScoresDict[word]
        return(sentiment)
    else:
        return 0

def calcTermSentiments(aScoresDict, aTermDict, aLine):
    sentiment = calcSentiment(aScoresDict, aLine)
    if (len(aLine) > 0) and (sentiment != 0):
        # split line into words
        words = aLine.split(' ')
        for word in words:
            if word not in aScoresDict:
                if word in aTermDict:
                    aTermDict[word] += sentiment
                else:
                    aTermDict[word] = sentiment
    return(aTermDict)

def main():
    finn_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # initialise an empty dictionary
    scores = {}
    terms = {}
    for line in finn_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    for line in tweet_file:
        terms = calcTermSentiments(scores, terms, parseTweet(line))
    for term in terms:
        print term.encode("utf-8"), terms[term]

if __name__ == '__main__':
    main()
