# loglikelihood
extracts bigrams from a text using log likelihood

## Usage

The program takes two arguments:

* inputfilename: The name of the text file to process
* outputfilename: The name of the file to write the results. 

```
python ll.py inputfilename outputfilename
```

For example, 

```
python ll.py lotusSutra.txt results.txt
```

The programs reads the configuration file, `ll.conf``.

The format of the configuration file is 

```
IgnoreCase = no
NumResults = 20
Punctuation ="“”.,?:;-"'
```

### IgnoreCase
If the value of IgnoreCase is `yes` then all words are lowercased. As a result *The Ohio, the Ohio,* and *the ohio* are all considered the same. If the value is `no` all those are considered unique.

### NumResults

The values can be either the word `all` or a number, This indicates the number of words to print to the result file.

### Punctuation
All the listed punctuation will be stripped from both the beginnings and ends of words. For example, using the value shown above `-ice-cream-` will be considered as `ice-cream`, and `end.)"` will be considered `end`