import streamlit as st
import pandas as pd
import networkx as nx
import random
from algorithm import csc
from algorithm import credits
from algorithm import name
from algorithm import algorithm
from algorithm import algorithm_2
from algorithm import schedule
from streamlit_js_eval import streamlit_js_eval

last_column_solutions = algorithm(csc)

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
    
def generate_columns(dfs, width, indices):
    o = len(dfs)
    l = len(dfs)
    
    # just so it renders in order
    dfs.reverse()
    
    while l > 0:
        m = min(l, width)
        cols = st.columns(m)
        
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

st.title('Generator')
st.sidebar.write('Generation -- create a schedule')
st.write('Algorithmically generate your dream college schedule.')

st.divider()

st.subheader('Preferences')

previous_courses = st.multiselect('What previous courses have you passed?', list(credits.keys()))

credit_hours = st.slider('What is your current total credit hours?', 0, 150)

max_hours = st.slider(
    'What are the maximum credit hours you would like per semester?', 
    6, 18, 15
)

majors = ['Computer Science']
minors = ['None']
current_majors = st.multiselect('What is your major(s)?', majors)
current_minors = st.multiselect('What is your minor(s)?', minors)

st.divider()

st.subheader('Current schedule')

for i in range(len(schedule)):
    df = make_course_dataframe(schedule[i])
    generate_columns(
        [df],
        1,
        False,
    )

st.subheader('Build schedule')

# Dummy data

# for i in range(8):
#     scheds = []
#     for j in range(9):
#         schedule = make_course_dataframe(random.sample(range(len(credits)), random.randrange(4, 5)), str(i))
#         scheds.append(schedule)
        
#     generate_columns(
#         scheds,
#         3
#     )

# example_schedule_fall2025_1 = make_course_dataframe([0, 3, 8, 6], 'Fall 2025')
# example_schedule_fall2025_2 = make_course_dataframe([0, 3, 5, 6], 'Fall 2025')
# example_schedule_spring2026_1 = make_course_dataframe([1, 2, 4, 8], 'Spring 2026')
# example_schedule_spring2026_2 = make_course_dataframe([1, 2, 4, 5], 'Spring 2026')
# example_schedule_fall2027_1 = make_course_dataframe([7], 'Fall 2027')

# generate_columns(
#     [example_schedule_fall2025_1, example_schedule_fall2025_2, 
#      example_schedule_spring2026_1, example_schedule_spring2026_2, 
#      example_schedule_fall2027_1],
#     3
# )

# make a choice of a semester plan, press next and be prompted with more choices
# there should be a title telling you what term this is for, and you should be able to go back and make a new choice
# schedule should save as you go
2
# Keep track of semester you are at

choice = st.selectbox('Choose the schedule you want for the upcoming semester.', list(range(1, len(last_column_solutions) + 1)), 0)

if st.button('Generate next') and len(last_column_solutions) != 0:
    algorithm_2(last_column_solutions, choice - 1)
    last_column_solutions = algorithm(csc)
    streamlit_js_eval(js_expressions="parent.window.location.reload()")
    
scheds = []
for i in range(len(last_column_solutions)):
    s = make_course_dataframe(last_column_solutions[i])
    scheds.append(s)
    
generate_columns(
    scheds,
    3,
    True
)