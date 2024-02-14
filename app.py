import streamlit as st
import pandas as pd
import datetime

from data_processing import processing_data
from visualizations import trophy_count_hbarchart, goals_count_line_plot


# setting the page title
st.set_page_config(page_title="International Football Dashboard")
# creating a large heading
st.title("International Football Dashboard")

# # adding a selectbox to the sidebar
# selected_tab = st.sidebar.radio(
#     'Choose tab:',
#     ('Tournaments Stats', 'Compare Teams')
# )

# reading the CSV files
results_df = pd.read_csv('datasets/results.csv')
shootouts_df = pd.read_csv('datasets/shootouts.csv')
goalscorers_df = pd.read_csv('datasets/goalscorers.csv')

# cleaning and preparing our data
rs = processing_data(results_df, shootouts_df)


#------------------------------------------------------------------------------------------------

# creating 2 columns for a dropdown list and a slider
row1 = st.columns(2)

# Tournament options and default selection
tournaments = ["All", "FIFA World Cup", "Copa América", "AFC Asian Cup", "African Cup of Nations", "UEFA Euro"]
selected_tournament = row1[0].selectbox("Choose Tournament", tournaments, index=1)  # Default: World Cup

# Range of years to view data from
start_year, end_year = row1[1].select_slider(
    'Select Year',
    options=range(1916, datetime.date.today().year + 1),
    value=(1916, datetime.date.today().year)
)

# cretaing tabs to view different charts
tab1, tab2 = st.tabs(["Trophies won", "Goals scored"])

# displaying trophy count chart
toggle = tab1.toggle('Trophies won as hosts')

if toggle:
    fig_trophies, fig_pie_chart = trophy_count_hbarchart(selected_tournament, rs, start_year, end_year, toggle)
    tab1.plotly_chart(fig_trophies)
    tab1.plotly_chart(fig_pie_chart)

else:
    tab1.plotly_chart(trophy_count_hbarchart(selected_tournament, rs, start_year, end_year, toggle))


# displaying goal count chart
tab2.plotly_chart(goals_count_line_plot(selected_tournament, rs, start_year, end_year))