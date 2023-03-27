import os
import argparse
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import csv
import re
from collections import defaultdict

# Useful if you want to perform stemming.
import nltk
stemmer = nltk.stem.PorterStemmer()

categories_file_name = r'/workspace/datasets/product_data/categories/categories_0001_abcat0010000_to_pcmcat99300050000.xml'

queries_file_name = r'/workspace/datasets/train.csv'
output_file_name = r'/workspace/datasets/fasttext/labeled_queries.txt'

parser = argparse.ArgumentParser(description='Process arguments.')
general = parser.add_argument_group("general")
general.add_argument("--min_queries", default=1,  help="The minimum number of queries per category label (default is 1)")
general.add_argument("--output", default=output_file_name, help="the file to output to")

args = parser.parse_args()
output_file_name = args.output

if args.min_queries:
    min_queries = int(args.min_queries)

# The root category, named Best Buy with id cat00000, doesn't have a parent.
root_category_id = 'cat00000'

tree = ET.parse(categories_file_name)
root = tree.getroot()

# Parse the category XML file to map each category id to its parent category id in a dataframe.
categories = []
parents = []
for child in root:
    cat_path = child.find('path')
    cat_path_ids = [cat.find('id').text for cat in cat_path]
    leaf_id = cat_path_ids[-1]
    if leaf_id != root_category_id:
        categories.append(leaf_id)
        parents.append(cat_path_ids[-2])
parents_df = pd.DataFrame(list(zip(categories, parents)), columns =['category', 'parent'])

# Read the training data into pandas, only keeping queries with non-root categories in our category tree.
queries_df = pd.read_csv(queries_file_name)[['category', 'query']]
queries_df = queries_df[queries_df['category'].isin(categories)]

NON_ALPHA = re.compile(r"[^a-zA-Z0-9_]")
COMBINE_WHITESPACE = re.compile(r"\s+")

def normalize(query: str):
    result = query.strip()
    result = NON_ALPHA.sub(" ", result)
    result = COMBINE_WHITESPACE.sub(" ", result)
    result = stemmer.stem(result, to_lowercase=True)
    return result

queries_df['query'] = queries_df['query'].apply(normalize)

parents_dict = dict(parents_df.set_index('category')['parent'])
category_counts = defaultdict(int)
category_counts.update(queries_df.category.value_counts())

while True:
    small = [category for category, count in category_counts.items() if count < min_queries]
    if not small:
        break
    for category in small:
        category_counts[parents_dict[category]] += category_counts.pop(category)

widener = {}
for category in categories:
    widened_category = category
    while widened_category not in category_counts:
        widened_category = parents_dict[widened_category]
    widener[category] = widened_category

queries_df['category'] = queries_df['category'].apply(lambda category: widener[category])
# Create labels in fastText format.
queries_df['label'] = '__label__' + queries_df['category']

# Output labeled query data as a space-separated file, making sure that every category is in the taxonomy.
queries_df = queries_df[queries_df['category'].isin(categories)]
queries_df['output'] = queries_df['label'] + ' ' + queries_df['query']
queries_df[['output']].to_csv(output_file_name, header=False, sep='|', escapechar='\\', quoting=csv.QUOTE_NONE, index=False)
