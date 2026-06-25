# Tourism Review Analysis Framework

Research code, notebooks, and paper sources for analysing sentiment-rating
incongruence in Sri Lankan tourism attraction reviews.

## Repository Layout

```text
data/
  raw/                  Source CSV files used by the notebooks
  processed/            Generated CSV outputs, ignored by Git
notebooks/
  01_dataset_preparation.ipynb
  02_model_feature_generation.ipynb
  03_analysis.ipynb
  04_model_validation.ipynb
paper/
  conference_paper_ieee.tex
  references.bib
  IEEEtran.cls
scripts/
  run_final_framework.py
  plot_incongruence_patterns.py
  plot_reviewer_expertise_patterns.py
  plot_venue_incongruence_rate.py
src/tourism_review_analysis/
  pipeline.py
```

Generated figures, processed CSVs, model outputs, LaTeX build files, and local
virtual environments are not tracked.

## Setup

Use Python 3.10, 3.11, or 3.12 for the pinned ML dependencies.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

For editable package usage:

```bash
python -m pip install -e .
```

## Notebook Workflow

Run notebooks from the repository root in this order:

1. `notebooks/01_dataset_preparation.ipynb`
2. `notebooks/02_model_feature_generation.ipynb`
3. `notebooks/03_analysis.ipynb`
4. `notebooks/04_model_validation.ipynb`

Expected paths:

- Raw input: `data/raw/Reviews.csv`
- Prepared data: `data/processed/Processed_Reviews.csv`
- Sentiment output: `data/processed/Processed_Reviews_with_Sentiment.csv`
- Generated figures: `outputs/figures/`
- Geocoding cache: `data/cache/country_resolution_cache.csv`

Keep live geocoding disabled for deterministic runs unless you intentionally
need to refresh the location cache.

## Run Final Framework

```bash
python scripts/run_final_framework.py \
  --input-csv data/processed/Processed_Reviews_with_Sentiment.csv \
  --output-csv data/processed/final_framework.csv
```

Useful flags:

```bash
python scripts/run_final_framework.py --disable-models --disable-topic
python scripts/run_final_framework.py --skip-models cardiff bertweet
```

After `python -m pip install -e .`, the console command is also available:

```bash
tourism-review-analysis \
  --input-csv data/processed/Processed_Reviews_with_Sentiment.csv \
  --output-csv data/processed/final_framework.csv
```

## Paper Figures

The paper references generated figures from `outputs/figures/`. Recreate them
with:

```bash
python scripts/plot_incongruence_patterns.py
python scripts/plot_venue_incongruence_rate.py
python scripts/plot_reviewer_expertise_patterns.py
```

Do not commit the generated PNG/PDF files.

## Paper Build

The IEEE paper source is in `paper/`. Build from inside `paper/` after
generating the required figures:

```bash
latexmk -pdf conference_paper_ieee.tex
```

Generated PDFs and auxiliary LaTeX files are ignored.
