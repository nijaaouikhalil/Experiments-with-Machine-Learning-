from __future__ import division
from collections import Counter
from codecs import open

def read_documents(doc_file):
    docs = []
    labels = []
    categories = []
    with open(doc_file, encoding='utf-8') as f:
        for line in f:
            words = line.strip().split()
            docs.append(words[3:])
            labels.append(words[1])
            categories.append(words[0])
    return docs, labels, categories




all_docs, all_labels, all_categories = read_documents('data_set_raw.txt')
split_point = int(0.80*len(all_docs))
train_docs = all_docs[:split_point]
train_labels = all_labels[:split_point]
eval_docs = all_docs[split_point:]
eval_labels = all_labels[split_point:]

#for line in train_docs:
#    print(Counter(line))

print(Counter(all_categories))