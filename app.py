
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Esto es una app")

X =np.random.normal(0,1,1000)
Y =np.random.normal(0,5,1000)
e =np.random.normal(0,1,1000)

tab1, tab2 = st.tabs(["Tab1", "Tab2"])

with tab1:
    fig, ax = plt.subplots(1, 2, sharey=True) 
    ax[0].hist(X, bins=50, alpha=0.5, color='g')
    ax[0].spines['right'].set_visible(False)
    ax[0].spines['top'].set_visible(False)    
    ax[0].axvline(X.mean(), color="g")

    ax[1].hist(Y, bins=50, alpha=0.5, color='g')
    ax[1].spines['right'].set_visible(False)
    ax[1].spines['top'].set_visible(False)    
    ax[1].axvline(Y.mean(), color="g")

    st.pyplot(fig)

with tab2:
    fig, ax = plt.subplots(1, 1) 
    ax.plot(e, color="k", alpha=0.6, ls = '--')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.axhline(e.mean(), color='k')

    st.pyplot(fig)

#import streamlit as st
import time
#import numpy as np

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)
fori in range(1, 101):
new_rows = last_rows[-1, :] + np.random.ran
status_text.text("%i%% Complete"% i)
chart.add_rows(new_rows)
progress_bar.progress(i)
last_rows = new_rows
time.sleep(0.05)
progress_bar.empty()

# Streamlit widgets automatically run the scrip
# this button is not connected to any other log
# rerun.
st.button("Re-run")    





