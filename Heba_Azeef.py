import streamlit as st

st.set_page_config(page_icon=":ribbon:", layout="wide")

for i in range(9):
    st.text("")

col1, col2 = st.columns([1.5, 1.5])

with col1:
    st.title("Hello, I'm Heba Azeef")
    #st.write("Information technology: Software Engineering, UX Design, Business Analysis")
    st.write("I am a developer, UX designer, and analyst with a Bachelor's degree in Information Technology, specializing in business systems analysis.")
    st.write("I have skills and experience with Python, Structured Query Language (SQL), UX Design, Prototyping (Figma), Business Analysis, Systems Analysis, UML, Business Proceess Redesign, and Web Design (HTML, JavaScript, React)")

with col2:
    st.image("meSummary.png", use_column_width=True)

for i in range(6):
    st.text("")

markdown_with_html = """
    <div style="display: flex; justify-content: center; align-items: center;">
        <img src="https://icons.veryicon.com/png/o/miscellaneous/simple-and-round-line-mark/down-arrow-56.png" width="80">
    </div>
"""
st.markdown(markdown_with_html, unsafe_allow_html=True)

st.text("")
st.text("")
st.text("")

#st.image("headshot.png")

#st.write("**A bit about me:** Some of my hobbies include acrylic painting, scrapbooking, learning new technology hands on, and participating in hackathons.")

st.write("Hello! Welcome to my portfolio website! This site was built on Python, using the Streamlit module. This website is meant to showcase myself and my work in a fun, interactive way!")
st.write("**Skills highlight:**")
skills = ["Object Oriented Programming: Python (intermediate/advanced), Java (some experience)", "Structured Query Language (SQL)", "Systems analysis and modelling with UML", "SAP ERP Systems Use and Analysis", "Business Process Modelling and Redesign", "User Experience Design on Figma", "Web Development: HTML/CSS, MERN Stack (Mongo DB, Express, React JS, Node JS) (limited)", "Statistics (Forecasting, trend analysis, estimation) and Data Visualization (Excel, Power BI)"]

col11, col12 = st.columns([1.5, 1.5])

with col11:
    for i in skills[:4]:
        st.markdown("- " + f"{i}")

with col12:
    for i in skills[4:]:
        st.markdown("- " + f"{i}")

st.divider()

#st.image('PythonHeader.png')

python_expander = st.expander("My Python Apps")

python_expander.caption("Click the image to interact with the program")

col5, col6, col7 = python_expander.columns([1.5, 1.5, 1.5])

with col5:
    #st.image('', width = 200)
    #st.page_link(page='pages\Todo List.py')

    markdown_with_html = """
    <a href="https://hebaazeefpy-8tyhtkhdfbjsvgzepnyfry.streamlit.app/Todo_List" target="_blank">
        <img src="https://cdn3d.iconscout.com/3d/premium/thumb/to-do-list-4727272-3928189.png" width="160">
    </a>
    """

    python_expander.markdown(markdown_with_html, unsafe_allow_html=True)
    python_expander.write("<b>Todo-list app</b>", unsafe_allow_html=True)

with col6:
    #st.image('camera_icon.png', width = 200)

    markdown_with_html = """
    <a href="https://hebaazeefpy-8tyhtkhdfbjsvgzepnyfry.streamlit.app/Grayscale_image_generator" target="_blank">
        <img src="https://cdn3d.iconscout.com/3d/premium/thumb/camera-4492134-3728254.png?f=webp" width="160">
    </a>
    """

    python_expander.markdown(markdown_with_html, unsafe_allow_html=True)
    python_expander.write("<b>Grayscale image generator</b>", unsafe_allow_html=True)

with col7:
    #st.image('PDF_icon.png', width = 200)
    
    markdown_with_html = """
    <a href="https://github.com/HebaAz/PDF-Converter" target="_blank">
        <img src="https://cdn3d.iconscout.com/3d/premium/thumb/pdf-file-10766769-8639812.png?f=webp" width="200">
    </a>
    """

    python_expander.markdown(markdown_with_html, unsafe_allow_html=True)
    python_expander.write("<b>PDF Generator (from CSV)</b>", unsafe_allow_html=True)

