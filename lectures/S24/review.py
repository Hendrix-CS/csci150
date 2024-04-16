words = {"a": 0, "an": 0, "the": 0, "and": 0, "or": 0, "is": 0, "on": 0}
text1 = "the elephant is an animal that is the largest on land and "
text2 = "the blue whale is the largest on land or sea"
text = text1 + text2

for word in text.split():
    if word in words:
        words[word] += 1

for word in words:
    print(word, words[word])