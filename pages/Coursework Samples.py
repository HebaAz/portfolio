import PIL.Image
import streamlit as st
import PIL

def formatter (list):
    for i in list:
        label = i[:6]

    return label

st.set_page_config(page_title="Education/Skills Samples", page_icon=":ribbon:", layout="centered")

st.markdown("""
<style>
.big-font {
    font-size:45px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<b><p class="big-font">My education - retained skills & coursework samples</p></b>', unsafe_allow_html=True)
st.caption('Examples of my work')

st.header("**End-to-end skills: UX design course**")
st.write("This UI/UX design course covers fundamental user experience (UX) design principles, alongside the design of an application using various skils. Application design involved...")

options = ['Phase 1: paper mockup + system analysis', 'Phase 2: user research questionnaire + analysis', 'Phase 3: High fidelity Figma prototype', 'Phase 4: walkthrough + final report']

phases = st.select_slider("Stages in the project, and samples of my work: ", options=['Phase 1', 'Phase 2', 'Phase 3', 'Phase 4'], label_visibility='visible')

if phases == 'Phase 1':
    st.write("**Phase 1: paper mockup + system analysis**")
    st.write("Creating a paper mockup/low fidelity prototype alonside a presentation of our proposal/system goals")
    
    Phase1_3230 = PIL.Image.open(f'coursework_images/3230_Phase1.png')
    st.image(Phase1_3230)

if phases == 'Phase 2':
    st.write("**Phase 2: user research questionnaire + analysis**")
    st.write("A user quiestionnaire following questionnaire best practices in order to recieve feedback on the low-fidelity design. Additionally did an analysis of the feedback, so it could be incorporated into later design")
    
    st.link_button(label= 'Try the questionnaire', url='https://docs.google.com/forms/d/e/1FAIpQLSdtMYKks7NMD52e3E75hiIyY8EYBpjRtVGLBoX6e18GLjSUzg/viewform?usp=sf_link')

    Phase2_3230 = PIL.Image.open(f'coursework_images/3230_phase2.png')
    st.image(Phase2_3230)

if phases == 'Phase 3':
    st.write("**Phase 3: High fidelity Figma prototype + video walkthrough of prototype**")
    st.write("An interactive, clean, colorful corporating user feedback from the previous questionnaire")

    st.video('https://youtu.be/7iBLZOTYzfA?si=ctbbKDuHH5pI0YqP')

    Phase31_3230 = PIL.Image.open(f'coursework_images/3230_phase3_1.png')
    st.image(Phase31_3230)
    Phase32_3230 = PIL.Image.open(f'coursework_images/3230_phase3_2.png')
    st.image(Phase32_3230)
    Phase33_3230 = PIL.Image.open(f'coursework_images/3230_phase3_3.png')
    st.image(Phase33_3230)

    st.link_button(label= 'Interact with my prototype in Figma', url='https://www.figma.com/proto/at3eU5mZQYaq2J2U2itMOo/PeacefulPoses?node-id=2-2&t=GU36jJ0K7AjV9XWz-1&scaling=scale-down&page-id=0%3A1&starting-point-node-id=2%3A2')

if phases == 'Phase 4':
    st.write("**Phase 4:** walkthrough + final report") 
    st.write("Summarizing the user experience and results of the walkthrough")
