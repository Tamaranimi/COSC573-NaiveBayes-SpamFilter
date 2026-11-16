# Naive Bayes Spam Filter — COSC 573

A Python implementation of a **multinomial Naive Bayes** spam filter using the `SpamHam` assignment template and word-count files sourced from the SpamAssassin project. The original assignment includes two labeled example messages and a local test runner. This repository also includes reproducible diagnostic experiments and their recorded results.

## Project overview

The classifier reads word frequencies from `spamcount.txt` and `hamcount.txt`, estimates class-conditional word likelihoods, and computes the posterior probability that an input message is spam. It uses equal priors, a likelihood floor of `1e-5` for unseen or low-probability tokens, and log-probabilities to prevent numerical underflow.

The main implementation is in `src/spamham.py`, specifically `SpamHam.evaluate(words)`.

The theoretical basis for the classifier includes Bayes' rule and naive Bayes models, as discussed in Chapter 12, Sections 12.5–12.6, of Russell and Norvig's *Artificial Intelligence: A Modern Approach* (4th ed., Global ed.).

## Requirements

* Python 3 (standard library only)
* No additional pip packages required

## Run

From the repository root, run:

```powershell
cd SpamHam
python3 src/main.py
python3 run_experiments.py
python3 -m testrunner
```

On Windows, `python` or `py -3` can be used instead of `python3` if needed.

## Verified results

| Input | Computed spam probability | Interpretation |
|---|---:|---|
| `spamesim.txt` | `1.0` (floating-point rounded) | Spam |
| `hamesim.txt` | `3.641589521379177e-46` | Ham |

The two included instructor tests passed locally (`2/2`). These are **two sample checks**, not evidence of general classification accuracy. The experiment script evaluates 13 cases total, but only the two supplied messages have provided class labels; the other 11 cases are controlled diagnostics.

## Results and files

* `src/spamham.py` — classifier implementation
* `src/main.py` — example runner
* `spamcount.txt`, `hamcount.txt` — training word counts
* `spamesim.txt`, `hamesim.txt` — example messages
* `test/`, `testrunner/` — instructor-supplied testing infrastructure
* `run_experiments.py` — reproducible diagnostic experiments
* `experiment_results/classifications.csv` — classification results
* `experiment_results/word_probabilities.csv` — selected word likelihoods
* `experiment_results/RESULTS.md` — results interpretation
* `PROJECT_NOTES.md` — implementation details and limitations

## Limitations

The supplied code uses whitespace-only tokenization, so capitalization and punctuation can change outcomes. Fixed probability flooring is not the same as normalized Laplace smoothing. The supplied word-count files do not establish message-level prior frequencies. A larger, independently labeled dataset would be needed for robust precision, recall, or F1 evaluation.

## Source and attribution

* Assignment starter archive: [SpamHam.zip](https://materiaalit.github.io/intro-to-ai/files/tests/SpamHam.zip), from [Introduction to AI course materials](https://materiaalit.github.io/intro-to-ai/).
* Word-count data provenance, as stated by the assignment: [Apache SpamAssassin](https://spamassassin.apache.org/).
* Russell, S. J., & Norvig, P. (2022). *Artificial Intelligence: A Modern Approach* (4th ed., Global ed.). Pearson. See Chapter 12, Sections 12.5–12.6, on Bayes' rule and naive Bayes models.
* Raschka, S. *Naive Bayes and Text Classification I — Introduction and Theory*. [arXiv:1410.5329](https://arxiv.org/abs/1410.5329).
* Sahami, M., Dumais, S., Heckerman, D., & Horvitz, E. (1998). *A Bayesian Approach to Filtering Junk E-Mail*. [AAAI Workshop paper](https://cdn.aaai.org/Workshops/1998/WS-98-05/WS98-05-009.pdf).

This repository incorporates educational starter materials. Consult the upstream sources for their applicable reuse and licensing terms before redistributing them. The Russell and Norvig textbook is cited as a reference; its PDF is not included in this repository.
