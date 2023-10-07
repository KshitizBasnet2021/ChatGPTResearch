import difflib

def getClosetFunctionName(word_list, target_word):

    # Minimum similarity score threshold (adjust as needed)
    min_similarity_score = 0.7

    # Calculate the similarity score for each word in the list
    similar_words = []
    for word in word_list:
        similarity_score = difflib.SequenceMatcher(None, target_word, word).ratio()
        if similarity_score >= min_similarity_score:
            similar_words.append((word, similarity_score))

    # Sort similar words by similarity score in descending order
    similar_words.sort(key=lambda x: x[1], reverse=True)
    print(word_list)
    print(similar_words)
    if(len(similar_words)==0): 
        return list(word_list)[0]
    # Print similar words and their similarity scores
    return similar_words[0]
