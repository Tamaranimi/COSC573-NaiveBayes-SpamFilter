#

# \# Naive Bayes Spam Filter â€” COSC 573

#

# \## Project Overview

#

# This project implements a \*\*Multinomial Naive Bayes spam filtering system using Python\*\* for COSC 573: Artificial Intelligence.

#

# The classifier distinguishes spam from legitimate (ham) messages using word-frequency information provided in the original SpamHam assignment package. The word-count data originates from materials associated with the Apache SpamAssassin project.

#

# The implementation uses Bayes' theorem, class-conditional word probabilities, logarithmic likelihood calculations, and a small probability floor to handle unseen or low-probability words.

#

# The repository includes the working classifier, original assignment files, instructor tests, additional diagnostic experiments, and recorded experimental results.

#

# \## Project Objectives

#

# 1\. Implement a Naive Bayes spam classifier using Python.

# 2\. Read and process spam and ham word-frequency data.

# 3\. Estimate conditional word probabilities for both classes.

# 4\. Calculate posterior spam probabilities for new messages.

# 5\. Classify messages as spam or ham.

# 6\. Verify the implementation using the instructor's automated tests.

# 7\. Examine the effects of individual words, word repetition, unknown words, capitalization, and punctuation.

#

# \## Dataset

#

# The assignment provides two word-count files:

#

# | Dataset Property | Spam | Ham |

# |---|---:|---:|

# | Unique words | 6,245 | 16,207 |

# | Total word occurrences | 75,268 | 290,673 |

#

# The files contain word frequencies after common stop words and words occurring only once were removed.

#

# The assignment also includes two example messages:

#

# \- `spamesim.txt` â€” spam message

# \- `hamesim.txt` â€” legitimate (ham) message

#

# These are the two labeled examples used by the instructor's local tests.

#

# \## Methodology

#

# The classifier estimates the likelihood of each word given its class:

#

# ```text

# P(word | spam) = spam word count / total spam word count

#

# P(word | ham)  = ham word count / total ham word count

# ```

#

# For example, the word `free` appears 624 times in the spam corpus:

#

# ```text

# P(free | spam) = 624 / 75268 â‰ˆ 0.00829

# ```

#

# The classifier combines the word likelihoods using the Naive Bayes conditional independence assumption.

#

# \### Model Configuration

#

# \- Classifier: Multinomial Naive Bayes

# \- Class priors: P(spam) = P(ham) = 0.5

# \- Probability floor: 0.00001 (1e-5)

# \- Numerical computation: Log-probabilities

# \- Classification threshold: 0.5

# \- Programming language: Python 3

# \- External Python packages: None

#

# Log-probabilities help prevent numerical underflow when processing messages containing many words.

#

# The probability floor prevents zero likelihoods for unseen or very low-probability tokens. This is a fixed flooring approach, not conventional normalized Laplace smoothing.

#

# \## Project Structure

#

# ```text

# COSC573-NaiveBayes-SpamFilter/

# â”‚

# â”œâ”€â”€ README.md

# â”‚

# â””â”€â”€ SpamHam/

# &#x20;   â”œâ”€â”€ src/

# &#x20;   â”‚   â”œâ”€â”€ \_\_init\_\_.py

# &#x20;   â”‚   â”œâ”€â”€ main.py

# &#x20;   â”‚   â””â”€â”€ spamham.py

# &#x20;   â”‚

# &#x20;   â”œâ”€â”€ test/

# &#x20;   â”œâ”€â”€ testrunner/

# &#x20;   â”‚

# &#x20;   â”œâ”€â”€ spamcount.txt

# &#x20;   â”œâ”€â”€ hamcount.txt

# &#x20;   â”œâ”€â”€ spamesim.txt

# &#x20;   â”œâ”€â”€ hamesim.txt

# &#x20;   â”‚

# &#x20;   â”œâ”€â”€ run\_experiments.py

# &#x20;   â”‚

# &#x20;   â”œâ”€â”€ experiment\_results/

# &#x20;   â”‚   â”œâ”€â”€ classifications.csv

# &#x20;   â”‚   â”œâ”€â”€ word\_probabilities.csv

# &#x20;   â”‚   â””â”€â”€ RESULTS.md

# &#x20;   â”‚

# &#x20;   â”œâ”€â”€ PROJECT\_NOTES.md

# &#x20;   â””â”€â”€ .gitignore

# ```

#

# \## Requirements

#

# \- Python 3

# \- Git (for cloning the repository)

# \- Windows, Linux, or macOS

#

# No additional Python packages are required.

#

# \## Installation and Execution

#

# \### 1. Clone the repository

#

# ```powershell

# git clone https://github.com/Tamaranimi/COSC573-NaiveBayes-SpamFilter.git

# ```

#

# \### 2. Enter the project folder

#

# From the directory containing the cloned repository:

#

# ```powershell

# cd COSC573-NaiveBayes-SpamFilter

# cd SpamHam

# ```

#

# \### 3. Run the Naive Bayes classifier

#

# ```powershell

# python3 src/main.py

# ```

#

# Expected example output:

#

# ```text

# 1.0

# 3.641589521379177e-46

# ```

#

