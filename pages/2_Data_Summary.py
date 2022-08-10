import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Data Summary')

# Load data
@st.cache
def load_data(path):
    pen_data = pd.read_csv(path, index_col=0)
    return pen_data

penguins = load_data('./Data/penguins.csv')
st.header('General Statistics')
penguin_species = penguins.groupby(['species', 'sex']).mean()
st.dataframe(penguin_species)
st.header('Species Breakdown')
species = penguins['species'].value_counts()
st.bar_chart(species)

st.header('Frequency Distributions')

def plot_hist(data, title):
    fig, ax = plt.subplots()
    ax.hist(data, bins='auto', stacked=True)
    ax.set_title(title)
    return st.pyplot(fig)
cols = list(penguins.columns)
cols.remove('species')
for col in cols:
    plot_hist(penguins[col], title=f'Distribution of {col}')

