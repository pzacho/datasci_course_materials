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

def calcFreq(aTermDict, aLine):
    if len(aLine) > 0:
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
    terms = {}
    for line in tweet_file:
        terms = calcFreq(terms, parseTweet(line))
    # calc number of terms
    totalTerms = float(sum(terms.values()))
    # calc frequency
    for term in terms:
        print term.encode("utf-8"), terms[term]/totalTerms

if __name__ == '__main__':
    main()