# The first value is the spam probability for the spam example; the second is the spam probability for the ham example.

#

# \### 4. Run the additional experiments

#

# ```powershell

# python3 run\_experiments.py

# ```

#

# This runs 13 experimental cases and produces results in the `experiment\_results` folder.

#

# \### 5. Run the instructor's tests

#

# ```powershell

# python3 -m testrunner

# ```

#

# Expected output:

#

# ```text

# Running local tests...

# ..

# \----------------------------------------------------------------------

# Ran 2 tests

#

# OK

# ```

#

# \*\*Windows note:\*\* If `python3` is not recognized, try `python` or `py -3`.

#

# \## Verified Results

#

# The classifier successfully identified the two labeled example messages.

#

# | Test Message | Spam Probability | Classification |

# |---|---:|---|

# | `spamesim.txt` | 1.0 (floating-point rounded) | Spam |

# | `hamesim.txt` | 3.641589521379177e-46 | Ham |

#

# The instructor's local testing framework reported:

#

# \- Tests executed: 2

# \- Tests passed: 2

# \- Test failures: 0

#

# Passing these two tests does not establish overall accuracy on a larger dataset.

#

# \## Additional Experiments

#

# Thirteen cases were executed, including the two instructor examples and eleven controlled diagnostic inputs.

#

# | Test Case | Spam Probability | Result |

# |---|---:|---|

# | `free` | 0.846196 | Spam |

# | `money` | 0.906452 | Spam |

# | `linux` | 0.406176 | Ham |

# | `listinfo` | 0.159562 | Ham |

# | `free linux` | 0.790059 | Spam |

# | `free` repeated five times | 0.999802 | Spam |

# | Empty input | 0.5 | Tie |

# | Unseen word | 0.5 | Tie |

# | `Free` | 0.5 | Tie |

# | `free!` | 0.5 | Tie |

# | Unseen word repeated 1,000 times | 0.5 | Tie |

#

# These diagnostic cases investigate model behavior. They are not an independently labeled test dataset and should not be interpreted as overall classification accuracy.

#

# \## Results Files

#

# The experiment results are recorded in:

#

# \- `SpamHam/experiment\_results/classifications.csv` â€” classification outputs and posterior probabilities.

# \- `SpamHam/experiment\_results/word\_probabilities.csv` â€” selected word-frequency likelihoods.

# \- `SpamHam/experiment\_results/RESULTS.md` â€” experimental results and interpretations.

#

# \## Challenges and Limitations

#

# \### 1. Unknown Words

#

# Words missing from the training vocabulary are assigned a fixed minimum likelihood. A word absent from both classes provides neutral evidence when the class priors are equal.

#

# \### 2. Case Sensitivity

#

# The implementation treats `free` and `Free` as different tokens.

#

# \### 3. Punctuation Sensitivity

#

# The implementation treats `free` and `free!` differently because it uses whitespace-based tokenization.

#

# \### 4. Probability Flooring

#

# The fixed lower bound is not equivalent to a fully normalized Laplace-smoothed probability distribution.

#

# \### 5. Limited Labeled Evaluation

#

# Only two labeled example messages are supplied for testing. A larger independently labeled dataset is required for reliable estimates of precision, recall, F1-score, and generalization performance.

#

# \## Potential Improvements

#

# Future extensions could include:

#

# 1\. Lowercase normalization and punctuation-aware tokenization.

# 2\. Laplace or Lidstone smoothing.

# 3\. Additional independent labeled test messages.

# 4\. Precision, recall, F1-score, and confusion matrix analysis.

# 5\. Investigation of different class priors and decision thresholds.

# 6\. Comparison with alternative text-classification methods.

#

# These are proposed improvements and are not claimed as features of the current implementation.

#

# \## References

#

# 1\. Raschka, S. \*Naive Bayes and Text Classification I â€” Introduction and Theory\*. https://arxiv.org/abs/1410.5329

# 2\. Sahami, M., Dumais, S., Heckerman, D., \& Horvitz, E. (1998). \*A Bayesian Approach to Filtering Junk E-Mail\*. AAAI Workshop on Learning for Text Categorization. https://cdn.aaai.org/Workshops/1998/WS-98-05/WS98-05-009.pdf

# 3\. Apache Software Foundation. \*Apache SpamAssassin\*. https://spamassassin.apache.org/

# 4\. Introduction to AI course materials. \*SpamHam Starter Package\*. https://materiaalit.github.io/intro-to-ai/files/tests/SpamHam.zip

#

# \## Attribution

#

# This project builds upon an educational SpamHam assignment template and its associated word-count data. The Naive Bayes evaluation method and additional diagnostic experiments were implemented as part of the COSC 573 project.

#

# The upstream educational materials and dataset retain their respective attribution and applicable licensing terms. Review those terms before further redistribution.

#

# \## Academic Context

#

# \*\*Course:\*\* COSC 573 â€” Artificial Intelligence

# \*\*Institution:\*\* Bowie State University

# \*\*Project:\*\* Implementation and Experimental Evaluation of a Naive Bayes Spam Filtering System Using Python

# \*\*Academic Term:\*\* Fall 2026

# &#x20;

