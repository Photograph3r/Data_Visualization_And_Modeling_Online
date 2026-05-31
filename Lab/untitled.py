from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import string
import seaborn as sns
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS as sklearn_stop_words

df = pd.read_csv(r'C:\Users\spoll\Desktop\Full Sail\Data Viz\Data_Visualization_And_Modeling_Online\Lab\Starbucks_reviews.csv')
df.head()