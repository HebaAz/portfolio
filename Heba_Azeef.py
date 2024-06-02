import streamlit as st

st.set_page_config(page_icon=":ribbon:", layout="wide")

col1, mty1, col2 = st.columns([1.0, 0.1, 1.5])

with col1:
    st.image("headshot_1.png")

with col2:
    st.title("Heba Azeef")
    st.caption("Information technology: Software Engineering, UX Design, Business Analysis")

    st.write("**Professional summary:** Skilled Developer with a Bachelor's degree in Information Technology and experience in software development in Python, Java and User Interface (HTML, JavaScript, React). Experience in Business Analysis, Databases, Systems Analysis and Prototyping (Figma). I am authorized to work in the US as I am a dual US and Canadian citizen. I am currently in Canada for school, however am going to relocate based on where I work")
    st.write("**A bit about me:** Some of my hobbies include acrylic painting, scrapbooking, learning new technology hands on, and participating in hackathons.")

col3, col4, mty2 = st.columns([1.5, 1.5, 3.0])

with col3:
    st.write(":envelope_with_arrow: heba.azeef@gmail.com")

with col4:
    st.write(":telephone_receiver: 437-350-7040")

st.divider()

st.write("Hello! Welcome to my portfolio website! This site was built on Python, using the Streamlit module. This website is meant to showcase myself and my work in a fun, interactive way!")

st.divider()

st.image('PythonHeader.png')
st.caption("Click the image to interact with the program")

col5, col6, col7 = st.columns([1.5, 1.5, 1.5])

with col5:
    st.write("<b>Todo-list app</b>", unsafe_allow_html=True)
    #st.image('', width = 200)
    #st.page_link(page='pages\Todo List.py')

    markdown_with_html = """
    <a href="https://hebaazeefpy-8tyhtkhdfbjsvgzepnyfry.streamlit.app/Todo_List" target="_blank">
        <img src="https://cdn3d.iconscout.com/3d/premium/thumb/to-do-list-4727272-3928189.png" width="160">
    </a>
    """

    st.markdown(markdown_with_html, unsafe_allow_html=True)

with col6:
    st.write("<b>Grayscale image generator</b>", unsafe_allow_html=True)
    #st.image('camera_icon.png', width = 200)

    markdown_with_html = """
    <a href="http://google.com.au" target="_blank">
        <img src="https://cdn3d.iconscout.com/3d/premium/thumb/camera-4492134-3728254.png?f=webp" width="160">
    </a>
    """

    st.markdown(markdown_with_html, unsafe_allow_html=True)

with col7:
    st.write("<b>PDF Generator (from CSV files)</b>", unsafe_allow_html=True)
    #st.image('PDF_icon.png', width = 200)
    
    markdown_with_html = """
    <a href="http://google.com.au" target="_blank">
        <img src="https://cdn3d.iconscout.com/3d/premium/thumb/pdf-file-10766769-8639812.png?f=webp" width="200">
    </a>
    """

    st.markdown(markdown_with_html, unsafe_allow_html=True)

st.divider()

st.image("UXHeader.png")
st.page_link(f"pages/User Experience Design.py", label = "**Click here to see my UI/UX design work in detail**")

col8, mty3, col9, mty4, col10 = st.columns([1.5, 0.1, 1.5, 0.1, 1.5])

with col8:
    st.write("Wireframe of parking booking app \n (Hack ITE hackathon)")
    st.image('ITE_1.png')
    st.link_button(label='View in Figma', url='https://www.figma.com/design/MvxZ16VElje4nDLR43XM23/Park-Smart?node-id=223-5763&t=GBRS5Lt0id46EQX0-1')

with col9:
    st.write("Find therapists + social media prototype (Seneca Hackathon)")
    st.image('Camatkar_summary.png')
    st.link_button(label='Interact in Figma', url='https://www.figma.com/proto/j7b2LBiWJaXopTuPRdKJVT/Camatk%C4%81r?node-id=1-2&t=4ZZmWqSFUF0AB6YU-1&scaling=scale-down&page-id=0%3A1&starting-point-node-id=1%3A2&show-proto-sidebar=1')

with col10:
    st.write("Video walkthrough of booking system", unsafe_allow_html=True)
    st.video('https://youtu.be/7iBLZOTYzfA?si=ctbbKDuHH5pI0YqP')

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

st.divider()

st.caption("Please note that some icons are not mine, however all code, apps, and Figma designs are created by me or created by myself in collaboration with others. Icons are simply used for viusal or learning purposes.")
st.caption("Sources for icons: iconscout, Udemy Andrew Sulce, Figma libraries")