import numpy as np
import collections


# EXERCISE: write a function charfreq(path, filter) that reads the file 'path' and returns,
# in a numpy array, the relative frequencies of the characters appearing in the file,
# considering only those in the string 'filter'. Example:
# In [130]: charfreq("it-1.txt", "aeiou")
# Out[130]: array([ 0.24,  0.24,  0.24,  0.22,  0.06])
def charfreq(filename, filter):
    book = open(filename, mode='r', encoding='ISO-8859-1').read()
    open(filename, mode='w', encoding='ISO-8859-1').write(book)
    book = open(filename)

    d = collections.OrderedDict()
    filter = sorted(filter)
    for c in filter:
        d[c] = 0

    for char in book.read().lower().replace('\t', '').replace('\n', '').replace('\r', '').replace(" ", ""):
        if(char in filter):
            d[char] += 1
    a = np.array(list(d.values()))
    return a/a.sum() if a.sum() > 0 else a


# EXERCISE: write a function euc(x,y) that computes the Euclidean distance
# between two points x and y in R^n, given as numpy arrays of n elements.
def euc(x,y):
    return np.sqrt(np.sum((np.array(x)-np.array(y))**2))


# EXERCISE: now suppose we want to cluster points. Each cluster is represented as a list.
# Write a function cldist(c1, c2) that computes the (Euclidean) distance between the two
# clusters c1 and c2. Each cluster is a list of NumPy arrays (= points in R^n).
def cldist(c1,c2):
    d = np.inf
    for x in c1:
        for y in c2:
            d = min(d, euc(x,y))
    return d


# EXERCISE: Write a function closest(L) that, given a list of clusters,
# returns the indices of the two distinct clusters that are closest to each other.
def closest(L):
    mindist = np.inf
    minpair = ()
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
                dist = cldist(L[i], L[j])
                if dist < mindist:
                    mindist = dist
                    minpair = (i,j)
    return minpair


# give a sequence number to each cluster (initially, all elements cluster themselves)
def initialize_cluster(L):
    cluster = dict()
    for i in range(len(L)):
        cluster[i] = [i]
    return cluster


def cluster(L1,L2):
    L = list()
    L.append(L1)
    L.append(L2)
    return L


def size(L):
    i = 0
    for e in L:
        if len(e) != 0:
            i += 1
    return i


def deleteempty(L):
    return [e for e in L if len(e) != 0]


def single_linkage(L, k=2):
    clusterIndices = initialize_cluster(L)
    L = [[b] for b in L]
    while size(L) > k:
        pair = closest(np.array(L))
        newcluster = cluster(L[pair[0]],L[pair[1]])
        L.pop(pair[0])
        L.pop(pair[1]-1)
        L.insert(pair[0], newcluster)
        L.insert(pair[1], [])

        clusterIndices[pair[0]] = clusterIndices[pair[0]] + clusterIndices[pair[1]]
        clusterIndices[pair[1]] = []

    return deleteempty(clusterIndices.values())
