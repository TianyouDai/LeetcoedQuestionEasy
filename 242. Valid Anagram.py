import collections
def isAnagram(s, t):
    if collections.Counter(s) == collections.Counter(t):
        return True
    else:
        return False
        
        
