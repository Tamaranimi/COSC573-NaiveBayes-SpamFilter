"""Regenerate every plot/table input from the two recorded experiment CSVs.
Run: python regenerate_assets.py   (from the paper/ directory)
No third-party dependencies. Does not retrain classifier.
"""
from pathlib import Path
import csv

HERE = Path(__file__).resolve().parent

def read(name):
    with (HERE/name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def save(name, fields, rows):
    with (HERE/name).open("w", newline="", encoding="utf-8") as f:
        out=csv.writer(f)
        out.writerow(fields)
        out.writerows(rows)

cases=read('classifications.csv')
words=read('word_probabilities.csv')
bycase={r['case']:r for r in cases}
byword={r['word']:r for r in words}

def percent(case):
    return f"{float(bycase[case]['spam_probability'])*100:.4f}"

save('labeled_results.csv',
     ['input_file','tokens','posterior','predicted_label','status'],
     [(name,bycase[key]['tokens'],bycase[key]['spam_probability'],bycase[key]['predicted_label'],'correct')
      for key,name in [('instructor_spam','spamesim.txt'),('instructor_ham','hamesim.txt')]])

displays=[
    ('spam_signal_free','free'),('spam_signal_money','money'),
    ('ham_signal_linux','linux'),('ham_signal_listinfo','listinfo'),
    ('mixed_free_linux','free linux'),('repeat_free_5','free repeated 5 times'),
    ('empty_input','empty input'),('unseen_word','completely unseen token'),
    ('capitalized_Free','Free'),('punctuated_free','free!'),
    ('unseen_repeated_1000','unseen token repeated 1000 times')]
save('diagnostic_results.csv',
     ['display_case','tokens','posterior','decision','group'],
     [(label,bycase[key]['tokens'],bycase[key]['spam_probability'],bycase[key]['predicted_label'],bycase[key]['group'])
      for key,label in displays])

save('word_ratios.csv',['token','spam_count','ham_count','q_spam','ratio'],
     [(w,byword[w]['spam_count'],byword[w]['ham_count'],
       f"{float(byword[w]['p_word_given_spam_used']):.7f}",
       f"{float(byword[w]['p_word_given_spam_used']) / float(byword[w]['p_word_given_ham_used']):.3f}")
      for w in ['free','money','linux','listinfo']])

save('figure_word_posteriors.csv',['word','spam_percent'],
     [(w,percent(key)) for w,key in [
       ('listinfo','ham_signal_listinfo'),('linux','ham_signal_linux'),
       ('free','spam_signal_free'),('money','spam_signal_money')]])
save('figure_repeat.csv',['case_label','spam_percent'],
     [(label,percent(key)) for label,key in [
       ('free','spam_signal_free'),('free+linux','mixed_free_linux'),('free x5','repeat_free_5')]])
print('Regenerated five derived CSV assets from recorded experiment results.')
