import collections

text = 'lorem ipsum dolor ipsum amet sit amet amet'
words = text.split()
counter = collections.Counter(words)
most_common , occurrences = counter.most_common()[0]

longest = max(words, key=len)

print(most_common, longest)