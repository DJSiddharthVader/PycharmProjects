

def add_bigram(d,key,w):
    """creates a dictionary d, with the key "key" corresponding with the entry "w", if key already
    has a corresponding a entry, the old w is turned into a list, the new w is added to it, and the
    list containing both entries is associated with the key"""
    if key in list(d.keys()):
        entry = []
        entry.append(d[key])
        entry.append(w)
        d[key]= entry
        return None
    else:
        d[key] = w
        return None


def create_bigram_dict(fn):
    """opens a specified file for reading, then associates each word as a key in an empty dictionary,
    with its corresponding value being the next word in the file and returns the dictionary"""
    wp = {}
    text = open(fn)
    for line in text:
        wordlist = []
        wordlist += line.strip().split(" ")
        for x in range(len(wordlist)-1):
            add_bigram(wp,wordlist[x],wordlist[x+1])
    return wp



