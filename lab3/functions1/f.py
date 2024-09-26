def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

# Example usage:
sentence = "We are ready"
print(reverse_sentence(sentence))  # Output: "ready are We"
