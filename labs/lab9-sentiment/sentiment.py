def read_movie_reviews(review_file):
    word_scores = {}
    word_counts = {}

    f = open(review_file, 'r')
    for line in f.readlines():
        words = line.split()
        score = int(words[0])
        for word in words[1:]:
            word_l = word.lower()
            if word_l not in word_scores:
                word_scores[word_l] = 0
                word_counts[word_l] = 0
            word_scores[word_l] += score
            word_counts[word_l] += 1

    for word in word_scores:
        word_scores[word] /= float(word_counts[word])

    return word_scores

def score_phrase(phrase, word_scores):
    score = 0
    for word in phrase.split():
        if not word in word_scores:
            score += 2
        else:
            score += word_scores[word]
    return score / len(phrase.split())

def main():
    word_scores = read_movie_reviews('movieReviews.txt')

    phrase = raw_input("Please enter a phrase: ")
    score = score_phrase(phrase, word_scores)
    if score < 2:
        print "Negative =("
    else:
        print "Positive =)"

main()
