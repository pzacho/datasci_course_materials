import sys
import json
import operator

def lines(fp):
    print str(len(fp.readlines()))

def parseTweet(aTweetLine):
    aTweet = json.loads(aTweetLine)
    if (aTweet.has_key('entities')) and (aTweet['entities'].has_key('hashtags')):
        return(aTweet['entities']['hashtags'])
    else:
        return({})

def calcFreq(aTermDict, aLine):
    if len(aLine):
        # split line into words
        words = aLine.split(' ')
        for word in words:
            if word.strip() in aTermDict:
                aTermDict[word.strip()] += 1
            else:
                aTermDict[word.strip()] = 1
    return(aTermDict)

def main():
    tweet_file = open(sys.argv[1])
    # initialise an empty dictionary
    tagsList = {}
    for line in tweet_file:
        hashtags = parseTweet(line)
        for tags in hashtags:
            if tags['text'].lower() in tagsList:
                tagsList[tags['text'].lower()]+=1
            else:
                tagsList[tags['text'].lower()]=1
    # sort list
    sortedList = sorted(tagsList.iteritems(), key=operator.itemgetter(1))
    sortedList.reverse()
    for x in range(0,9):
        print sortedList[x][0], sortedList[x][1]

if __name__ == '__main__':
    main()
