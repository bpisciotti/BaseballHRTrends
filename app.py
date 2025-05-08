import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
  df = pd.read_csv("Teams.csv", usecols = ["yearID", "HR"])
  return df

def main():
  st.title("MLB Home Run Trends (1901-2016)")

df = load_data()
hrByYear = df.groupby("yearid").sum().reset_index()

st.line_chart(
  data = hrByYear.set_index("yearID"),
  height = 400,
  width = 700,
  use_container_width = True
)

st.markdown(
  """
  **Data Source:** Baseball Databank `Teams.csv`

  *Total home runs per season from 1901 to 2016.*
  """
)

if __name__ == "__main__":
  main()
