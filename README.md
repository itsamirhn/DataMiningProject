# DataMiningProject

A data mining project that replicates the results from the paper "An Enhanced Ensemble Learning Method for Sentiment Analysis based on Q-learning" using the Yelp Reviews dataset.

## Project Presentation

- [Online Presentation (Google Slides)](https://docs.google.com/presentation/d/1LoxtbJsh631oyjNnnTFM6Bzv6sChcTwHrr-5Nxe00iA/)
- [Offline Version (presentation.pdf)](presentation.pdf)

## Overview

This project implements sentiment analysis on Yelp restaurant reviews, following the methodology described in the research paper. The analysis includes data preprocessing, exploratory data analysis, and model evaluation for sentiment classification.

## Project Structure

```
DataMiningProject/
├── 0 - download.py           # Downloads the Yelp dataset from Kaggle
├── 1 - convert.ipynb         # Converts JSON data to CSV format and creates sample
├── 2 - analysis.ipynb        # Exploratory data analysis and visualization
├── 3 - preprocess.ipynb      # Text preprocessing and cleaning
├── 4 - evaluation.ipynb      # Model evaluation and results
├── data/                     # Data directory (created after download)
│   ├── yelp_academic_dataset_review.json
│   ├── reviews.csv
│   ├── reviews_sample.csv
│   └── reviews_sample_processed.csv
├── paper.pdf                 # Reference paper
├── pyproject.toml           # Project dependencies
└── README.md                # This file
```

## Prerequisites

- Python 3.11+
- UV package manager (recommended) or pip
- Kaggle account and API key configured

## Setup

### 1. Clone and Navigate to Project

```bash
git clone https://github.com/itsamirhn/DataMiningProject.git
cd DataMiningProject
```

### 2. Install Dependencies

**Using UV:**

```bash
uv sync
```

## Usage

**⚠️ IMPORTANT: Execute in the following order:**

### Step 1: Download Dataset

```bash
python "0 - download.py"
```

This script downloads the Yelp Academic Dataset from Kaggle (~5GB) and extracts the review JSON file to the `data/` directory.

### Step 2: Convert and Sample Data

Open and run `1 - convert.ipynb` to:

- Convert the large JSON file to CSV format
- Create a 10% sample for analysis (to reduce computation time)
- Generate `reviews.csv` and `reviews_sample.csv`

### Step 3: Exploratory Data Analysis

Open and run `2 - analysis.ipynb` to:

- Analyze dataset statistics and distributions
- Visualize rating patterns and trends
- Understand data characteristics and biases

### Step 4: Text Preprocessing

Open and run `3 - preprocess.ipynb` to:

- Clean and preprocess text data
- Handle emojis, emoticons, and slang
- Remove stopwords and apply stemming/lemmatization
- Generate `reviews_sample_processed.csv`

### Step 5: Model Evaluation

Open and run `4 - evaluation.ipynb` to:

- Implement sentiment analysis models
- Evaluate performance metrics
- Compare results with the reference paper

## Dataset Information

- **Source**: Yelp Academic Dataset
- **Size**: ~5GB (original), ~45MB (sample)
- **Records**: ~8M reviews (original), ~800K reviews (sample)
- **Features**: Review text, star ratings, user/business IDs, dates, vote counts
- **Labels**: Binary sentiment classification (positive: 4-5 stars, negative: 1-3 stars)

## Key Features

### Data Processing Pipeline

1. **Raw Data Download**: Automated Kaggle dataset download
2. **Format Conversion**: JSON to CSV transformation
3. **Sampling**: 10% random sample for efficient processing
4. **Text Cleaning**: Comprehensive preprocessing pipeline
5. **Feature Engineering**: Binary sentiment labeling

### Text Preprocessing Steps

- Expressive lengthening reduction
- Emoji and emoticon conversion to text
- HTML markup removal
- Contraction expansion
- Slang dictionary mapping
- Stopword removal
- Stemming and lemmatization

## Troubleshooting

### Performance Tips

- Use the sample dataset (`reviews_sample.csv`) for faster processing
- Consider running notebooks on machines with 8GB+ RAM
- The full dataset processing may take several hours

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is for academic purposes. Please refer to the Yelp Dataset License for data usage terms.

## Citation

If you use this project in your research, please cite the original paper:

```
"An Enhanced Ensemble Learning Method for Sentiment Analysis based on Q-learning"
```

## Contact

For questions or issues, please open a GitHub issue or contact the project maintainer.
