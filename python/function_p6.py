def read_data():
    docs = {}
    n = int(input().strip())
    for i in range(n):
        tokens = input().strip().split()        
        doc_name = tokens[0]
        doc_keywords = tokens[1:]
        for kword in doc_keywords:
            if kword in docs.keys():
                docs[kword].add(doc_name)
            else:
                docs[kword] = {doc_name}
    return docs

def search(docs,condition,search_key):
    target = [docs[e] for e in search_key if e in docs]
    if len(target) == 0 : return []
    if condition == 'and' :
        if len(target) != len(search_key) : return []
        return list(set.intersection(*target))
    elif condition == 'or':
        return list(set.union(*target))
    else : return []
    
docs = read_data()
tokens = input().split()
print(sorted(search(docs,tokens[0],tokens[1:])))
