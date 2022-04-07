import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import plotly.graph_objects as go 
import plotly.express as px 

dataset = pd.read_csv('projectC234_EPL.csv')

goal_column = dataset['Goals']
sorted_club_data_by_ascending_order = goal_column.groupby(dataset['Club'])
sum_of_goal_by_each_club = sorted_club_data_by_ascending_order.sum()
sorted_goal_values = sorted_club_data_by_ascending_order.sort_values(ascending=False)
print("Goal values = ", sorted_goal_values)
epl_top_goals = dataset.sort_values(by=['Goals'], asscending=False)[:10]
print("Top EPL Goal values = ", epl_top_goals)
fig = px.bar(epl_top_goals, x='Name', y='Goals', color='Goals', hover_data=['Club','Age'], text='Goals')
fig.show()