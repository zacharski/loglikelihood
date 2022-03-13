import configparser
import fileinput
import sys
from collections import Counter
from math import log

def entropy(elements):
  sum = 0
  result = 0
  for element in elements:
    if element > 0:
      result += element * log(element)
      sum += element
  result -= sum * log(sum)
  return -result



def logLikelihoodRatio(biCount, w1, w2, tot):
  rowEntropy = entropy([biCount, w1]) + entropy([w2, tot])
  columnEntropy = entropy([biCount, w2]) + entropy([w1, tot])
  matrixEntropy = entropy([biCount, w1, w2, tot])
  if (rowEntropy + columnEntropy > matrixEntropy):
    	return 0;
  else:
    return 2 * (matrixEntropy - rowEntropy - columnEntropy)  


def computeLogLikelihood(filename, outfilename):
  global punct, ignoreCase, numResults
  print('GLOBAL', punct)
  tot = 0
  bigrams = Counter()
  unigrams = Counter()
  #punct = "“”.,?:;-"
  w1 = ''
  w2 = 'HEAD'
  for line in fileinput.input([filename]):
      words = line.split()
      for word in words:
        word = word.strip(punct)
        if ignoreCase == 'yes':
            word = word.lower()
        # check whether after removing punctuation
        # there is still characters in the word
        if word != '':
          w1 = w2
          w2 = word
          bigrams[w1 + ' ' + w2] += 1
          unigrams[w2] += 1
          #print(w1, w2)
          tot = tot + 1
        # now compute log likelihood for each bigram        
  results = Counter()
  for (key, value) in bigrams.items():
    (w1, w2) = key.split()
    results[key] = logLikelihoodRatio(value, unigrams[w1] - value, unigrams[w2] - value, tot-value)
  if numResults == 'all':
    resultsData =   results.most_common()
  else:
    resultsData =  results.most_common(int(numResults))  
  with open(outfilename, 'w') as outfile:
      for (phrase, score) in resultsData:
          outfile.write("%s\t%f5.3\n" % (phrase, score))


if len(sys.argv) == 3:


    config = configparser.ConfigParser()  
    config.read('ll.conf')

    punct = config['DEFAULT']['Punctuation']
    ignoreCase = config['DEFAULT']['IgnoreCase']
    numResults = config['DEFAULT']['NumResults']
    computeLogLikelihood(sys.argv[1], sys.argv[2])

else:
    print("Incorrect number of arguments")








