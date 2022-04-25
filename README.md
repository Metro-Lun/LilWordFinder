# Word finder
Searches words in the furnished dictionary, following the specific constraints of your choice.

## Table of contents
* [Description](#description)
* [Languages and libraries](#languages-and-library)
* [How to use it ?](#how-to-use-it)
* [References](#references)

## Description
Being tired of having to look up the Internet or the dictionary to find some types of words (i.e. words starting or ending by specific letters), I decided to make a small program to help me find them.

For now, you can search words in French and English. See [References](#references) for more information.

## Languages and libraries
* Python > 3.7
* Json library

## How to use it ?
The `words_en.json` file has been converted to a .txt file using `json_to_txt.py`.
For the main program, use the implemented functions.

### Functions :
* Find words starting or ending by specific letters
* Possibility to reduce the research to n-letter words, n being a word length of your choice

## References
* For the [French dictionary](http://jph.durand.free.fr/scrabble.txt)
* For the [English dictionary](https://www.wordgamedictionary.com/word-lists/)

## License
Distributed under the **LGPL-3.0 License**. See [license](LICENSE) for more information.