import fasttext
import csv

model = fasttext.load_model("/workspace/datasets/fasttext/title_model.bin")
synonyms = []
with open("/workspace/datasets/fasttext/top_words.txt", "r") as top_words:
    for word in top_words:
        neighbors = [synonym
            for similarity, synonym in model.get_nearest_neighbors(word)
            if similarity > 0.75
        ]
        if neighbors:
            synonyms.append([word.strip(), *neighbors])

with open("/workspace/datasets/fasttext/synonyms.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(synonyms)