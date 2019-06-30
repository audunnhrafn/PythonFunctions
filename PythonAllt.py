Python Áfangi forritun


Verkefni 0

def sum_two(a,b):
    return a+b
    
def mod_sum(n):
    return sum([b if b % 3 == 0 or b % 5 == 0 else 0 for b in range(n)])
    
def sum_no_3(k):
    return sum([l for l in k if l % 10 != 3])
    
def sum_first(l, n):
    return sum(l[:n])

def list_product(a, b):
    return [x*y for x,y in zip(a,b)]
    
def remove_empty(l):
    return [i for i in l if i]

def decrypt(s):
    return s[::3]


def gymnastics(l):
    if len(l) > 2:
        l.sort()
        l = l[1:-1]
    return sum(l) // len(l)

def boom(n):
    return ["boom!" if "7" in str(i) or i % 7 == 0 else str(i) for i in range(1,n+1)]
    


Verkefni 1

cdo = lambda l: ' '.join(sorted(l.split()))

from collections import Counter as c
duplicates = lambda l: [i for i,k in c(l).items() if k > 1]

flatten = lambda l:[sorted(l).index(i) for i in l]

rm_duplicates = lambda l: sorted(set(l))

scramble = lambda l, i: [l[k] for k in i]

def excel_index(i):
    n = 0
    for s in i:
        n = n * 26 + ord(s) - 64
    return n

def birthdays(i):
    d = {}
    for k in i.split():
        a = k[0:4]
        if a not in d:
            d[a] = []
        d[a].append(k)
    return [tuple(c) for c in d.values() if len(c) > 1]


BOOM SHAKALAKKA!!
from itertools import zip_longest as z
from re import split as r
from builtins import list as l

process_ls = lambda s:[e for t in l(z(*[r(' {2,}', x) for x in s.splitlines()])) for e in t if e]


Verkefni 2

def rank_hand(h):
    b = dict((r, i) for i, r in enumerate('..23456789TJQKA'))

    s = [s for r, s in h]
    h = sorted([b[r] for r, s in h])

    t = (max(h)-min(h) == 4) and 5 == len(set(h))
    f = len(set(s)) == 1
    l = 60 == sum(h)

    if t is not True and 14 == max(h) and 14 == sum(h[:4]):
        t = True

    def p(p):
        for r in h:
            if h.count(r) == p:
                return True
        return False

    def c():
        p = []
        for r in h:
            if h.count(r) == 2:
                p.append(r)
        if len(p) == 4:
            return True
        return False

    if l and f and t:
        return 9
    if t and f:
        return 8
    if p(4):
        return 7
    if p(3) and p(2):
        return 6
    if f:
        return 5
    if t:
        return 4
    if p(3):
        return 3
    if c():
        return 2
    if p(2):
        return 1
    return 0
    
    

    
from itertools import permutations

def countdown(f, w):
    result = set()
    filewords = set()

    file = open(f)
    for word in file:
        filewords.add(word.strip())

    for i in range(4, 10):
        for p in permutations(w, i):
            p = "".join(p)
            if p in filewords:
                result.add(p)

    return sorted(list(result))



import re

def css_properties(text):
    regex = re.compile(r'([\w-]*\s{0,}:[^;]*)')
    result = []

    a = re.findall(regex, text)
    for t in a:
        k = t.split(":")
        k = [x.strip() for x in k]
        b = tuple(k)
        result.append(b)

    return result


letters = ' aábcdðeéfghiíjklmnoópqrstuúvwxyýzþæö'
alphabet = {k: v for v, k in enumerate(letters)}


def sort_names(nameList):
    namesDict = {}
    namesMixed = []

    result = []

    for n in nameList:
        splited = n.split(" ")
        name = splited[0] + " " + splited[-1]

        if splited[1] is not splited[-1]:
            name += splited[1]

        name = name.lower()
        namesDict[name] = splited
        namesMixed.append(name)

    sortedNames = sorted(namesMixed, key=lambda word: [alphabet.get(c, ord(c)) for c in word])

    for p in sortedNames:
        result.append(namesDict[p])

    return [" ".join(x) for x in result]
    
    
import re
from fractions import Fraction as frac

def mixed_fractions(n):
    number = n.numerator // n.denominator
    reminder = n.numerator % n.denominator

    if reminder == 0:
        return str(number)
    if number == 0:
        return str(reminder) + "/" + str(n.denominator)
    return str(number) + " " + str(reminder) + "/" + str(n.denominator)

def fix_mixed(n):
    num, f = n.split(" ")
    return frac(f) + frac(num)

def scale(recipie, s):
    s = frac(s)
    newNumbers = []
    regex = re.compile(r'([\d]+ [\d]+/[\d]+|[\d]+/[\d]+|[\d]+)')
    numbers = re.findall(regex, recipie)

    for n in numbers:
        if " " in n:
            n = fix_mixed(n)
        newNum = frac(n) * s
        mixed = mixed_fractions(newNum)
        newNumbers.append(mixed)

    return regex.sub(lambda m: newNumbers.pop(0), recipie)
    
from itertools import product
from itertools import zip_longest
from itertools import chain

def insert_operators(numlist, n):
    strNum = [str(i) for i in numlist]
    for op in product(['+', '-', ''], repeat=len(numlist) - 1):

        possibleOps = list((a, b) for a, b in zip_longest(strNum, list(op), fillvalue=''))
        result = ''.join(chain.from_iterable(possibleOps))

        if eval(result) == n:
            result += '=' + str(n)
            return result
    return None
    
import re
import string


