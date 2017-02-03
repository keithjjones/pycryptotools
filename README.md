# pycryptotools

A set of Python tools useful for cryptography and cryptanalysis.  More documentation will be added later.

# Installation

You can install the dependencies with the following command:

```
pip install -r requirements.txt
```

# Libraries

`library/ciphers` holds the objects for ciphers.  `library/data` holds the objects for data manipulation.
`library/statistics` holds the objects for statistical operations.

# Frequency Analysis

`frequency_analysis.py` will show the ngram frequency analysis of an input file.

## Example:

```
$ python frequency_analysis.py samples/cipher1.txt
**** Cipher Text ****

tpfccdlfdtte pcaccplircdt dklpcfrp?qeiq lhpqlipqeodf gpwafopwprti izxndkiqpkii krirrifcapnc dxkdciqcafmd vkfpcadf.


Letter Counts:
p = 13
c = 12
i = 11
d = 10
f = 9
k = 6
r = 6
q = 6
l = 5
t = 5
a = 5
e = 3
o = 2
n = 2
w = 2
x = 2
m = 1
z = 1
v = 1
g = 1
h = 1

Digram Counts:
ca = 4
iq = 3
pq = 3
pc = 3
cd = 3
dt = 2
df = 2
ki = 2
...
lf = 1

Trigram Counts:
pqe = 2
pca = 2
qpk = 1
dci = 1
...
lfd = 1

Quadgram Counts:
rrif = 1
eodf = 1
cdtd = 1
...
rpqe = 1
```

# Monoalpha (Simple) Substitution Cipher Cracker

`monoalphabuster.py` tries to crack the input cipher file assuming a mono alpha substitution cipher was used.

```
$ python monoalphabuster.py -h
usage: monoalphabuster.py [-h] [-s] [-p] [-m] CipherFile

Attempts to decrypt mono alpha ciphers.

positional arguments:
  CipherFile         The cipher file to decrypt.

optional arguments:
  -h, --help         show this help message and exit
  -s, --spaces       Counts spaces as a valid cipher character instead of
                     ignoring them.
  -p, --punctuation  Counts punctuation as valid cipher characters instead of
                     ignoring them.
  -m, --mayzner      Use Mayzner statistical data.
```

By default the data used for cracking came from practicalcryptography.com.  You can try the Mayzner data, but the PC
data tends to crack the cipher faster, in my experience.

## Example:

```
$ cat samples/cipher1.txt
tpfccdlfdtte pcaccplircdt dklpcfrp?qeiq lhpqlipqeodf gpwafopwprti izxndkiqpkii krirrifcapnc dxkdciqcafmd vkfpcadf.
$ python monoalphabuster.py samples/cipher1.txt
Loading statistical data...
Cipher Text:

tpfccdlfdtte pcaccplircdt dklpcfrp?qeiq lhpqlipqeodf gpwafopwprti izxndkiqpkii krirrifcapnc dxkdciqcafmd vkfpcadf.

Looping continuously, press ctl-c when you have your plain text!
*****
Iteration 1 better score -486.74027673721775
Current Cipher Key/Plain Values:
['p', 'm', 'q', 'n', 'i', 'u', 'v', 'e', 'd', 'z', 'l', 't', 'o', 'k', 'a', 'h', 'y', 'f', 'r', 'c', 'x', 'j', 'g', 'b', 'w', 's']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Cipher Text:
tpfccdlfdtte pcaccplircdt dklpcfrp?qeiq lhpqlipqeodf gpwafopwprti izxndkiqpkii krirrifcapnc dxkdciqcafmd vkfpcadf.

Current Plain Text:
larttikrillh atottakestil inkatrsa?chec kpackeachmir wayormayasle ejudinecanee nsessertoadt iunitectorbi gnratoir.

*****
Iteration 2 better score -451.06928385640185
Current Cipher Key/Plain Values:
['p', 'j', 'o', 'r', 'i', 'x', 'm', 'e', 'a', 'y', 'l', 'w', 'n', 'f', 'd', 'z', 'u', 'k', 'q', 'c', 'v', 'g', 't', 's', 'h', 'b']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Cipher Text:
tpfccdlfdtte pcaccplircdt dklpcfrp?qeiq lhpqlipqeodf gpwafopwprti izxndkiqpkii krirrifcapnc dxkdciqcafmd vkfpcadf.

Current Plain Text:
wanttoknowwh atittakedtow orkatnda?shes kyaskeashcon valincaladwe epfmoresaree rdeddentiamt ofrotestingo urnation.

*****
Iteration 8 better score -432.5413722871861
Current Cipher Key/Plain Values:
['p', 'h', 'q', 'o', 'i', 'g', 'm', 'e', 'a', 'y', 'l', 'n', 'w', 'f', 'd', 'x', 'b', 'k', 'r', 'c', 'v', 'u', 't', 'z', 's', 'j']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Cipher Text:
tpfccdlfdtte pcaccplircdt dklpcfrp?qeiq lhpqlipqeodf gpwafopwprti izxndkiqpkii krirrifcapnc dxkdciqcafmd vkfpcadf.

Current Plain Text:
wanttoknowwh atittakestow orkatnsa?chec kbackeachdon famindamaswe explorecaree rsessentialt oprotectingo urnation.

*****
Iteration 243 better score -431.10849018770915
Current Cipher Key/Plain Values:
['p', 'h', 'q', 'g', 'i', 'y', 'm', 'e', 'a', 's', 'l', 'n', 'o', 'f', 'd', 'x', 'b', 'k', 'r', 'c', 'v', 'u', 't', 'z', 'w', 'j']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Cipher Text:
tpfccdlfdtte pcaccplircdt dklpcfrp?qeiq lhpqlipqeodf gpwafopwprti izxndkiqpkii krirrifcapnc dxkdciqcafmd vkfpcadf.

Current Plain Text:
wanttoknowwh atittakestow orkatnsa?chec kbackeachmon dayinmayaswe explorecaree rsessentialt oprotectingo urnation.
```

# Data:

Some of the data for these tools were downloaded from http://norvig.com/mayzner.html.  The License of that project
applies to that data only.  Some other data was downloaded from http://practicalcryptography.com/.  The License of
that project applies to that data only.  The data can be found in the data directory.

# References:

Here are some references that were consulted for this project:
    - http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/#a-python-implementation
    - http://storage.googleapis.com/books/ngrams/books/datasetsv2.html
    - Cryptography and Network Secuirty, William Stallings, 7th Edition
    - http://vanilla47.com/PDFs/Cryptography/Cryptoanalysis/A%20Fast%20Method%20for%20Cryptoanalysis%20of%20Substitution%20Ciphers.pdf
        - http://www.tandfonline.com/doi/abs/10.1080/0161-119591883944
    - http://norvig.com/mayzner.html
    - http://www.data-compression.com/english.html
    - http://quipqiup.com/
    - http://www.ti89.com/cryptotut/frequencies.htm
    - http://altamatic.com/crypt

# License:

This application(s) is/are covered by the Creative Commons BY-SA license.

- https://creativecommons.org/licenses/by-sa/4.0/
- https://creativecommons.org/licenses/by-sa/4.0/legalcode
