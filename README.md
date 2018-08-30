# redditimage.py
a script for scraping image links off of a subreddit

## Usage
At the start of the script, change `verbose` to true to show debugging information, change to false to only output discovered links without additional information.
```python
verbose = True
```

At the end of the script, change `"Cyberpunk"` to the subreddit you want to target. `Count` is currently not implemented.
```python
if __name__ == '__main__':
	reddit_scrape("Cyberpunk", 10)
```

## To-do:
1. Implement imgur() function
2. implement parameters/arguments for operation from command line
