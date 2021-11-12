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

coca_dict = defaultdict(list)
query_pos = "NOUN"

with open("noun-list.txt", "r") as f:
    nouns = f.read().splitlines()

for query in nouns:
    print('Query:', query)
    with open("pkl/coca-fiction-stanza.pkl", "rb") as fr:
        try:
            while True:
                doc = pkl.load(fr)
                for sent in tqdm(doc.sentences, leave=False):
                    sample = collect_sample(sent, query, query_pos)
                    if sample:
                        coca_dict[query].append(sent.text)
                    else:
                        continue
        except EOFError:
            pass

with open("pkl/coca-dict.pkl", "wb") as f:
    pkl.dump(coca_dict, f)

