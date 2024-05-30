import PIL.Image
import streamlit as st
import PIL

def formatter (list):
    for i in list:
        label = i[:6]

    return label

st.set_page_config(page_icon=":ribbon:", layout="centered")

st.markdown("""
<style>
.big-font {
    font-size:45px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<b><p class="big-font">User Experience Design</p></b>', unsafe_allow_html=True)
st.caption('Examples of my work')

st.header("**Hackathons - Figma**")
st.write("By participating in several hackathons in the past year, I have developed strong experience with user experience design, specifically with industry standard tools like Figma. Here's some of the work i've done:")

#Seneca
st.subheader("Seneca Smart Cities Hackathon: Technology in Mental Heath")

Camatkar_client = PIL.Image.open('camatkar_client1.png')
st.image(Camatkar_client)

Camatkar_client2 = PIL.Image.open('camatkar_client2.png')
st.image(Camatkar_client2)
st.write("The client user interface: allows users to search for therapists, and journal details about their mental health (including setting goals)")

Camatkar_therapist = PIL.Image.open('camatkar_therapist.png')
st.image(Camatkar_therapist)
st.write("The therapists view: on which the therapist can easily create/manage an account, manage their schedule, and manage/analyze client information. I designed the therapist interface with UX in mind, including data visibility for easy descision making, popular icons (ie. calendar) for speed of use and visual appeal.")

st.write("I worked in a team of 3, with a financial analyst and project manager to create a solution to be used in the mental health/therapy sector. Camatkar is a web based application with unique user experience interfaces for different target user groups")

st.write("The use of colour on both interfaces is meant to be relaxing, while still highlighting the important aspects (ie. red cancelled icons) for visibility. Some common priorities in this user experience design include learnability, ease of use, and visibility. One common platform on both interfaces is a social media aspect, which is design to be calming but facilitate engagement and social interaction")

st.divider()

#Hack ITE
st.subheader("Hack ITE")

st.write("My first hackathon, a 3-day competition with the Institution of Transportation Engineers (ITE). I worked in a cross functional team of accountants, engineers, and myself; who created the prototype and business analysis. This was my first time using Figma, and I created a design incorprating important design priciples and consideration for the user experience within it. For this interface, it was important to consider the use case; a user using their device to locate a parking space while on the go. As such, I designed an easy-to-navigate, clearly visible interface. Our solution won first place in this competion, and judges cited a simple solution with a great user experience design as the reason for the award.")

ParkSmart1 = PIL.Image.open('ITE_1.png')
st.image(ParkSmart1)

ParkSmart2 = PIL.Image.open('ITE_2.png')
st.image(ParkSmart2)

ParkSmart3 = PIL.Image.open('ITE_3.png')
st.image(ParkSmart3)

ParkSmart4 = PIL.Image.open('ITE_overall.png')
st.image(ParkSmart4)

st.link_button(label= 'Try it out in Figma', url='https://www.figma.com/design/MvxZ16VElje4nDLR43XM23/Park-Smart?node-id=202%3A5106&t=tMD5OwMYjQhsEi85-1')

st.divider()

st.header("**End-to-end skills: UX design course**")
st.write("This UI/UX design course covers fundamental user experience (UX) design principles, alongside the design of an application using various skils. Application design involved...")

options = ['Phase 1: paper mockup + system analysis', 'Phase 2: user research questionnaire + analysis', 'Phase 3: High fidelity Figma prototype', 'Phase 4: walkthrough + final report']

phases = st.select_slider("Stages in the project, and samples of my work: ", options=['Phase 1', 'Phase 2', 'Phase 3', 'Phase 4'], label_visibility='visible')

if phases == 'Phase 1':
    st.write("**Phase 1: paper mockup + system analysis**")
    st.write("Creating a paper mockup/low fidelity prototype alonside a presentation of our proposal/system goals")
    
    Phase1_3230 = PIL.Image.open('3230_Phase1.png')
    st.image(Phase1_3230)

if phases == 'Phase 2':
    st.write("**Phase 2: user research questionnaire + analysis**")
    st.write("A user quiestionnaire following questionnaire best practices in order to recieve feedback on the low-fidelity design. Additionally did an analysis of the feedback, so it could be incorporated into later design")
    
    st.link_button(label= 'Try the questionnaire', url='https://docs.google.com/forms/d/e/1FAIpQLSdtMYKks7NMD52e3E75hiIyY8EYBpjRtVGLBoX6e18GLjSUzg/viewform?usp=sf_link')

    Phase2_3230 = PIL.Image.open('3230_phase2.png')
    st.image(Phase2_3230)

if phases == 'Phase 3':
    st.write("**Phase 3: High fidelity Figma prototype + video walkthrough of prototype**")
    st.write("An interactive, clean, colorful corporating user feedback from the previous questionnaire")

    st.video('https://youtu.be/7iBLZOTYzfA?si=ctbbKDuHH5pI0YqP')

    Phase31_3230 = PIL.Image.open('3230_phase3_1.png')
    st.image(Phase31_3230)
    Phase32_3230 = PIL.Image.open('3230_phase3_2.png')
    st.image(Phase32_3230)
    Phase33_3230 = PIL.Image.open('3230_phase3_3.png')
    st.image(Phase33_3230)

    st.link_button(label= 'Interact with my prototype in Figma', url='https://www.figma.com/proto/at3eU5mZQYaq2J2U2itMOo/PeacefulPoses?node-id=2-2&t=GU36jJ0K7AjV9XWz-1&scaling=scale-down&page-id=0%3A1&starting-point-node-id=2%3A2')

if phases == 'Phase 4':
    st.write("**Phase 4:** walkthrough + final report") 
    st.write("Summarizing the user experience and results of the walkthrough")
