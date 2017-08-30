import urllib2

test = urllib2.urlopen("https://www.bitstamp.net/api/ticker/").read()
print test
