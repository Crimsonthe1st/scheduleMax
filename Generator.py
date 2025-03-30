import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import pydot
from algorithm import csc
from algorithm import credits
from algorithm import name
from algorithm import algorithm
from algorithm import algorithm_2
from algorithm import schedule
from algorithm import add_subgraph_to_dot_file
from  algorithm import graph
from time import sleep

if not 'pressed' in st.session_state:
    st.session_state.pressed = False

try:
    subgraph_content
except NameError:
    subgraph_content=""
    
choice = 1    
last_column_solutions = algorithm(csc, 15)


def make_course_dataframe(names):
    return pd.DataFrame(
        {
            'course': names,
            'hours': [credits[i] for i in names],    
            'name': [name[i] for i in names]
        }
    )
    
def render_course_dataframe(df, col):
    col.dataframe(
        df,
        column_config = {
            'course': 'Course',
            'name': 'Name',
            'hours': 'Credit Hours',
        },
        hide_index=True,
    )  
    
def generate_columns(dfs, width, indices, tab):
    o = len(dfs)
    l = len(dfs)
    
    # just so it renders in order
    dfs.reverse()
    
    while l > 0:
        m = min(l, width)
        cols = tab.columns(m)
        
        for i in range(m):
            x = l - 1 - i
            render_course_dataframe(dfs[x], cols[i])
            
            s = sum(dfs[x]['hours'])
            cols[i].caption('Total hours: ' + str(s))
            
            if indices: 
                cols[i].caption('Index: ' + str(o + 1 - l))
            
            l -= 1       

st.set_page_config(
    page_title='Generator',
    layout='wide'
)

st.title('📓 Credit Cruncher')
# st.sidebar.write('Generation -- generate yourself a schedule')
st.write('Algorithmically generate your dream college schedule.')
st.divider()
st.subheader('About')
st.write('Our application uses 0/1 Knapsack to algorithmically generate schedules for students to determine optimal class schedules. Equip with our web scraper, students from colleges and universities ' +
         'have the ability to input their own courses, majors, and requirements, in order to generate schedules.')
st.divider()

st.subheader('Preferences')

st.divider()

previous_courses = st.multiselect('What previous courses have you passed?', list(credits.keys()), disabled=st.session_state.pressed)

max_hours = st.slider(
    'What are the maximum credit hours you would like per semester?', 
    6, 18, 15
)

majors = ['Computer Science']
minors = ['None']
current_majors = st.multiselect('What is your major(s)?', majors)
current_minors = st.multiselect('What is your minor(s)?', minors)

st.divider()

st.subheader('Build schedule')

st.divider()

# make a choice of a semester plan, press next and be prompted with more choices
# there should be a title telling you what term this is for, and you should be able to go back and make a new choice
# schedule should save as you go
# Keep track of semester you are at

if st.button('Begin generating semesters', disabled=st.session_state.pressed):
    last_column_solutions = algorithm(csc, max_hours)
    for x in previous_courses:
        csc.remove_node(x)
    st.session_state.pressed = True
    
if st.button('Next', disabled=not st.session_state.pressed) and len(last_column_solutions) != 0:
    algorithm_2(last_column_solutions, choice - 1)
    last_column_solutions = algorithm(csc, max_hours)

choice = st.selectbox('Choose the schedule you want for the upcoming semester.', list(range(1, len(last_column_solutions) + 1)), 0, disabled=not st.session_state.pressed)
    
with st.container(height=700):
    if st.session_state.pressed:
        scheds = []
        for i in range(len(last_column_solutions)):
            s = make_course_dataframe(last_column_solutions[i])
            scheds.append(s)
            
        generate_columns(
            scheds,
            3,
            True,
            st
        )
        
st.divider()

with st.container(height=700):
    tab1, tab2 = st.tabs(['Current schedule', 'Graduation tree'])

    for i in range(len(schedule)):
        df = make_course_dataframe(schedule[i])
        generate_columns(
            [df],
            1,
            False,
            tab1
        )

    if len(schedule)>0:
        subgraph_content = add_subgraph_to_dot_file('graph.dot',len(schedule),schedule[-1], subgraph_content)
    with open('graph.dot', 'r') as f:
        savedata=f.read() 
        tab2.graphviz_chart(savedata)
