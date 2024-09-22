#Example 1: Creating a set with duplicate elements

unique_numbers = {1, 2, 3, 4, 5}
print("Unique Numbers:", unique_numbers)

#Example 2: Using set() constructor
programming_languages = set(["Python", "Java", "C++"])
print("Programming Languages:", programming_languages)

#Example 3: Creating an empty set

empty_set = set()
print("Empty Set:", empty_set)

#Example 4: Creating an immutable set
immutable_set = frozenset [18, 20, 30]
print("Immutable Set:", immutable_set)




def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)


text_input = ("Python is a high-level programming language. "
              "Python's simplicity and flexibility make it a popular programming language. "
              "Learning Python is essential for mastering web development, data science, and automation tasks.")

unique_words_count = count_unique_words(text_input)
print("Number of unique words: ", unique_words_count)

