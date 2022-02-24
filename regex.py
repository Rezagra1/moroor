# regex : regular exprestion


^the : start with "the"
$that : Ends with "that"
$ ta akhar khat miravad

. : every thing

\s  : white space
\w : word
\d digit

* : 0 or more
+ : 1 or more
[abc] : exiting a or b or c

[^abc] : not exiting a  , b and c

\t : tab
\n : new line

{n}: n ta
{2,5} : 2-5 ta

greedy = حريص , regex is greedy - insert ? to not be greedy

[A-Z] : A ta Z

(): gorooh bandi

import re
re.search() : # search re.search(r'.*', str)
re.findall(): # find re.findall(r'.*', str)
re.sub() : # replace re.sub(r'[sS]alam', 'hi, str)
# re.sub(r'hello (*.)', hi g<1> , str) #### g<1> jahat eshare be gorooh 






