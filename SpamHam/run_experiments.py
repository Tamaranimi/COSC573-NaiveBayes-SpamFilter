"""Reproducible additional experiments for the COSC 573 SpamHam project.
Run from the SpamHam directory: python run_experiments.py
Uses the original classifier without changing instructor files.
"""
from pathlib import Path
import csv
import math
from src.spamham import SpamHam, SMALL_NUMBER

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'experiment_results'
OUT.mkdir(exist_ok=True)
classifier = SpamHam('spamcount.txt', 'hamcount.txt')

# Controlled diagnostic inputs, NOT new independently labeled real-world emails.
CASES = [
    ('instructor_spam', 'spamesim.txt', None, 'spam', 'provided example'),
    ('instructor_ham', 'hamesim.txt', None, 'ham', 'provided example'),
    ('empty_input', None, [], None, 'edge case'),
    ('unseen_word', None, ['wordnotintrainingvocabulary123'], None, 'edge case'),
    ('spam_signal_free', None, ['free'], None, 'controlled diagnostic'),
    ('ham_signal_linux', None, ['linux'], None, 'controlled diagnostic'),
    ('spam_signal_money', None, ['money'], None, 'controlled diagnostic'),
    ('ham_signal_listinfo', None, ['listinfo'], None, 'controlled diagnostic'),
    ('mixed_free_linux', None, ['free', 'linux'], None, 'controlled diagnostic'),
    ('repeat_free_5', None, ['free'] * 5, None, 'controlled diagnostic'),
    ('capitalized_Free', None, ['Free'], None, 'tokenization diagnostic'),
    ('punctuated_free', None, ['free!'], None, 'tokenization diagnostic'),
    ('unseen_repeated_1000', None, ['wordnotintrainingvocabulary123'] * 1000, None, 'stability check'),
]

def prediction(p):
    return 'spam' if p > 0.5 else ('ham' if p < 0.5 else 'tie (0.5)')

rows = []
for ident, filename, words, expected, group in CASES:
    if filename:
        words = (ROOT / filename).read_text(encoding='utf-8').split()
    p = classifier.evaluate(words)
    rows.append({
        'case': ident, 'group': group, 'tokens': len(words),
        'spam_probability': repr(p), 'predicted_label': prediction(p),
        'expected_label_if_provided': expected or '',
        'correct_if_labeled': (str(prediction(p) == expected) if expected else '')
    })

with (OUT / 'classifications.csv').open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

total_spam = sum(classifier.spam.values())
total_ham = sum(classifier.ham.values())
word_rows=[]
for w in ['free','email','money','please','mail','list','click','content','business','information','lists','use','exmh','like','some','wrote','linux','listinfo','rpm']:
    s=classifier.spam.get(w,0); h=classifier.ham.get(w,0)
    word_rows.append({'word':w,'spam_count':s,'ham_count':h,
        'p_word_given_spam_raw':repr(s/total_spam),
        'p_word_given_ham_raw':repr(h/total_ham),
        'p_word_given_spam_used':repr(max(s/total_spam,SMALL_NUMBER)),
        'p_word_given_ham_used':repr(max(h/total_ham,SMALL_NUMBER))})
with (OUT / 'word_probabilities.csv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=word_rows[0].keys());writer.writeheader();writer.writerows(word_rows)

summary = f'''# Reproducible experiment results\n\nRun `python run_experiments.py` from the SpamHam project directory.\n\n- Spam vocabulary: {len(classifier.spam):,} words; total occurrences: {total_spam:,}.\n- Ham vocabulary: {len(classifier.ham):,} words; total occurrences: {total_ham:,}.\n- Used prior: P(spam)=P(ham)=0.5.\n- Probability floor: {SMALL_NUMBER}.\n- Decision rule: spam if P(spam | message) > 0.5; ham if lower; tie at 0.5.\n\n## Test outcomes\n\n| Case | Words | P(spam | message) | Predicted |\n|---|---:|---:|---|\n'''
for r in rows:
    summary += f"| {r['case']} | {r['tokens']} | {r['spam_probability']} | {r['predicted_label']} |\n"
summary += '''\n**Interpretation:** Only the instructor's two sample messages have provided class labels.\nThe other entries are controlled diagnostics, not a held-out test set or evidence of overall model accuracy.\nA `1.0` posterior may reflect floating-point rounding and should not be described as logical certainty.\nWord likelihood estimates in `word_probabilities.csv` include both raw frequencies and the floored likelihood actually used by the classifier.\nBecause the fixed floor is applied to every very rare/missing word, these floored likelihoods do not necessarily sum to one.\nThe original whitespace tokenization is case- and punctuation-sensitive.\n'''
(OUT / 'RESULTS.md').write_text(summary,encoding='utf-8')
print(summary)
