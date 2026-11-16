# COSC 573 research paper and reproducible figures

This folder holds the final eight-page, single-column LaTeX research paper and the saved numerical data used in its experimental figures and tables. The paper uses numbered equations, colored vector TikZ/PGFPlots figures, and booktabs/PGFPlotstable tables. Page numbers are shown as `1, 2, ...`.

## Files

- `COSC573_NaiveBayes_Paper.tex` — editable manuscript source; email `kenanaghan0131@students.bowiestate.edu`.
- `COSC573_NaiveBayes_Paper.pdf` — compiled eight-page paper.
- `classifications.csv`, `word_probabilities.csv` — original recorded model outputs.
- `regenerate_assets.py` — rebuilds the *five* derived CSV tables/plots below.
- `labeled_results.csv`, `diagnostic_results.csv`, `word_ratios.csv` — automatically derived table inputs.
- `figure_word_posteriors.csv`, `figure_repeat.csv` — automatically derived colored chart inputs.

## Reproduce

1. From the GitHub repository root, run `cd paper`, then `python regenerate_assets.py` (or `py -3 regenerate_assets.py` on Windows).
2. Upload the `.tex` and all seven `.csv` files together to Overleaf, with the main document set to `COSC573_NaiveBayes_Paper.tex`. Compile using **pdfLaTeX** twice.
3. The LaTeX source draws the colored plots from the CSVs with PGFPlots, formats the result tables from CSVs with PGFPlotstable, and draws the flow diagram as vector TikZ. No screenshot or external proprietary plotting program is required.
4. To rerun the underlying classifier and refresh the raw CSV results, run `python run_experiments.py` from the repository's `SpamHam/` folder, then copy `SpamHam/experiment_results/classifications.csv` and `SpamHam/experiment_results/word_probabilities.csv` into this `paper/` folder, run the regeneration script and recompile the manuscript. The supplied instructor tests can be rerun with `python -m testrunner` from `SpamHam/`.

**Interpretation:** Only two provided emails have ground-truth labels; the remaining eleven cases are diagnostics rather than an independent accuracy benchmark. Regeneration of visual assets from saved CSVs does not demonstrate independent retraining or new model validation.
