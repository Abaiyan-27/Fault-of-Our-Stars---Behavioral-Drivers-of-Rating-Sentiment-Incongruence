# Tourism Review Analysis Framework

Research code and paper sources for analysing sentiment-rating incongruence in
Sri Lankan tourism attraction reviews.

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
src/tourism_review_analysis/
  pipeline.py           Reusable feature engineering and modelling pipeline
scripts/
  run_final_framework.py
```

Generated figures, processed CSVs, model outputs, and LaTeX build files are not
tracked. Recreate them from the notebooks or pipeline when needed.

## Setup

Use Python 3.10, 3.11, or 3.12 for the pinned ML dependencies.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

For editable package usage:

```bash
python -m pip install pandas numpy pycountry scikit-learn python-dotenv
```

## Run Final Framework

```bash
python scripts/run_final_framework.py \
  --input-csv data/processed/Processed_Reviews_with_Sentiment.csv \
  --output-csv data/processed/final_framework.csv
```

After `pip install -e .`, the console command is also available:

```bash
# Faster fallback (no transformer inference)
python scripts/final_tourism_analysis_framework.py --disable-models

# Skip BERTopic step
python scripts/final_tourism_analysis_framework.py --disable-topic
```

## Models Used (Final)

Sentiment ensemble:

- `cardiffnlp/twitter-roberta-base-sentiment`
- `siebert/sentiment-roberta-large-english`
- `finiteautomata/bertweet-base-sentiment-analysis`

Emotion model:

- `j-hartmann/emotion-english-distilroberta-base`

Topic modeling:

- `BERTopic`
- embedding model: `sentence-transformers/all-MiniLM-L6-v2`

Keyword extraction support:

- `KeyBERT` with `sentence-transformers/all-MiniLM-L6-v2` (supporting topic interpretation)

## Output Columns Added

The script generates the framework columns below:

- `review_count_per_location`, `review_count_per_city`
- `avg_rating_location`, `avg_rating_city`, `rating_class`
- `combined_sentiment`, `sentiment_score`, `emotion`, `sentiment_rating_gap`
- `dominant_topic`, `topic_probability`, `topic_keywords`, `review_theme`
- `province`, `district`, `tourism_region`
- `user_country`, `user_region`
- `travel_year`, `travel_month`, `travel_season`, `published_year`, `published_month`, `review_delay_days`
- `review_length`, `word_count`, `title_length`, `reviewer_experience_level`, `helpfulness_ratio`
- `has_helpful_votes`, `helpful_vote_bucket`, `review_quality_score`
- `rating_sentiment_match`, `inconsistency_flag`
- `destination_avg_rating`, `destination_review_count`, `destination_sentiment_mean`
- `length_bucket`, `avg_helpful_by_length`, `avg_rating_by_length`
- `destination_rank_by_rating`, `destination_rank_by_reviews`, `popularity_vs_quality_gap`
