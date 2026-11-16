# Reproducible experiment results

Run `python run_experiments.py` from the SpamHam project directory.

- Spam vocabulary: 6,245 words; total occurrences: 75,268.
- Ham vocabulary: 16,207 words; total occurrences: 290,673.
- Used prior: P(spam)=P(ham)=0.5.
- Probability floor: 1e-05.
- Decision rule: spam if P(spam | message) > 0.5; ham if lower; tie at 0.5.

## Test outcomes

| Case | Words | P(spam | message) | Predicted |
|---|---:|---:|---|
| instructor_spam | 140 | 1.0 | spam |
| instructor_ham | 232 | 3.641589521379177e-46 | ham |
| empty_input | 0 | 0.5 | tie (0.5) |
| unseen_word | 1 | 0.5 | tie (0.5) |
| spam_signal_free | 1 | 0.8461964369830097 | spam |
| ham_signal_linux | 1 | 0.4061758873790851 | ham |
| spam_signal_money | 1 | 0.9064520798703553 | spam |
| ham_signal_listinfo | 1 | 0.15956205163449894 | ham |
| mixed_free_linux | 2 | 0.7900585578129616 | spam |
| repeat_free_5 | 5 | 0.9998016693304197 | spam |
| capitalized_Free | 1 | 0.5 | tie (0.5) |
| punctuated_free | 1 | 0.5 | tie (0.5) |
| unseen_repeated_1000 | 1000 | 0.5 | tie (0.5) |

**Interpretation:** Only the instructor's two sample messages have provided class labels.
The other entries are controlled diagnostics, not a held-out test set or evidence of overall model accuracy.
A `1.0` posterior may reflect floating-point rounding and should not be described as logical certainty.
Word likelihood estimates in `word_probabilities.csv` include both raw frequencies and the floored likelihood actually used by the classifier.
Because the fixed floor is applied to every very rare/missing word, these floored likelihoods do not necessarily sum to one.
The original whitespace tokenization is case- and punctuation-sensitive.
