import streamlit as st

st.set_page_config(page_icon=":ribbon:", layout="wide")

col1, mty, col2 = st.columns([1.0, 0.1, 1.5])

with col1:
    st.image("headshot.png")

with col2:
    st.title("Heba Azeef")
    st.caption("Information technology: Software Engineering, UX Design, Business Analysis")

    st.write("**Professional summary:** Skilled Developer with a Bachelor's degree in Information Technology and experience in software development in Python, Java and User Interface (HTML, JavaScript, React). Experience in Business Analysis, Databases, Systems Analysis and Prototyping (Figma). I am authorized to work in the US as I am a dual US and Canadian citizen. I am currently in Canada for school, however am going to relocate based on where I work")
    st.write("**A bit about me:** Some of my hobbies include acrylic painting, scrapbooking, learning new technology hands on, and participating in hackathons.")

st.write(":envelope_with_arrow: heba.azeef@gmail.com")
st.write(":telephone_receiver: 437-350-7040")

st.divider()

st.write("Hello! Welcome to my portfolio website! This site was built on Python, using the Streamlit module. This website is meant to showcase myself and my work in a fun, interactive way!")

st.divider()

st.subheader("A bit about me: ")
st.write("")

st.divider()

st.subheader("Education: ")
st.write("Bachelors (Honors) majoring in Information Technology, specialized in Business Systems Analysis.")
st.write("Cumulative overall GPA of 3.3 in a 4-point scale (7.05 in a 9-point scale). Sessional GPA of 3.88 in my final year (8.08 in a 9-point scale). This is calculated using York universities GPA converter.")
st.link_button(label='Offical York University GPA conversions', url='https://secretariat.info.yorku.ca/files/Conversion-Scales-for-New-Grading-Schemes.pdf?x50430')

st.write("**Relevant courses, descriprions of skills learned from the course, and my grade**")
st.write("**Using and Designing Database Systems**: intermediate SQL skills, ERD modelling of database schemas (A)")
st.write("**Object based programming**: Algorithm development. Java topics include primitive data types, control structures, classes and arrays. The use of API&#39;s to develop applications (A).")
st.write("**Systems Analysis & Design (1 and 2)**: Design of system structure and interactions. UML diagrams in-depth, interaction design, requirements analysis, system and boundary design, object design, creation of RAD and SDD documents (A and A+)")
st.write("**Enterprise Resource Planning Systems**: Learning about cloud technology, hands-on use of SAP using market simulations & data analysis (A+)**")
