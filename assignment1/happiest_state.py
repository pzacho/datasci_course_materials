import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def parseTweet(aTweetLine):
    aTweet = json.loads(aTweetLine)
    if aTweet.has_key('place'):
        return(aTweet['place'], aTweet['text'])
    else:
        return("","")

def calcSentiment(aScoresDict, aLine):
    if len(aLine) > 0:
        # split line into words
        words = aLine.split(' ')
        sentiment = 0
        for word in words:
            if aScoresDict.has_key(word):
                sentiment+=aScoresDict[word]
        return(sentiment)
    else:
        return(0)
            
def addTweetSentiment(stateList, state, sentiment):
    if state in stateList:
        #print "found:", state, "=", stateList[state]
        num,sentsum=stateList[state]
        num+=1
        sentsum+=sentiment
    else:
        num=1
        sentsum=sentiment
    stateList[state] = [num,sentsum]
    return(stateList)

def findState(aString):
    if len(aString) > 0:
        return(aString[aString.index(', ')+2:])
    else:
        return("na")

def main():
    finn_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # initialise an empty dictionary
    scores = {}
    states = {}
    for line in finn_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    for line in tweet_file:
        place, tweet = parseTweet(line)
        if (place != None) and (len(place) > 0):
            if place.has_key("country_code") and place["country_code"] == "US":
                #print place["full_name"], ":", tweet.encode("utf-8")
                sentiment = calcSentiment(scores, tweet)
                states = addTweetSentiment(states, findState(place["full_name"]), sentiment)
    # find highest
    highState = None
    highSent = 0.0
    for state in states:
        num,sentsum = states[state];
        avg = float(sentsum)/float(num);
        if avg>highSent:
            highState=state
            highSent=avg

    print highState, highSent

if __name__ == '__main__':
    main()
