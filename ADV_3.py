import concurrent.futures                                                          # concurrent execution
import newspaper                                                                   # article parsing
import timeit
from newspaper import Article                                                      # importing the Article class
'''
get_headlines
input: takes url as a input as it is called by executor.submit
output: returns the url and the list of headlines
'''
def get_headlines(url):
    result = newspaper.build(url, memoize_articles=False)                          # creates a newspaper.source object for each website
                                                                                   # used to extract articles, headlines and such
    headlines = []                                                                 # list to store the headlines for each url
    for article in result.articles[:5]:                                            # process top 5 articles
        article.download()                                                         # download the article's content
        article.parse()                                                            # parse the downloaded content
        headlines.append(article.title)                                            # adds each article title to headlines list
    return url, headlines                                                          # returns the url and headlines list to the executor   
'''
urlList:
this was adapted from https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor ,
to incorportate newspaper instead of urllib.request
'''
def urlList():
    URLs = ['http://www.foxnews.com/',
            'http://www.cnn.com/',
            'http://www.derspiegel.de/',
            'http://www.bbc.co.uk/',
            'https://theguardian.com']                                             # list of urls to get headlines
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:         # ProcessPoolExecutor class is an executor subclass that uses a pool of processes to execute calls asynchronously
        urlexecution = {executor.submit(get_headlines, url): url for url in URLs}  # submit tasks to get headlines for each url
        for completedexe in concurrent.futures.as_completed(urlexecution):         # iterate over completedexe which is of all the completed processes
            url = urlexecution[completedexe]                                       # retrieve the url associated with the completed process
            url, headlines = completedexe.result()                                 # get the url and headline
            print('\n''The headlines from %s are' % url, '\n')                     # print the headlines for the URL
            for headline in headlines:                                             # iterate over headlines list
                print(headline)                                                    # print each headline to terminal

if __name__ == '__main__':
    elapsed_time = timeit.timeit(urlList, number=2)/2                              # measure the execution time of the main function, run twice and take average time
    print(f"Elapsed Time: {elapsed_time} seconds")                                 # print the elapsed time
