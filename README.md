# Data Analysis Starter Kit

This repository provides quick tools for data exploration and automated machine learning using **Python 3.11**. These tools are designed to give you high-level insights with minimal coding.

## Quick Setup
## Only complete steps 1 & 2 if you want to run pycaret for ML 
1. **Create the Environment**
   Make a new directory and open it, at the command line:
```bash (command line)
   mkdir BOW && cd BOW
   git clone https://github.com
   python3.11 -m venv .venv
   ```
** Note: you can skip this if you don't plan to use pycaret for ML 
** Note: You will need to have python 3.11 installed first

2. Activate the Environment:
* **Windows**: `.\.venv\Scripts\activate`
* **macOS/Linux**: `source .venv/bin/activate`

3. Install Dependencies:[space][space]
At the command line run these two lines
```bash
   python -m pip install --upgrade pip setuptools wheel
   pip install -r requirements.txt
   ```

## Tools

### 1. Data Health Check (`profiling_snippet.py`) Example uses an sklearn dataset.
Generates an interactive HTML report of your dataset's health.
- **Run:** `profiling_snippet.py`
- **Output:** Open `data_report.html` to see missing values and correlations.

### 2. Instant Visuals (`autoviz_snippet.py`)
Automatically generates dozens of charts to find patterns.
- **Run:** `autoviz_snippet.py`
- **Output:** Interactive charts found in the `AutoViz_Plots` folder.

### 3. Automated ML (`pycaret_notebook.ipynb`)
Finds the best ML model automatically. Must be run in VS Code.
- **Action:** Click "Select Kernel" at the top right and choose `.venv` (Python 3.11).
- **Compare:** Trains ~15 models and shows a leaderboard.
- **Evaluate:** Provides an interactive dashboard for performance metrics.

---

## ⚠️ Troubleshooting (VS Code)

- **Kernel Not Found:** Run `pip install ipykernel` in your terminal and refresh the notebook.
- **Build Errors:** Ensure you are using Python 3.11 and ran the `pip upgrade` command in Step 3.
- **UI Widgets:** If `evaluate_model()` doesn't show buttons, ensure the Jupyter Extension is installed in VS Code.

