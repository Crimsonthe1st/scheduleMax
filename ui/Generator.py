import streamlit as st

st.set_page_config(
    page_title='Generator'
)

st.title('Generator')
st.sidebar.write('Generation -- create a schedule')
st.write('Algorithmically generate your dream college schedule.')

st.divider()

st.subheader('Preferences')

classes = ['CSC 130', 'CSC 230', 'CSC 340', 'MAT 196', 'MAT 296', 'STA 290', 'CHE 351', 'CHE 352', 'BIO 330']
previous_classes = st.multiselect('What previous classes have you passed?', classes)

credits = st.slider('What are your total credit hours?', 0, 150)

min_hours, max_hours = st.select_slider(
    'What are the min/max credit hours you would like per semester?', 
    options=list(range(1, 21 + 1)),
    value=[12, 16]
)

majors = ['Computer Science', 'Mathematics', 'Biology']
current_majors = st.multiselect('What are your majors?', majors)
current_minors = st.multiselect('What are your minors?', majors)