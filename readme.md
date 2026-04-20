# 📊 Data Analytics Practical README (Python + R)

This guide helps you quickly understand:

* How to use R and Python
* How to install libraries
* Which libraries are required
* What to replace in code during exam

---

# 🐍 Python Setup

## ✅ Install Libraries

Run in terminal:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels textblob wordcloud
```

---

# 📦 Python Libraries Used

| Purpose              | Library             |
| -------------------- | ------------------- |
| Data handling        | pandas              |
| Numerical operations | numpy               |
| Visualization        | matplotlib, seaborn |
| ML models            | scikit-learn        |
| Time series          | statsmodels         |
| Text analysis        | textblob            |
| Word cloud           | wordcloud           |

---

# 📈 Running Python Code

* Use VS Code / Jupyter Notebook
* Run using ▶️ or `python file.py`

---

# 🟦 R Setup

## ✅ Install R

Download from: [https://cran.r-project.org/](https://cran.r-project.org/)

## ✅ Install Libraries

Run in R console:

```r
install.packages("ggplot2")
install.packages("dplyr")
install.packages("wordcloud")
install.packages("e1071")
install.packages("syuzhet")
install.packages("tm")
```
---

# 📦 R Libraries Used

| Purpose           | Library   |
| ----------------- | --------- |
| Visualization     | ggplot2   |
| Data manipulation | dplyr     |
| Text mining       | tm        |
| Spam filter       | e1071     |
| Sentiment         | syuzhet   |
| Word cloud        | wordcloud |

---

# ▶️ Running R Code

## Option 1: VS Code

* Install "R" extension
* Press Ctrl + Enter

## Option 2: RStudio (Recommended)

* Open RStudio
* Run code directly

---

# 🔁 IMPORTANT: What to Replace in Codes

## 📊 Dataset Columns

| Placeholder   | Replace With                        |
| ------------- | ----------------------------------- |
| `data.csv`    | Your dataset file                   |
| `df` / `data` | Keep same                           |
| `x`           | Independent / input column          |
| `y`           | Dependent / numeric column          |
| `value`       | Main numeric column                 |
| `date`        | Date/time column                    |
| `text`        | Text column                         |
| `label`       | Output column (spam/ham, sentiment) |

---

# 🧠 How to Identify Columns

## ✔ Independent (X)

* Input features
* Example: age, salary, experience

## ✔ Dependent (y)

* Output to predict
* Example: price, result, spam/ham

---

# ⚡ Quick Tricks During Exam

## Python

```python
print(df.columns)
```

## R

```r
colnames(data)
```

---

# 📌 Topic-wise Replacement Guide

## 🔹 Regression

* X → input columns
* y → output column

## 🔹 Time Series

* date → time column
* value → numeric column

## 🔹 Text Analytics

* text → text column
* label → spam/ham or sentiment

## 🔹 Visualization

* x → category column
* y → numeric column

---

# ✅ Final Exam Strategy

1. Load dataset
2. Identify columns using `head()` or `columns`
3. Replace placeholders
4. Run code

---

# 🚀 Final Tip

👉 Always keep code simple 👉 Don’t overthink dataset 👉 Replace column names correctly 👉 Write clean output

---

You are now ready for your practical exam ✅🔥
