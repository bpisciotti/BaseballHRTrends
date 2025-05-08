# BaseballHRTrends

**Question:** How has the total number of home runs hit changed each season from 1901 through 2016?

This Streamlit app reads the `Teams.csv` dataset from the Baseball Databank and displays a line chart of total home runs per year.

---

## 📁 Project Structure

```
baseball-hr-trends/
├── app.py           # Streamlit application
└── Teams.csv        # Downloaded dataset from Baseball Databank
```

---

## ⚙️ Requirements

* Python 3.7 or higher
* pandas
* streamlit

---

## 🚀 Setup

1. **Clone or create the repository**

   ```bash
   git clone https://github.com/bpisciotti/BaseballHRTrends.git
   cd BaseballHRTrends.git
   ```

2. **Download the data**

   * Visit the [Baseball Databank on Kaggle](https://www.kaggle.com/datasets/open-source-sports/baseball-databank?select=Teams.csv)
   * Download `Teams.csv` and place it in this project folder.

3. **Install dependencies**

   ```bash
   python3 -m pip install --user pandas streamlit
   ```

> **Optional:** Use a virtual environment:
>
> ```bash
> python3 -m venv venv
> source venv/bin/activate    # macOS/Linux
> pip install pandas streamlit
> ```

---

## ▶️ Running the App Locally

From the project root, launch:

```bash
streamlit run app.py
```

A browser window should open at `http://localhost:8501` displaying the home run trends chart.

---

## 🔧 How It Works

1. **Data Loading**: `app.py` uses `pandas` to load `Teams.csv`, selecting the `yearID` and `HR` columns.
2. **Aggregation**: It groups by `yearID` and sums the `HR` values to compute total home runs per season.
3. **Visualization**: Streamlit’s `line_chart` displays the trend over time.

---

## ⚙️ Customization

* **Different Metrics**: Change the column in `usecols` (e.g. `R`, `H`, `SO`) to chart runs, hits, strikeouts, etc.
* **Date Range**: Filter `hr_by_year` in `app.py` before plotting to focus on specific eras.

---

## 🛠 Contributing

1. Fork the repo
2. Create a branch (`git checkout -b feature/my-change`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature/my-change`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. Feel free to use and modify for your own learning and exploration.

---

*Enjoy exploring the long ball trends!*
