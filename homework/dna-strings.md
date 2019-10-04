---
layout: work
number: CSCI 150
title: Foundations of Computer Science
semester: Fall 2019
---
# Homework 5: Strands of DNA

## Materials

-   [String
    Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
    in Python
-   [histone\_h4.txt](../data/histone_h4.txt)

## Description

One thread common to all life on Earth is Deoxyribonucleic acid (DNA).
DNA is composed of long strands of four basic molecules: Adenine,
Cytosine, Guanine and Thymine. These four bases coil together to form a
double-helix structure, and we have 23 such structures called
chromosomes in every cell of our body. The bases have the interesting
property of pairing up across the double-helix, such that Adenine always
matches Thymine, and Cytosine always matches Guanine. For our purposes
as computer scientists, we can abbreviate these bases as A, C, G, and T.

DNA contains segments called genes detailing how every piece of our
cells should work. A gene becomes a protein through a process known as
the [Central dogma of molecular
biology](http://en.wikipedia.org/wiki/Central_dogma_of_molecular_biology):
DNA is transcribed into RNA (Ribonucleic Acid) and then translated into
proteins. Proteins are the machinery that makes our cells work; they
form the cell walls, transport molecules around the cell, and in general
make everything work. It is this process of DNA to RNA to Proteins that
we will study in this homework, using Python and String functions to
analyze small pieces of DNA. The process may seem a bit complex, but
with Python we can make very fast progress.

### Step 1

We'll start with a small example to get familiar with how to analyze
these DNA strings with Python. Our sample DNA for these first
experiments will be

    s = "catgcttcgcataacatgactgct"

Depending on the database we use to find our DNA sequences, some may be
in lowercase, while others are all capital letters. To make our life
easier, we can convert any string to all uppercase by using the
`s.upper()` method to eliminate any variations from the source.

**G-C Content**

After capitalization, we now have

    s = "CATGCTTCGCATAACATGACTGCT"

One way to determine if there might be a gene hiding in a strand of DNA
is to examine it's G-C content. Because of how genes are encoded, most
genes have a balanced number of Gs and Cs in relation to the number of
As and Ts. To determine the G-C content of a DNA strand, we can add up
the number of Gs and Cs we find, and divide this by the total number of
bases in the string. In this case, there would be 11 Gs and Cs out of 24
total bases, giving us 45.83%. Most genes have between 25% and 75% Gs
and Cs, so this gives our strand a good shot of being a gene. Python
lets us do this with the `s.count()` method.

**Transcription from DNA to RNA**

Our next step is to transcribe the DNA into RNA. RNA is a
single-stranded molecule as opposed to the double-stranded DNA. This
means it cannot replicate itself as does DNA, but RNA still plays many
useful roles in cell function. Primarily, it is RNA that gets translated
into proteins, so having these steps be separate eases the burden on DNA
to process all the work. In the transcription from DNA to RNA, every
Thymine molecule is replace with Uracil. So when manipulating these
strings in Python, we can replace T with U using the `s.replace`(*find,
replace*) method. This gives us the RNA strand

    r = "CAUGCUUCGCAUAACAUGACUGCU"

**Translation from RNA to proteins**

![](https://upload.wikimedia.org/wikipedia/en/1/1d/Rna-codons-protein.png)
With our strand now in RNA form, we are ready to make the final step to
proteins. This works by reading the [Genetic
Code](http://en.wikipedia.org/wiki/Genetic_code) of RNA. Just like words
are composed of individual letters, genes are divided up into segments
called **codons**. A codon consists of three sequential bases, so with 4
choices for each base (from A, C, G, and U), this gives us 4 X 4 X 4 =
64 different combinations. Each of these 64 possibilities translates
into one of 20 [amino
acids](http://en.wikipedia.org/wiki/List_of_standard_amino_acids)
(redundancy is built into this system to decrease the effects of random
mutations), and it is the conjunction of these amino acids that
ultimately fold up and create proteins. Not all of the bases in a strand
of RNA will encode for a gene, and actually, only 10% - 20% of our
current DNA is known to encode genes; the other 80% - 90% of our genome
is mostly unexplained and unexplored for different modes of
functionality.

When you are reading a strand of RNA, there are two important locations
to find: where to **start** reading and where to **stop** reading. There
are actually three different ways to change a strand into amino acids.
We could start with the first base at index 0, such that our codons are
substrings from 0:3, 3:6, 6:9, etc. Staring with index 1 makes our
substrings 1:4, 4:7, 7:10, etc, and starting with index 2 gives us 2:5,
5:8, 8:11, etc.

These initial indices (0, 1, 2) define the **reading frame** for this
gene. In English we start every sentence with a capital letter, and stop
each sentence with a period. RNA uses an interesting way of signaling
the start of a gene by designating one particular codon, AUG, as the
start codon. For our purposes, wherever you find AUG, this marks the
start of a gene; this also defines our reading frame, which can be found
by modding the initial index of the start codon by 3. In our sample
sequence above, we can use the method `s.find`(*substring*) to locate
the index for "AUG", and determine that the reading frame is 1 % 3 = 1.

For robustness, there are three codons which tell us when to stop
translating RNA into amino acids: UAG, UGA and UAA. As soon as any one
of these three stop codons is found **in the same reading frame after
the start codon**, translation stops and the protein is complete. In our
RNA strand, we first find UAA at index 11, however 11 % 3 = 2 and is not
in the same reading frame as the start codon. Our next instance of a
stop codon is at index 16, and since 16 % 3 = 1, we have found our stop
codon. This means that the gene to be translated is

    gene = "CUUCGCAUAACA"

### Step 2

Now that you have some familiarity with the processing of DNA, we will
be using an [Azure Notebook](https://notebooks.azure.com/) to analyze very long DNA strings.

Open up the [`histone_h4.txt`](../data/histone_h4.txt) file. This
relatively small section of DNA (most genes are between 1000 and 10,000
bases long) that encodes for [Histone
H4](http://en.wikipedia.org/wiki/Histone). Histone H4 plays a major role
in how the DNA strands wind up to form chromosomes, and this gene is
highly conserved across almost all [Eukaryotic
organisms](http://en.wikipedia.org/wiki/Eukaryote) (those which have a
nucleus).

Create a new [Azure Notebook](https://notebooks.azure.com/) Project called
'Homework 5', and then create a new Notebook (using Python 3.6) called
'DNA.ipynb'. Open this notebook, and perform the following steps on the
Histone DNA strand. For each step, create a Code cell to write your
Python code, then create a Markdown cell to analyze your results.

1.  Create a string in the interpreter for the data in `histone_h4.txt`.
    Be sure to make it all one big long string, there should be no
    carriage returns in the middle.
2.  Convert this string to uppercase and record the first 10 and last 10
    bases.
3.  Find and record the GC content of the DNA as a percent of the
    overall length of the DNA.
4.  Translate this gene into RNA. Record how many bases were changed
    from T to U.
5.  Determine the reading frame for the first gene present in the RNA.
6.  Find the segment of RNA that encodes the first gene, excluding the
    start and stop codon. This will take some trial and error from you;
    use the functions described in the string module. Remember that the
    stop codon must be in the same reading frame as the start codon.
    Record the locations of both the start and stop codon.

## What to Hand In

-   A printed copy of your Azure Notebook.
