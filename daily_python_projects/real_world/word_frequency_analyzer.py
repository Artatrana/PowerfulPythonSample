# The program should:
#
# Accept text input from the user (or read from a file)
# Clean the text by removing punctuation and converting to lowercase
# Count the frequency of each word
# Display the most common words in a formatted report
# Show basic text statistics (total words, unique words, etc.)
# Bonus (optional):
#
# Filter out common stop words (the, and, of, etc.)
# Create a simple bar chart of word frequencies
# Save results to a file
# Find the longest and shortest words
# This project gives you hands-on practice with dictionaries, string processing, and data analysis — essential skills
# for text mining, content analysis, and natural language processing.

import string
import re
from collections import Counter

class TextAnalyzer:

    def __init__(self):
        # Common English stop words
        self.stop_words = {
            'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with',
            'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had',
            'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might',
            'can', 'must', 'a', 'an', 'this', 'that', 'these', 'those', 'i', 'you',
            'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'
        }

    def clean_text(selft, text:str):
        # remove punctuation and convert to lower case
        text = re.sub(r'[\w\s]', '',text.lower())
        # Split into words and remove empty strings
        words = [word for word in text.split() if word]
        return words

    def filter_stop_words(self, words):
        return [word for word  in words if word not in self.stop_words]

    def analyze(self, text, remove_stop_words=None):
        words = self.clean_text(text)

        if remove_stop_words:
            filtered_words = self.filter_stop_words(words)
        else:
            filtered_words = words

        if not filtered_words:
            return None

        # Statistics
        total_words = len(words)
        total_filtered = len(filtered_words)
        unique_words = len(set(filtered_words))
        avg_length = sum(len(word) for word in filtered_words) / total_filtered

        # Frequency analysis
        word_count = Counter(filtered_words)
        most_common = word_count.most_common(10)

        # Word length analysis
        longest = max(filtered_words, key=len)
        shortest = min(filtered_words, key=len)

        return {
            'total_original': total_words,
            'total_filtered': total_filtered,
            'unique': unique_words,
            'avg_length': avg_length,
            'most_common': most_common,
            'longest': longest,
            'shortest': shortest,
            'stop_words_removed': remove_stop_words
        }

    def display_results(self, results):
        if not results:
            print("No valid words found to analyze.")
            return

        print("\n=== Advanced Word Frequency Analysis ===")
        print(f"Total words (original): {results['total_original']}")

        if results['stop_words_removed']:
            print(f"Total words (after removing stop words): {results['total_filtered']}")
        print(f"Unique words: {results['unique']}")
        print(f"Average word length: {results['avg_length']:.1f}")

        print(f"\nTop {min(10, len(results['most_common']))} Most Common Words:")
        for i, (word, count) in enumerate(results['most_common'],1):
            percentage = (count / results['total_filtered']) * 100
            print(f"{i:2d}. {word:<12}: {count:3d} times ({percentage:5.2f}%)")

        print(f"\nWord Length Analysis:")
        print(f"Longest word: {results['longest']} ({len(results['longest'])} letters)")
        print(f"Shortest word: {results['shortest']} ({len(results['shortest'])} letters)")

# Main program
analyzer = TextAnalyzer()

print("=== Text Analysis Tool ===")
text = input("Enter your text: ")
remove_stop = input("Remove common stop words? (y/n): ").lower() == 'y'

results = analyzer.analyze(text, remove_stop_words=remove_stop)
analyzer.display_results(results)




