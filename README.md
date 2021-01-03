[![PyPI](https://img.shields.io/pypi/v/rake_new2)](https://pypi.org/project/rake-new2/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rake_new2)
[![GitHub](https://img.shields.io/github/license/BALaka-18/rake_new2)](https://github.com/BALaka-18/rake_new2/blob/master/LICENSE.txt)
![Maintenance](https://img.shields.io/maintenance/yes/2020)

[![GitHub issues](https://img.shields.io/github/issues/BALaka-18/rake_new2)](https://github.com/BALaka-18/rake_new2/issues)
[![GitHub forks](https://img.shields.io/github/forks/BALaka-18/rake_new2?style=social)](https://github.com/BALaka-18/rake_new2/network/members)
[![GitHub stars](https://img.shields.io/github/stars/BALaka-18/rake_new2?style=social)](https://github.com/BALaka-18/rake_new2/stargazers)

________________________________________________________________________________________________________________________________________________________________________________

<p align="center">
       <img src="https://miro.medium.com/max/1282/1*M6NUbP09lwQpaTcywBzU7w.png" alt="WoC logo" width="720" height="300" />
</p>

<p align="center">
   <strong>WINTER OF CODE 2020 PROJECT IDEAS FOR rake_new2 : <a href = "https://github.com/dsc-iem/WoC-Project-Ideas#rake_new2">Read all project ideas here</a></strong>
</p>


<p align="center">
   <strong> ---- ALL STUDENTS FOR THIS SEASON OF WoC HAVE BEEN SELECTED ALREADY. NO LONGER ACCEPTING PROPOSALS. ---- </strong> Head over to DevScript Winter of Code logo if you want to contribute. 
</p>

________________________________________________________________________________________________________________________________________________________________________________

<p align="center">
   <strong> --- AND --- </strong>
</p>

________________________________________________________________________________________________________________________________________________________________________________

<p align="center">
       <img src="https://devscript.tech/woc/img/WOC-logo.png" alt="DWoC logo" width="300" height="300" />
</p>

<p align="center">
   <strong>WINTER OF CODE 2020 PROJECT IDEAS FOR rake_new2 : <a href = "https://github.com/BALaka-18/rake_new2/issues?q=is%3Aissue+is%3Aopen+label%3ADWOC">See all updated and open Issues here. </a></strong> Comment to get assigned. Assignment is based on FCFS(First Come, First Serve) basis or based on better proposal/idea/worklflow.
</p>

________________________________________________________________________________________________________________________________________________________________________________

<h2 align="center">
   <strong>ABOUT THIS PROJECT</strong>
</h2>

<h3 align="left">
       <strong><a href = "https://pypi.org/project/rake-new2/">rake_new2</a></strong>
</h3>

rake_new2 is a Python library that enables simple and fast keyword extraction
from any text. This library helps beginners or those lost while finding keywords, understand 
which keywords are more important.

HOW IS THIS DIFFERENT FROM ANY OTHER ALGORITHM ? : This library gives you weights/scores along with each keyword/keyphrase.
This helps you pick out the correct key-phrases. Just choose the ones with more weights.  

┐(︶▽︶)┌

--> Psst! I tested it myself by writing my project abtract keywords using my library. The teacher has approved, so yeah, this works. (ʘ ͜ʖ ʘ) 

![Demo](https://user-images.githubusercontent.com/49288068/88929310-97fc2400-d297-11ea-811a-79d986cdfee4.png)

## New in version 1.0.5

1. Handles repetitive keywords/key-phrases

2. Handles consecutive punctuations.

3. Handles HTML tags in text : The user is allowed an option to choose if they
   want to keep HTML tags as keywords too.

![Demo 2](https://user-images.githubusercontent.com/49288068/89038453-00add400-d35e-11ea-8da5-62c53e1e3990.png)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install
rake_new2.

```bash
pip install rake_new2
```

## Quick Start

```python
from rake_new2 import Rake

text = "Red apples are good in taste."
text2 = "<h1> Hello world !</h1>"
rk,rk_new1,rk_new2 = Rake(),Rake(keep_html_tags=True),Rake(keep_html_tags=False)

# Case 1
# Initialize
rk.get_keywords_from_raw_text(text)
kw_s = rk.get_keywords_with_scores()
# Returns keywords with degree scores : {(1.0, 'taste'), (1.0, 'good'), (4.0, 'red apples')}
kw = rk.get_ranked_keywords()
# Returns keywords only : ['red apples', 'taste', 'good']
f = rk.get_word_freq()
# Returns word frequencies as a Counter object : {'red': 1, 'apples': 1, 'good': 1, 'taste': 1}
deg = rk.get_kw_degree()
# Returns word degrees as defaultdict object : {'red': 2.0, 'apples': 2.0, 'good': 1.0, 'taste': 1.0}

# Case 2 : Sample case for testing the 'keep_html_tags' parameter. Default = False
print("\nORIGINAL TEXT : {}".format(text))
# Sub Case 1 : Keeping the HTMLtags
rk_new1.get_keywords_from_raw_text(text2)
kw_s1 = rk_new1.get_keywords_with_scores()
kw1 = rk_new1.get_ranked_keywords()
print("Keeping the tags : ",kw1)

# Sub Case 2 : Eliminating the HTML tags
rk_new2.get_keywords_from_raw_text(text2)
kw_s2 = rk_new2.get_keywords_with_scores()
kw2 = rk_new2.get_ranked_keywords()
print("Eliminating the tags : ",kw2)

'''OUTPUT >>
ORIGINAL TEXT : <h1> Hello world !</h1>
Keeping the tags :  {'h1', 'hello'}
Eliminating the tags :  {'hello world'}
'''
```

## Debugging

You might come across a stopwords error.

It implies that you do not have the stopwords corpus downloaded from NLTK.

To download it, use the command below.

```python
python -c "import nltk; nltk.download('stopwords')"
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to
discuss what you would like to change.

Please make sure to update tests as appropriate.


## License

[MIT](https://choosealicense.com/licenses/mit/)

### Beta Tester

Sankha Subhra Mondal
