# Naive Bayes SpamHam — Project notes

## How to run
From this `SpamHam` directory:

```bash
python3 -m testrunner
python3 src/main.py
```

`src/main.py` prints the posterior probability of spam for `spamesim.txt` and then `hamesim.txt`.

## What was changed
Only the classifier implementation in `src/spamham.py` was edited: `math` was imported and the `evaluate(self, words)` method was implemented. The provided training counts, sample messages, test suite, and entrypoint were preserved.

## Method
- Multinomial Naive Bayes with observed word counts.
- Per-class word probability: `count(word, class)/sum(all counts in class)`.
- Equal class priors: `P(spam)=P(ham)=0.5` (class message counts were not provided).
- Each message token is included, including repeated tokens, matching the supplied `get_words` behavior.
- Per-class likelihoods below `SMALL_NUMBER = 0.00001` are floored to that constant, as suggested by the exercise. This is probability flooring, not Laplace smoothing.
- Log probabilities are accumulated and normalized using a numerically stable logistic calculation.
- `evaluate` returns a floating-point posterior probability of spam in `[0,1]`; a probability above 0.5 is classified as spam.

## Verified on the supplied dataset
- Spam: 6,245 unique tokens, 75,268 word occurrences.
- Ham: 16,207 unique tokens, 290,673 word occurrences.
- `P(free|spam) = 624/75268 = 0.008290...`.
- `spamesim.txt`: `1.0`, spam.
- `hamesim.txt`: `3.641589521379177e-46`, ham.
- Local instructor tests: 2/2 passed with `python3 -m testrunner`.
- Additional smoke checks: empty input -> 0.5; unknown word -> 0.5; probability stays in valid range for a long repeated unseen-word message.

## Limitations and improvements
- The supplied training data contains word counts rather than the actual training documents, so real prior class frequencies cannot be estimated directly.
- The template splits text on whitespace, retaining punctuation and capitalization, which can reduce token matching.
- Unknown words and small likelihoods share a fixed floor of `1e-5`, a pragmatic approximation rather than a fully smoothed probability distribution.
- Two instructor test messages demonstrate basic correctness but do not establish generalization accuracy or precision/recall on a held-out labeled dataset.
- Future improvements could compare Laplace smoothing, normalized tokenization, nonuniform empirically estimated priors, threshold selection, and evaluations on a larger labeled corpus.
