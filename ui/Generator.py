import streamlit as st
import pandas as pd

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
previous_courses = st.multiselect('What previous courses have you passed?', courses)

credits = st.slider('What are your total credit hours?', 0, 150)

min_hours, max_hours = st.select_slider(
    'What are the min/max credit hours you would like per semester?', 
    options=list(range(1, 21 + 1)),
    value=[12, 16]
)

majors = ['Computer Science', 'Mathematics', 'Biology']
current_majors = st.multiselect('What are your majors?', majors)
current_minors = st.multiselect('What are your minors?', majors)

fall2025_courses = [0, 3, 5, 6]
example_schedule_fall2025 = pd.DataFrame(
    {
        'courses': [courses[i][0] for i in fall2025_courses],
        'hours': [courses[i][1] for i in fall2025_courses],        
    }
)

st.dataframe(
    example_schedule_fall2025,
    column_config = {
        'courses': 'Courses',
        'hours': 'Credit Hours',
    },
    hide_index=True,
)