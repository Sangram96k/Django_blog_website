import textstat
from collections import Counter
import re

class ContentOptimizer:
    def __init__(self, text):
        self.text = text

    def analyze(self):
        suggestions = []

        # Check readability
        readability_score = textstat.flesch_reading_ease(self.text)
        if readability_score < 60:
            suggestions.append("Improve readability. Current score is below 60.")

        # Check sentence length
        avg_sentence_length = textstat.avg_sentence_length(self.text)
        if avg_sentence_length > 20:
            suggestions.append("Reduce average sentence length. Current average is above 20 words.")

        # Check for difficult words
        difficult_words = textstat.difficult_words(self.text)
        if difficult_words > 10:
            suggestions.append(f"Reduce the number of difficult words. Current count is {difficult_words}.")

        # Check for passive voice
        passive_voice_count = self.count_passive_voice()
        if passive_voice_count > 0:
            suggestions.append(f"Reduce passive voice usage. Current count is {passive_voice_count}.")

        # Check keyword density
        keyword_density = self.check_keyword_density()
        if keyword_density:
            suggestions.append(f"Keyword density is too high for: {', '.join(keyword_density)}")

        # Check for stop words
        stop_word_percentage = self.calculate_stop_word_percentage()
        if stop_word_percentage > 50:
            suggestions.append(f"Reduce stop words. Current percentage is {stop_word_percentage:.2f}%.")

        return suggestions

    def count_passive_voice(self):
        # Naive check for passive voice using regex
        passive_voice_regex = re.compile(r'\b(?:is|are|was|were|be|been|being)\b\s+\w+\b(?:ed|en)\b', re.IGNORECASE)
        matches = passive_voice_regex.findall(self.text)
        return len(matches)

    def check_keyword_density(self):
        # Example keywords, this can be dynamic based on user input or specific context
        keywords = ['example', 'keyword']
        word_list = re.findall(r'\b\w+\b', self.text.lower())
        word_count = Counter(word_list)
        total_words = len(word_list)
        high_density_keywords = []

        for keyword in keywords:
            density = (word_count[keyword] / total_words) * 100
            if density > 2:  # Consider 2% as a threshold for keyword stuffing
                high_density_keywords.append(keyword)

        return high_density_keywords

    def calculate_stop_word_percentage(self):
        # Example stop words, this list can be expanded
        stop_words = {'a', 'the', 'is', 'in', 'at', 'of', 'on', 'and', 'or', 'an'}
        word_list = re.findall(r'\b\w+\b', self.text.lower())
        stop_word_count = sum(1 for word in word_list if word in stop_words)
        total_words = len(word_list)

        return (stop_word_count / total_words) * 100 if total_words > 0 else 0
