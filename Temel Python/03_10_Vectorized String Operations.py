# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# %%
data = ['peter', 'Paul', 'MARY', 'gUIDO']

# %%
data = [s.capitalize() for s in data]

# %%
data = ['peter', None, '', 'gUIDO']
data = [s.capitalize() for s in data]

# %%
names = pd.Series(data)
print(names)

# %%
names = names.str.capitalize()
print(names)

# %%
# Monty Python and the Holy GrailIngiliz gercek ustu komedi filmi 1975
monte = pd.Series(['Graham Chapman', 'John Cleese', 'Terry Gilliam',
                   'Eric Idle', 'Terry Jones', 'Michael Palin'])

# len()	    lower()	        translate()	    islower()
# ljust()	upper()	        startswith()	isupper()
# rjust()	find()	        endswith()	    isnumeric()
# center()	rfind()	        isalnum()	    isdecimal()
# zfill()	index()	        isalpha()	    split()
# strip()	rindex()	    isdigit()	    rsplit()
# rstrip()	capitalize()   	isspace()	    partition()
# lstrip()	swapcase()	    istitle()   	rpartition()

# %%
print(monte.str.lower())
print(monte.str.len())
print(monte.str.startswith('T'))
print(monte.str.split()[0])

# %%
###############################
# Regular Expressions
###############################
# Method            Description
# match()           Call re.match() on each element, returning a boolean.
# extract()         Call re.match() on each element, returning matched groups as strings.
# findall()	        Call re.findall() on each element
# replace()	        Replace occurrences of pattern with some other string
# contains()	    Call re.search() on each element, returning a boolean
# count()	        Count occurrences of pattern
# split()	        Equivalent to str.split(), but accepts regexps
# rsplit()	        Equivalent to str.rsplit(), but accepts regexps


# %%
# Extract first name by asking for a contiguous group of characters at the beginning of each element
monte.str.extract('([A-Za-z]+)', expand=False)

# %%

monte.str.findall(r'^[^Te].*[^m]$')

# %%
monte.str[0:3]
print(monte.str.split().str.get(-1))

# %%
# Get Dummies actors appearing in episodes
full_monte = pd.DataFrame({'name': monte,
                           'episodes': ['2|3|4', '2|4', '1|3',
                                        '2|4', '2|3', '2|3|4']})

print(full_monte)

monte_dummies = full_monte['episodes'].str.get_dummies('|')

############################
# Recipe Database
############################
# %%
try:
    recipes = pd.read_json('dataFiles/recipeitems-latest.json')
except ValueError as e:
    print("ValueError:", e)

# %%
recipes.shape

# %%
recipes.ingredients.str.len().describe()
print(recipes.name[np.argmax(recipes.ingredients.str.len())])

# %%
spice_list = ['beef', 'pepper', 'oregano', 'sage', 'parsley',
              'rosemary', 'tarragon', 'thyme', 'paprika', 'cumin']
import re

spice_df = pd.DataFrame(dict((spice, recipes.ingredients.str.contains(spice, re.IGNORECASE))
                             for spice in spice_list))
print(spice_df)

# %%
from addict import Dict

mapping = Dict()
##############################