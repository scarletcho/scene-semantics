import stanza
import os
import pickle as pkl
from tqdm import tqdm

nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma', logging_level='DEBUG')

doc_list = []
fiction_list = os.listdir("fiction_refined")

for fiction in tqdm(fiction_list):
    with open("fiction_refined/" + fiction, "r") as f:
        documents = f.readlines()

    in_docs = [stanza.Document([], text=d) for d in documents] # Wrap each document with a stanza.Document object
    out_docs = nlp(in_docs) # Call the neural pipeline on this list of documents

    doc_list.extend(out_docs)

with open("pkl/coca-fiction.pkl", "wb") as f:
    pkl.dump(doc_list, f)

