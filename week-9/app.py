import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from utils import getDataFrame, processTags

st.set_option('deprecation.showPyplotGlobalUse', False)

file_name = "processed-data.csv"
df = getDataFrame(file_name)

sample_df = df.sample(n=20, ignore_index=True)

st.title("Subset of the DataFrame")
st.write("This is a subset of the dataframe being loaded from BackBlaze")
st.dataframe(sample_df)

st.title("Quantitative Question")
st.write("What is the proportion of article tags does the dataset contain?")

tag_counts = {}

for row in df.iterrows():
    row_tags = processTags(row[1]["updated_tags"])

    for tag in row_tags:
        tag_counts[tag] = tag_counts.get(tag, 0) + 1
st.write(tag_counts)
data = {'Keys': list(tag_counts.keys()), 'Values': list(tag_counts.values())}
df2 = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
sns.barplot(x='Keys', y='Values', data=df2)
plt.xlabel('Tags')
plt.ylabel('Counts')
plt.xticks(rotation=45, ha='right')
st.pyplot()

st.write("GitHub Repo Link - " + "https://github.com/sashanktalakola/INFO-I501")