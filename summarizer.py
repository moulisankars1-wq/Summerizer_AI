print("\n====== TEXT SUMMARIZATION TOOL ======")
print("Developed by : Moulisankar\n")

text = input("Enter your paragraph:\n")

sentences = text.split('.')

word_freq = {}

for sentence in sentences:
    words = sentence.split()
    for word in words:
        word = word.lower()
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

sentence_score = {}

for sentence in sentences:
    words = sentence.split()
    for word in words:
        word = word.lower()
        if word in word_freq:
            if sentence in sentence_score:
                sentence_score[sentence] += word_freq[word]
            else:
                sentence_score[sentence] = word_freq[word]

sorted_sentences = list(sentence_score.items())
sorted_sentences.sort(key=lambda x: x[1], reverse=True)

print("\n------ SUMMARY ------\n")

result = sorted_sentences[0][0] + "." + sorted_sentences[1][0] + "."
print(result)

file = open("summary.txt", "w")
file.write("Student Name: Moulisankar\n\n")
file.write("Original Text:\n" + text + "\n\n")
file.write("Summary:\n" + result)
file.close()

print("\nSummary Saved in summary.txt")
