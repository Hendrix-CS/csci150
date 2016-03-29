import os

def score_word(word):
    word = word.lower()

    reviews_file = open("movieReviews.txt", "r")

    total_score = 0
    num_reviews = 0
    for line in reviews_file.readlines():
        line = line.lower()
        words = line.split()
        if word in words[1:]:
            total_score += int(words[0])
            num_reviews += 1
    if num_reviews == 0:
        return None
    else:
        return float(total_score) / num_reviews

def score_user_word():
    word = raw_input("Please enter a word: ")
    score = score_word(word)
    if (score == None):
        print "Sorry, that word is not in the database."
    else:
        print "Score: " + str(score)
        pos_neg(score)

def pos_neg(score):
    if score < 2:
        print "Negative. =("
    else:
        print "Positive! =)"

def score_phrase(phrase):
    phrase = phrase.lower()
    words = phrase.split()
    total_score = 0
    word_count = 0
    for word in words:
        score = score_word(word)
        if score != None:
            word_count += 1
            total_score += score
    if (word_count == 0):
        return None
    else:
        return total_score/word_count

def score_user_phrase():
    phrase = raw_input("Please enter a word or phrase: ")
    score = score_phrase(phrase)
    if (score == None):
        print "Sorry, none of those words are in the database."
    else:
        print "Score: " + str(score)
        pos_neg(score)

def read_movie_reviews(review_file):
    cache_file_name = review_file + ".cached"
    if os.path.isfile(cache_file_name):
        print "Reading cached word score data..."
        word_scores = {}
        word_data_file = open(cache_file_name, 'r')
        for line in word_data_file.readlines():
            data = line.split()
            word_scores[data[0]] = float(data[1])
        return word_scores
    else:
        print "No cache found."
        print "Reading review data..."
        word_scores = parse_movie_reviews('movieReviews.txt')
        print "Saving data for later use..."
        word_data_file = open(cache_file_name, 'w')
        for word in word_scores:
            word_data_file.write(word + " " + str(word_scores[word]) + "\n")
        return word_scores

def parse_movie_reviews(review_file):
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

def score_phrase_dict(word_scores, phrase):
    phrase = phrase.lower()
    words = phrase.split()
    total_score = 0
    word_count = 0
    for word in words:
        if word in word_scores:
            word_count += 1
            total_score += word_scores[word]
    if (word_count == 0):
        return None
    else:
        return total_score/word_count

def main():

    word_scores = read_movie_reviews('movieReviews.txt')

    phrase = ""
    while phrase != "quit":
        phrase = raw_input("Please enter a phrase, or 'quit': ")
        if phrase != 'quit':
            score = score_phrase_dict(word_scores, phrase)
            if (score == None):
                print "None of those words are in the database."
            elif score < 2:
                print "Negative =("
            else:
                print "Positive =)"

main()
