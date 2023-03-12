## For classifying product names to categories: What precision (P@1) were you able to achieve?
P@1     0.966
## For classifying product names to categories: What fastText parameters did you use?
-epoch 25 -lr 1.0 -wordNgrams 2
## For classifying product names to categories: How did you transform the product names?
I noticed that `transform()` function was noop and added `strip()` and `lower()` thereto. This, however, is redundant in case of normalization using `sed`.
## For classifying product names to categories: How did you prune infrequent category labels, and how did that affect your precision?
By only including categories with more than 500 products. It improved P@1 from 0.655 to 0.966.
## For classifying product names to categories: How did you prune the category tree, and how did that affect your precision?
Skipped
## For deriving synonyms from content: What were the results for your best model in the tokens used for evaluation?
**laptop**
laptops 0.760666
notebook 0.721517
netbook 0.670614
macbook 0.611353
netbooks 0.593329
notebooks 0.577809
dell 0.543332
briefcase 0.540654
mouse 0.527199
inspiron 0.526445

**kodak**
easyshare 0.80092
canon 0.606203
photosmart 0.568195
photo 0.541945
powershot 0.529482
share 0.498171
coolpix 0.497834
epson 0.496415
finepix 0.488568
frame 0.480553

**stratocaster** 🤦‍♂️
roaster 0.65434
toaster 0.621825
strategy 0.620023
crock 0.60568
slow 0.602313
rice 0.598768
toasters 0.598217
straps 0.593189
pots 0.583317
cooker 0.578714

## For deriving synonyms from content: What fastText parameters did you use?
-minCount 98 -epoch 27
## For deriving synonyms from content: How did you transform the product names?
lowercase, remove punctuation and special characters, drop words less than 4 symbols
## For integrating synonyms with search: How did you transform the product names (if different than previously)?
Didn't change
## For integrating synonyms with search: What threshold score did you use?
0.75
## For integrating synonyms with search: Were you able to find the additional results by matching synonyms?
Affirmative.

query | without | with
--- | --- | ---
earbuds | 1205 | 1723
nespresso 🤷‍♂️ | 8 | 8
dslr | 2837 | 3140

## For classifying reviews: What precision (P@1) were you able to achieve?
Lower-case and trim **both title and comment**
Shuffle, head 20000 as training data and tail **1000** as test data
P@1     0.688

Lower-case and trim **both title and comment**
Shuffle, head 20000 as training data and tail **20000** as test data
P@1     0.68

Lower-case and trim **only title**
Shuffle, head 20000 as training data and tail **20000** as test data
P@1     0.648

## For classifying reviews: What fastText parameters did you use?
Lower-case and trim **both title and comment**
Shuffle, head 20000 as training data and tail **1000** as test data
-lr 1.0 -epoch 14 -wordNgrams 3

Lower-case and trim **both title and comment**
Shuffle, head 20000 as training data and tail **20000** as test data
-lr 1.0 -epoch 23 -wordNgrams 2

Lower-case and trim **only title**
Shuffle, head 20000 as training data and tail **20000** as test data
-lr 1.0 -epoch 19 -wordNgrams 2

## For classifying reviews: What else did you try and learn?
I thought shorter titles are easier to correlate with reviews since they tend to use strong and meaningful adjectives, but apparently 🤷‍♂️