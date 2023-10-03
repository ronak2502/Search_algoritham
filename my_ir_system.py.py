import os
import re
import argparse
import time

# task-1
def stem_word(word):
    """
    Apply Porter stemming algorithm to a given word.
    """
    stem = word

   # Step 1a
    if stem.endswith("sses"):
        stem = stem[:-4]
    elif stem.endswith("ies"):
        stem = stem[:-3]
    elif stem.endswith("ss"):
        stem = stem
    elif stem.endswith("s"):
        stem = stem[:-1]

    # Step 1b
    if re.search(r"[aeiouy]", stem):
        if stem.endswith("eed"):
            stem = stem[:-1]
        elif stem.endswith(("ed", "ing")):
            stem_candidate = stem[:-2]
            if re.search(r"[aeiouy]", stem_candidate):
                stem = stem_candidate
                if stem.endswith(("at", "bl", "iz")):
                    stem += "e"
                elif stem.endswith((stem[-1], stem[-2])) and not re.search(r"[aeiouy]", stem[:-2]):
                    stem = stem[:-1]
                    if stem.endswith("l") and len(stem) >= 3 and re.search(r"[aeiouy]", stem[:-1]):
                        stem = stem[:-1]  # def remove_stop_words(text):

   # Step 1c
    if re.search(r"[aeiouy]", stem):
        if stem.endswith("y"):
            stem_candidate = stem[:-1]
            if re.search(r"[aeiouy]", stem_candidate):
                stem = stem_candidate

    # Step 2
    if re.search(r"[aeiouy]", stem):
        stem_candidate = stem
        if stem_candidate.endswith("ational"):
            stem = stem_candidate[:-5] + "e"
        elif stem_candidate.endswith("tional"):
            stem = stem_candidate[:-2]
        elif stem_candidate.endswith("enci"):
            stem = stem_candidate[:-1] + "e"
        elif stem_candidate.endswith("anci"):
            stem = stem_candidate[:-1] + "e"
        elif stem_candidate.endswith("izer"):
            stem = stem_candidate[:-1]
        elif stem_candidate.endswith("abli"):
            stem = stem_candidate[:-1] + "e"
        elif stem_candidate.endswith("alli"):
            stem = stem_candidate[:-2]
        elif stem_candidate.endswith("entli"):
            stem = stem_candidate[:-2]
        elif stem_candidate.endswith("eli"):
            stem = stem_candidate[:-2]
        elif stem_candidate.endswith("ousli"):
            stem = stem_candidate[:-2]
        elif stem_candidate.endswith("ization"):
            stem = stem_candidate[:-5] + "e"
        elif stem_candidate.endswith("ation"):
            stem = stem_candidate[:-3] + "e"
        elif stem_candidate.endswith("ator"):
            stem = stem_candidate[:-2]
        elif stem_candidate.endswith("alism"):
            stem = stem_candidate[:-3]
        elif stem_candidate.endswith("iveness"):
            stem = stem_candidate[:-4]
        elif stem_candidate.endswith("fulness"):
            stem = stem_candidate[:-4]
        elif stem_candidate.endswith("ousness"):
            stem = stem_candidate[:-4]
        elif stem_candidate.endswith("aliti"):
            stem = stem_candidate[:-3]
        elif stem_candidate.endswith("iviti"):
            stem = stem_candidate[:-3] + "e"
        elif stem_candidate.endswith("biliti"):
            stem = stem_candidate[:-5] + "le"

   # Step 3
    if re.search(r"[aeiouy]", stem):
        stem_candidate = stem
        if stem_candidate.endswith("icate"):
            stem = stem_candidate[:-3]
        elif stem_candidate.endswith("ative"):
            stem = stem_candidate[:-5]
        elif stem_candidate.endswith("alize"):
            stem = stem_candidate[:-3]
        elif stem_candidate.endswith("iciti"):
            stem = stem_candidate[:-3]
        elif stem_candidate.endswith("ical"):
            stem = stem_candidate[:-2]
        elif stem_candidate.endswith("ful"):
            stem = stem_candidate[:-3]
        elif stem_candidate.endswith("ness"):
            stem = stem_candidate[:-4]

   # Step 4
    if re.search(r"[aeiouy]", stem):
        stem_candidate = stem
        if stem_candidate.endswith("al"):
            stem = stem_candidate[:-2]
        elif stem_candidate.endswith("ance"):
            stem = stem_candidate[:-4]
        elif stem_candidate.endswith("ence"):
            stem = stem_candidate[:-4]
        elif stem_candidate.endswith("er"):
            stem = stem_candidate[:-2]
        elif stem_candidate.endswith("ic"):
            stem = stem_candidate[:-2]
        elif stem_candidate.endswith("able"):
            stem = stem_candidate[:-4]
        elif stem_candidate.endswith("ible"):
            stem = stem_candidate[:-4]
        elif stem_candidate.endswith("ant"):
            stem = stem_candidate[:-3]
        elif stem_candidate.endswith("ement"):
            stem = stem_candidate[:-5]
        elif stem_candidate.endswith("ment"):
            stem = stem_candidate[:-4]
        elif stem_candidate.endswith("ent"):
            stem = stem_candidate[:-3]
        elif stem_candidate.endswith(("ion", "sion", "tion")):
            stem = stem_candidate[:-3]
            if stem.endswith("t") and stem[-2] in "st":
                stem = stem[:-1]
        elif stem_candidate.endswith("ou"):
            stem = stem_candidate[:-2]
        elif stem_candidate.endswith("ism"):
            stem = stem_candidate[:-3]
        elif stem_candidate.endswith("ate"):
            stem = stem_candidate[:-3]
        elif stem_candidate.endswith("iti"):
            stem = stem_candidate[:-3]
        elif stem_candidate.endswith("ous"):
            stem = stem_candidate[:-3]
        elif stem_candidate.endswith("ive"):
            stem = stem_candidate[:-3]
        elif stem_candidate.endswith("ize"):
            stem = stem_candidate[:-3]

   # Step 5a
    if re.search(r"[aeiouy]", stem):
        stem_candidate = stem
        if stem_candidate.endswith("e"):
            stem = stem_candidate[:-1]
            if len(stem) >= 2 and not re.search(r"[aeiouy]", stem):
                stem = stem_candidate

    # Step 5b
    if re.search(r"[aeiouy]", stem):
        stem_candidate = stem
        if len(stem_candidate) >= 2 and stem_candidate[-1] == stem_candidate[-2] and not re.search(r"[aeiouy]", stem_candidate[:-2]):
            stem = stem_candidate[:-1]

    return stem


