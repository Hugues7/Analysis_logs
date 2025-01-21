# Log Analysis Pipeline

This repository provides a complete pipeline for log analysis, from data preprocessing to anomaly detection and
reporting. The pipeline is designed to handle logs with the following structure:

| Date                             | Hostname  | Process         | IdProcess | Message                                           |
|----------------------------------|-----------|-----------------|-----------|---------------------------------------------------|
| 2024-12-11T17:14:51.738480+01:00 | hilbert02 | gnome-shell     | 2026.0    | meta_window_set_stack_position_no_sync: assert... |
| 2024-12-11T17:20:14.050043+01:00 | hilbert02 | gnome-text-edit | 6677.0    | Trying to snapshot GtkGizmo 0x559f9a9e7800 wit... |

## Features

1. **Data Preprocessing**
   - Handles missing values (e.g., `NaN` in `IdProcess`).
   - Parses and normalizes timestamps.
   - Categorizes log messages into `Error`, `Warning`, or `Info`.

2. **Exploratory Data Analysis (EDA)**
   - Generates summary statistics for processes and error types.
   - Visualizes log distribution over time.
   - Identifies processes generating frequent errors.

3. **Anomaly Detection**
   - Detects anomalies based on log frequencies.
   - Implements Isolation Forest for machine learning-based anomaly detection.

4. **Reporting**
   - Outputs summary tables and visualizations.
   - Supports exporting processed logs and reports in CSV format.

---

## Setup

### Prerequisites

Ensure you have Python 3.8+ installed along with the following packages:

```bash
pip install pandas matplotlib scikit-learn
```

### Dataset

Prepare your log dataset in a CSV format with the following columns:

- `Date`: Timestamp of the log entry.
- `Hostname`: System generating the log.
- `Process`: Name of the process.
- `IdProcess`: Process ID.
- `Message`: Log description.

### Project Structure

```plaintext
log-analysis/
├── data/
│   ├── all_logs.csv              # Input log dataset
├── notebooks/
│   ├── analysis.ipynb        # Jupyter Notebook for exploration
├── scripts/
│   ├── preprocess.py         # Data preprocessing script
│   ├── anomaly_detection.py  # Anomaly detection script
├── outputs/
│   ├── processed_logs.csv    # Cleaned and categorized logs
│   ├── reports/              # Generated reports and visualizations
└── README.md                 # Project documentation
```

---

## Usage

### 1. Preprocessing

Run the preprocessing script to clean and categorize the logs.

```bash
python scripts/preprocess.py --input data/logs.csv --output outputs/processed_logs.csv
```

### 2. Exploratory Data Analysis

Use the Jupyter Notebook to perform exploratory analysis and visualize trends.

```bash
jupyter notebook notebooks/analysis.ipynb
```

### 3. Anomaly Detection

Run the anomaly detection script to identify unusual log patterns.

```bash
python scripts/anomaly_detection.py --input outputs/processed_logs.csv --output outputs/anomalies.csv
```

### 4. Reporting

View summary tables and visualizations in the `outputs/reports/` folder.


