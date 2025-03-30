import streamlit as st
import pandas as pd

def make_course_dataframe(indices, term):
    return pd.DataFrame(
        {
            'course': [courses[i][0] for i in indices],
            'hours': [courses[i][1] for i in indices],        
        }
    )
    
def render_course_dataframe(df, col):
    col.dataframe(
        df,
        column_config = {
            'course': 'Course',
            'hours': 'Credit Hours',
        },
        hide_index=True,
    )  
    
def generate_columns(dfs, width):
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
            
        l -= width
        

st.set_page_config(
    page_title='Generator'
)

st.title('Generator')
st.sidebar.write('Generation -- create a schedule')
st.write('Algorithmically generate your dream college schedule.')

st.divider()

st.subheader('Preferences')

# TODO: Pre-reqs
courses = [('CSC 130', 3), ('CSC 230', 3), ('CSC 340', 3), ('MAT 196', 4), ('MAT 296', 3), ('STA 290', 3), ('CHE 351', 3), ('CHE 352', 3), ('BIO 330', 3)]
previous_courses = st.multiselect('What previous courses have you passed?', [courses[i][0] for i in range(len(courses))])

credits = st.slider('What are your total credit hours?', 0, 150)

min_hours, max_hours = st.select_slider(
    'What are the minimum and maximum credit hours you would like per semester?', 
    options=list(range(1, 21 + 1)),
    value=[12, 16]
)

majors = ['Computer Science', 'Mathematics', 'Biology']
minors = majors.copy()
minors.insert(0, 'None')
current_majors = st.multiselect('What is your major(s)?', majors)
current_minors = st.multiselect('What is your minor(s)?', minors)

st.divider()

st.subheader('Build schedule')

# Dummy data
example_schedule_fall2025_1 = make_course_dataframe([0, 3, 8, 6], 'Fall 2025')
example_schedule_fall2025_2 = make_course_dataframe([0, 3, 5, 6], 'Fall 2025')
example_schedule_spring2026_1 = make_course_dataframe([1, 2, 4, 8], 'Spring 2026')
example_schedule_spring2026_2 = make_course_dataframe([1, 2, 4, 5], 'Spring 2026')
example_schedule_fall2027_1 = make_course_dataframe([7], 'Fall 2027')

generate_columns(
    [example_schedule_fall2025_1, example_schedule_fall2025_2, 
     example_schedule_spring2026_1, example_schedule_spring2026_2, 
     example_schedule_fall2027_1],
    2
)