def hangman(file, state, guessed):
    allLetters = list(string.ascii_lowercase)
    regex = ""

    with open(file, encoding="utf-8") as fileData:
        text = fileData.read()

    for g in guessed:
        pop = allLetters.index(g)
        allLetters.pop(pop)
    letters = "".join(allLetters)

    for s in state:
        if s == "-":
            regex += "[" + letters + "]"
        else:
            regex += s
    regex = re.compile(r"\b" + regex + r"\b")

    words = list(set(re.findall(regex, text)))

    return words
    

def extract(string):
    legalList = ["4","5","6","7","8","9", "S", "M"]
    result = []
    string = string.upper()

    illegalChars = [" ", ".", "-", ","]
    for c in illegalChars:
        string = string.replace(c, "")
    string = string.replace("O", "0")
    string = string.replace("L", "1")
    stringLength = len(string)

    for i in range(stringLength):
        try:
            if string[i] == "1" and string[i+1] == "0":
                result.append(string[i] + string[i+1])
            elif string[i] == "0" and string[i-1] == "1":
                continue
            elif string[i] in legalList:
                result.append(string[i])
            else:
                return None
        except IndexError:
            return None

    return result
    
from urllib import request
import json

def count_names(string):
    fjoldi1 = fjoldi2 = 0
    with request.urlopen("http://mooshak.ru.is/~python/names.json") as url:
        data = json.loads(url.read())
    for n in data:
        nafn = n["Nafn"]
        if nafn.startswith(string):
            print(nafn)
            fjoldi1 += int(n["Fjoldi1"])
            fjoldi2 += int(n["Fjoldi2"])
    return (fjoldi1,fjoldi2)
    
from datetime import datetime
import csv
from collections import defaultdict


def release_days(cast, dates, actors):
    titles = dict()
    result = defaultdict(set)

    with open(cast) as c:
        castDict = csv.DictReader(c)
        for c in castDict:
                if c['name'] in actors:
                    titles[c["title"]] = c["year"]

    with open(dates) as d:
        datesDict = csv.DictReader(d)
        for d in datesDict:
            if d["title"] in titles and "USA" == d["country"] and titles[d["title"]] == d["year"]:
                date = d["date"]
                date = datetime.strptime(date, '%Y-%m-%d')
                weekday = datetime.weekday(date) + 1
                result[weekday].add(d["title"])

    return dict(result)

import re
import glob
import operator

problemRegex = re.compile(r'Problem\s*(\w+\b)')
teamRegex = re.compile(r'Team\s*(\w+\b)')
dateRegex = re.compile(r'Date\s*(\d+\b)')
statusRegex = re.compile(r'Classify\s*(\w+\b)')


def get_info(text):
    status = re.findall(statusRegex, text)
    if status:
        team = re.search(teamRegex, text).group(1)
        problem = re.search(problemRegex, text).group(1)
        date = re.search(dateRegex, text).group(1)
        return team, problem, date
    else:
        return None, None, None



def parse_submissions(sub):
    ans = {}
    url = sub + "/*/data.tcl"
    p = glob.glob(url)
    for s in p:
        with open(s) as f:
            t, p, d = get_info(f.read())
            if t is not None:
                ans[str(d)] = (t, p)

    sorted_ans = sorted(ans.items(), key=operator.itemgetter(0))
    a = [b for i in range(len(sorted_ans)) for b in sorted_ans[i][1:2]]
    return a
    
    
import re


def jam(string):
    persons = {}

    string = re.findall(r',\s(.*),', string)
    for i in string:
            i = i.replace(" with", ",").replace(" and", ",").replace(" plus", ",")
            i.strip()
            per = i.split(",")
            for p in per:
                p = p.lstrip(' ')
                if p == '':
                    pass
                elif p not in persons:
                    persons[p] = 1
                else:
                    persons[p] += 1
    return persons


Keppni

def balanced(s):
    for k in s:
        s = s.replace('()', '')
    return s == ""
    
import time
from calendar import isleap as y

def valid(s):
    try:
        time.strptime(s[0:6], '%d%m%y')
        p = int(s[4:6])
        if s[9] == '0':
            r = 2000 + p
        else:
            r = 1900 + p
        b = s[:4] == "2902"
        if b and not y(r):
            return False
        k = [int(i) for i in s]
        if k[8] == (11 - (((3 * k[0]) + (2 * k[1]) + (7 * k[2]) + (6 * k[3]) + (5 * k[4]) + (4 * k[5]) + (3 * k[6]) + (2 * k[7])) % 11)):
            if (k[9] == 9) or (k[9] == 0):
                return True
        return False
    except ValueError:
        return False
        
from builtins import divmod as f

def palindrome(n, b):
    k = []
    while n:
        n, d = f(n, b)
        k.append(d)
    return k == k[::-1]
    
    
from collections import defaultdict as de

def all_palindromes(f):
    res = set()
    words = list(open(f, encoding="utf-8").read().split())
    dd = de(list)

    for w in words:
        k = w.lower().replace("'", "").replace(" ", "")
        dd[k].append(w)

    for i in range(len(words)):
        for j in range(len(words[i]) + 1):
            word = words[i]
            f = words[i][j:]
            s = words[i][:j]

            f = f.replace("'", "").replace(" ", "").lower()
            s = s.replace("'", "").replace(" ", "").lower()

            if f == f[::-1] and s[::-1] in dd:
                w = dd[s[::-1]]
                for l in w:
                    res.add(word + " " + l)
            if s == s[::-1] and f[::-1] in dd:
                w = dd[f[::-1]]
                for l in w:
                    res.add(l + " " + word)

    return list(res)
    
def hamsters(h):
    k = 10000
    for i in range(len(h)):
        if h[i] > 5000:
            h[i] = k - h[i]
    a = max(h)
    n = k-min(h)

    return (a,n)
    
