# Practicing basic charts

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Esto es una práctica de un gráfico")

df = pd.DataFrame(data={'Name':['Jessica','John','Alex'],
'Score 1':[77,56,87],'Score 2':[76,97,82]}
                  )
df.set_index('Name').plot(kind='bar',stacked=False,xlabel='Name',ylabel='Score')
st.pyplot(plt)

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

df = pd.DataFrame(data={'Exam':['Exam 1','Exam 2','Exam 3'],
'Dani':[77,76,87],'Daimi':[56,97,95],'Orlando':[87,82,93],'David':[97,92,93]}
                  )
fig = go.Figure(data=[
    go.Line(name='Dani', x=df['Exam'], y=df['Dani']),
    go.Line(name='Daimi', x=df['Exam'], y=df['Daimi']),
    go.Line(name='Orlando', x=df['Exam'], y=df['Orlando']),
    go.Line(name='David', x=df['Exam'], y=df['David'])    
])

fig.update_layout(
    xaxis_title='Exam',
    yaxis_title='Score',
    legend_title='Name',
)

st.plotly_chart(fig) # Plotting the final result 