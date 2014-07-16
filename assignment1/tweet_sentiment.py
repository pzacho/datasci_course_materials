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
            if aScoresDict.has_key(word):
                sentiment+=aScoresDict[word]
        print(sentiment)
    else:
        print 0
 
def main():
    finn_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # initialise an empty dictionary
    scores = {}
    for line in finn_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    for line in tweet_file:
        calcSentiment(scores, parseTweet(line))

if __name__ == '__main__':
    main()
