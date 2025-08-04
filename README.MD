# Tweets Analyzer

A Python application that analyzes Twitter data.


## File Hierarchy

```
tweetsAnalyzer/
├── main.py                          # Entry point - initializes and runs the analysis
├── README.MD                        # This documentation file
├── controller/
│   └── manager.py                   # Main controller class that orchestrates the analysis
├── data/
│   └── tweets_dataset.csv           # Input dataset containing tweet data with columns:
│                                     # TweetID, Username, Text, CreateDate, Biased, Keyword
├── src/
│   ├── data_loader.py               # Handles CSV file loading and validation
│   └── data_analyzer.py             # Core analysis logic with statistical methods
└── results/
    └── result.json                  # Output file containing all analysis results
```

## Key Components

### Main Entry Point (`main.py`)
- Simple entry point that creates a Manager instance and runs the analysis

### Manager (`controller/manager.py`)
- Orchestrates the entire analysis process
- Coordinates between data loading and analysis
- Formats and saves results to JSON

### Data Loader (`src/data_loader.py`)
- Handles CSV file loading with error handling
- Validates file paths before processing
- Returns pandas DataFrame for analysis


