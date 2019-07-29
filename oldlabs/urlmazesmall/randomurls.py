import random

alpha = "abcdefghijklmnopqrstuvwxyz\n"

def proportionalprob(d):
    r = random.random()
    total = 0
    for k in d.keys():
        total += d[k]
        if r < total:
            return k

def markov_freq(file, order):
    d = {}
    fin = open(file, "r")
    for line in fin.readlines():
        prev = "\n" * order
        for c in line:
            if prev not in d:
                temp = {}
                for r in alpha:
                    temp[r] = 0
                d[prev] = temp
            d[prev][c] += 1
            prev = prev[1:] + c
    for c in d:
        tot = 0.0
        for x in d[c]:
            tot += d[c][x]
        for x in d[c]:
            d[c][x] /= tot
    return d

def markov_freq_random(fdot, pages, complete, name, count, chunk, order):
    f = open("page" + str(name) + ".html", "w")
    f.write("<html><body>\n")
    f.write("<h1>Page " + str(name) + "</h1>\n")
    d = markov_freq("english2.txt", order)
    for j in range(count):
        words = []
        linked = False
        for i in range(chunk):
            w = "\n" * order
            finished = False
            while not finished:
                w += proportionalprob(d[w[-order:]])
                if w[-1] == "\n":
                    finished = True
            r = random.random()
            if not linked and r < 0.2:
                linked = True
                if not complete:
                    if len(pages) > 0 and random.random() < 0.4:
                        where = random.choice(pages)
                    else:
                        where = len(pages)
                else:
                    where = random.choice(pages)
                fdot.write("page" + str(name) + "->page" + str(where) + ";\n")
                if where not in pages:
                    pages.append(where)
                words.append("<a href=\"http://mgoadric.github.io/csci150/labs/urlmazesmall/page" + str(where) + ".html\">" + w[order:-1] + "</a>")
            else:
                words.append(w[order:-1])
        f.write(" ".join(words).capitalize() + ".<p>\n")
    f.write("</html></body>\n")
    f.close()

def main():
    fdot = open("mapping.dot", "a")
    fdot.write("digraph {\n");
    pages = []
    p = 3
    for i in range(p):
        markov_freq_random(fdot, pages, False, i, 5, 40, 3)
    print(pages)
    for pg in pages[p:]:
        markov_freq_random(fdot, pages, True, pg, 5, 40, 3)
    print(pages[p:])
    fdot.write("}")
    fdot.close()
        
main()
