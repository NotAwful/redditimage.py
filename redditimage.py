'''
redditimages.py

by Devon Taylor
===

To-do:
1. Implement image count loop
2. Implement imgur() function
3. implement parameters/arguments for operation from command line

Note: old.reddit.com is really finicky and this script currently fails a bunch
    due to 429 (Too many requests). Though this might be a local issue from
    testing it agressively, as the script only makes one request.

'''

import requests
import lxml
from lxml import etree

htmlparser = etree.HTMLParser()

# If verbose = True, show verbose information
verbose = True

def make_request(headers, url):
    '''
    :param headers: typically {'User-Agent': 'Mozilla/5.0'}
    :param url: the website to send a request to
    '''
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://"+url
    if verbose: print("[!] Making request to %s." % url)
    resp = requests.get(url,headers)
    if verbose: print("[!] HTTP Status Code: %s" % resp.status_code)
    resp = etree.fromstring(resp.text, htmlparser)
    return resp

def ireddit(page):
    '''
    This function is used for collecting the images hosted by reddit in a
        particular subreddit.

    :param page: An object generated by make_request
    :return: a list object to be added to the pages set.
    '''
    local_tasks = []
    if verbose: print("About to enter i.redd.it check.")
    for link in page.xpath('//div[@data-domain="i.redd.it"]/@data-url'):
        if verbose: print("[!] Link found: %s." % link)
        local_tasks.append(link)
    if verbose and local_tasks:
        print("[!] i.redd.it list:")
        print(local_tasks)
    return local_tasks

'''
:note: This function is currently in development. Imgur albums are annoying to
    deal with.

:param page: An object generated by make_request
:return: a list object to be added to the pages set.
def imgur(page):
    local = []
    for link in tree.xpath('//div[@data-domain="imgur.com"]/@data-url'):
        if verbose: print("[!] Imgur link found %s" % link)
        if link.startswith("https://imgur.com/a/"):
            if verbose: print("[!] Link is an album.")
            resp = make_request(link)
            for image in resp.xpath('//img/@src')
                imgur_tasks.append(image)
        elif 
    if verbose and local_tasks:
        print("[!] imgur list:")
        print(local_tasks)
    return local_tasks
'''

def reddit_scrape(subreddit, count):
'''
:param subreddit, type string: Which subreddit to query. Do not include /r/,
    just the subreddit name. Example: "Cyberpunk" rather than "/r/Cyberpunk"
:param count, type int: the minimum number of image links to grab may return
    more images than requested. It grabs all the images on a page, then checks
    how many images it has gathered.
    [!] COUNT IS NOT IMPLEMENTED, ONLY SCANS THE FIRST PAGE
:note: Adding new sources (like imgur), add another pages.update().
    The logic for checking whether or not a source exists is in the functions.
'''
    pages = set()
    headers = {'User-Agent': 'Mozilla/5.0'}
    tree = make_request(headers, 'https://old.reddit.com/r/'+subreddit)
    pages.update(ireddit(tree))
    if verbose:
        print("[!] Contents of pages:")
        print(pages)
    for link in pages: print(link)

'''
Change to the name of the subreddit you are targeting and the number of
    images to grab.
'''
if __name__ == '__main__':
	reddit_scrape("Cyberpunk", 10)
