import os
import math

SMALL_NUMBER = 0.00001


def get_occurrences(filename):
    results = {}
    dir_path = os.path.dirname(os.path.realpath(__file__))

    try:
        with open(os.path.join(dir_path, '..', filename)) as file:
            for line in file:
                count, word = line.strip().split(' ')
                results[word] = int(count)

        return results

    except FileNotFoundError:
        print("File %s was not found." % filename)
        raise
    except Exception as e:
        print("Something terrible happened: %s" % str(e))
        raise


def get_words(filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    try:
        with open(os.path.join(dir_path, '..', filename)) as file:
            words = [word for line in file for word in line.split()]

        return words

    except FileNotFoundError:
        print("File %s was not found." % filename)
        raise
    except Exception as e:
        print("Something terrible happened: %s", str(e))
        raise


class SpamHam:
    """ Naive Bayes spam filter
        :attr spam: dictionary of occurrences for spam messages {word: count}
        :attr ham: dictionary of occurrences for ham messages {word: count}
    """

    def __init__(self, spam_file, ham_file):
        self.spam = get_occurrences(spam_file)
        self.ham = get_occurrences(ham_file)

    def evaluate_from_file(self, filename):
        words = get_words(filename)
        return self.evaluate(words)

    def evaluate_from_input(self):
        words = input().split()
        return self.evaluate(words)

    def evaluate(self, words):
        """
        :param words: Array of str
        :return: probability that the message is spam (float)
        """
        # The supplied files contain word occurrence counts, not probabilities.
        # Sum the counts separately for spam and legitimate (ham) messages.
        total_spam = sum(self.spam.values())
        total_ham = sum(self.ham.values())

        # Use equal prior probabilities because the template does not supply
        # the numbers of spam and ham training messages.
        log_spam = math.log(0.5)
        log_ham = math.log(0.5)

        # Multinomial Naive Bayes: each occurrence contributes evidence.
        # Log probabilities prevent underflow on long messages.
        for word in words:
            spam_likelihood = self.spam.get(word, 0) / total_spam
            ham_likelihood = self.ham.get(word, 0) / total_ham

            # Bound very small/unseen word likelihoods to avoid log(0).
            spam_likelihood = max(spam_likelihood, SMALL_NUMBER)
            ham_likelihood = max(ham_likelihood, SMALL_NUMBER)

            log_spam += math.log(spam_likelihood)
            log_ham += math.log(ham_likelihood)

        # Convert log-scores into a stable posterior probability of spam.
        # This avoids exponentiating the extremely negative log-scores.
        log_odds = log_ham - log_spam
        if log_odds >= 0:
            return math.exp(-log_odds) / (1.0 + math.exp(-log_odds))
        return 1.0 / (1.0 + math.exp(log_odds))