#st.image("UXHeader.png")
UX_expander = st.expander("Samples of my UI/UX design work")

col8, mty3, col9, mty4, col10 = st.columns([1.5, 0.1, 1.5, 0.1, 1.5])

with col8:
    UX_expander.write("Wireframe of parking booking app \n (Hack ITE hackathon)")
    UX_expander.image(f'hackathons_images/ITE_1.png')
    UX_expander.link_button(label='View in Figma', url='https://www.figma.com/design/MvxZ16VElje4nDLR43XM23/Park-Smart?node-id=223-5763&t=GBRS5Lt0id46EQX0-1')

with col9:
    UX_expander.write("Find therapists + social media prototype (Seneca Hackathon)")
    UX_expander.image(f'hackathons_images/Camatkar_summary.png')
    UX_expander.link_button(label='Interact in Figma', url='https://www.figma.com/proto/j7b2LBiWJaXopTuPRdKJVT/Camatk%C4%81r?node-id=1-2&t=4ZZmWqSFUF0AB6YU-1&scaling=scale-down&page-id=0%3A1&starting-point-node-id=1%3A2&show-proto-sidebar=1')

with col10:
    UX_expander.write("Video walkthrough of booking system", unsafe_allow_html=True)
    UX_expander.video('https://youtu.be/7iBLZOTYzfA?si=ctbbKDuHH5pI0YqP')
    UX_expander.link_button(label='Phases of this project', url='http://localhost:8502/Coursework_Samples#end-to-end-skills-ux-design-course')

st.divider()

BIPOC_expander = st.expander("Student leadership and management experience")

BIPOC_expander.write('The BIPOC Artist Hub is a group at York University that I had the pleasure of being a Stage Manager for throughout the past 3 years. Click the image to view my work, websites, and more in relation to the position')

markdown_with_html = """
<a href="https://hebaazeefpy-8tyhtkhdfbjsvgzepnyfry.streamlit.app/BIPOC_Artist_Hub" target="_blank">
    <img src= f"HubPhotos/HUBHeader.png">
</a>
"""
BIPOC_expander.markdown(markdown_with_html, unsafe_allow_html=True)

st.divider()

educ_expander = st.expander("Education: ")
educ_expander.write("Bachelors (Honors) majoring in Information Technology, specialized in Business Systems Analysis.")
educ_expander.write("Cumulative overall GPA of 3.3 in a 4-point scale (7.05 in a 9-point scale). Sessional GPA of 3.88 in my final year (8.08 in a 9-point scale). This is calculated using York universities GPA converter.")
educ_expander.link_button(label='Offical York University GPA conversions', url='https://secretariat.info.yorku.ca/files/Conversion-Scales-for-New-Grading-Schemes.pdf?x50430')

educ_expander.write("**Relevant courses, descriprions of skills learned from the course, and my grade**")
educ_expander.write("**Using and Designing Database Systems**: intermediate SQL skills, ERD modelling of database schemas (A)")
educ_expander.write("**Object based programming**: Algorithm development. Java topics include primitive data types, control structures, classes and arrays. The use of API&#39;s to develop applications (A).")
educ_expander.write("**Systems Analysis & Design (1 and 2)**: Design of system structure and interactions. UML diagrams in-depth, interaction design, requirements analysis, system and boundary design, object design, creation of RAD and SDD documents (A and A+)")
educ_expander.write("**Enterprise Resource Planning Systems**: Learning about cloud technology, hands-on use of SAP using market simulations & data analysis (A+)**")

st.divider()

st.subheader("Contact me")

col3, col4, mty2 = st.columns([1.5, 1.5, 2])

with col3:
    st.write(":envelope_with_arrow: heba.azeef@gmail.com")

with col4:
    st.write(":telephone_receiver: 437-350-7040")

st.divider()

st.caption("Please note that some icons are not mine, however all code, apps, and Figma designs are created by me or created by myself in collaboration with others. Icons are simply used for viusal or learning purposes.")
st.caption("Sources for icons: iconscout, veryicon, Udemy Andrew Sulce, Figma libraries")