def linear_search(query, search_mode, model, documents, stemming):
    search_directory = 'collection_original' if documents == 'original' else 'collection_no_stopwords'

    # Prepare the query for matching
    keywords = query.lower().split()
    if stemming:
       stemmed_keywords = [stem_word(keyword) for keyword in keywords]
    else:
        stemmed_keywords = keywords
    print(stemmed_keywords)
    # Perform linear search
    matching_files = []
    for file_name in os.listdir(search_directory):
        file_path = os.path.join(search_directory, file_name)
        with open(file_path, 'r') as file:
            content = file.read().lower()
            if all(stemmed_keyword in content for stemmed_keyword in stemmed_keywords):
                # Include the matching search words
                matching_files.append(
                    (file_name, stemmed_keywords if stemming else keywords))

    # Print the matching file names and search words
    for file_name, search_words in matching_files:
        print(f"File: {file_name}")
        print(f"Matching Words: {' '.join(search_words)}")
        print()


# task2
def tokenize_query(query):
    tokens = query.split('&')
    return tokens


def inverted_search(query, search_mode, documents, model):
    search_directory = 'collection_original' if documents == 'collection_no_stopwords' else 'original'
    tokens = tokenize_query(query)
    result = None
    for term in tokens:
        if term[0] == '!':
            neg_term = term[1:]
            if neg_term in search_directory:
                neg_docs = set(search_directory[neg_term])
                if result is None:
                    result = set(documents.keys()) - neg_docs
                else:
                    result = result.intersection(set(documents.keys()) - neg_docs)
        else:
            if term in search_directory:
                term_docs = set(search_directory[term])
                if result is None:
                    result = term_docs
                else:
                    result = result.intersection(term_docs)
            else:
                # If any term is not found, return empty result
                return []
    if result is None:
        return []
    return [documents[doc_id] for doc_id in result]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--extract-collection', metavar='file_name')
    parser.add_argument('--query', metavar='QUERY_TEXT')
    parser.add_argument('--model', choices=['bool'])
    parser.add_argument('--search-mode', choices=['linear', 'inverted'])
    parser.add_argument('--documents', choices=['original', 'no_stopwords'])
    parser.add_argument('--orignal_file_name', metavar='orignal_file_name' )
    parser.add_argument('--stop_word_removel_file', metavar='stop_word_removel_file') 
    parser.add_argument('--stemming', action='store_true', help='Enable stemming for query and document terms')
    args = parser.parse_args()

    start_time = time.time()
    if args.search_mode == 'inverted':
        if args.query:
            query = args.query
            model = args.model
            search_mode = args.search_mode
            documents = args.documents
            stemming = args.stemming
            inverted_search(query, model, search_mode, documents)

    if args.search_mode == 'linear':
        if args.query:
            query = args.query
            model = args.model
            search_mode = args.search_mode
            documents = args.documents
            stemming = args.stemming
            linear_search(query, model, search_mode, documents, stemming)

    end_time = time.time()

    print(f'Time taken: T={int((end_time - start_time) * 1000)}ms')