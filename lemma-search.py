import pickle as pkl
from collections import defaultdict
from tqdm import tqdm

def collect_sample(sentence, query, query_pos):
    lemmas_in_sent = [w.lemma.lower() for w in sentence.words]
    try:
        i = lemmas_in_sent.index(query)
    except ValueError:
        return None

    word_pos = sent.words[i].pos
    if word_pos == query_pos:
        return sent.text
    else:
        return None

with open("pkl/coca-fiction.pkl", "rb") as f:
    coca = pkl.load(f)

with open("noun-list.txt", "r") as f:
    nouns = f.read().splitlines()

coca_dict = defaultdict(list)
query_pos = "NOUN"

for query in nouns:
    print('Query:', query)
    for doc in tqdm(coca):
        for sent in tqdm(doc.sentences, leave=False):
            sample = collect_sample(sent, query, query_pos)
            if sample:
                # key = '.'.join([query, query_pos])
                key = query
                coca_dict[key].append(sent.text)
            else:
                continue

with open("pkl/coca-dict.pkl", "wb") as f:
    pkl.dump(coca_dict, f)

