import PIL.Image
import streamlit as st
import PIL
import streamlit.components.v1 as components

st.set_page_config(page_title="My Hackathons Experience", layout="wide")

st.title("**Hackathons**")
st.subheader("Figma UX design, business analysis, and business presentation skills")
st.write("By participating in several hackathons in the past year, I have developed strong experience with user experience design, specifically with industry standard tools like Figma. Here's some of the work i've done:")

#Seneca
st.subheader("Seneca Smart Cities Hackathon: Technology in Mental Heath")

col1, mty1, col2 = st.columns([1.5, 0.1, 1.5])

with col1:
    Camatkar_client = PIL.Image.open(f'hackathons_images/camatkar_client1.png')
    st.image(Camatkar_client)

with col2:
    Camatkar_client2 = PIL.Image.open(f'hackathons_images/camatkar_client2.png')
    st.image(Camatkar_client2)
st.write("The client user interface: allows users to search for therapists, and journal details about their mental health (including setting goals)")

Camatkar_therapist = PIL.Image.open(f'hackathons_images/camatkar_therapist.png')
st.image(Camatkar_therapist)
st.write("The therapists view: on which the therapist can easily create/manage an account, manage their schedule, and manage/analyze client information. I designed the therapist interface with UX in mind, including data visibility for easy descision making, popular icons (ie. calendar) for speed of use and visual appeal.")

st.write("I worked in a team of 3, with a financial analyst and project manager to create a solution to be used in the mental health/therapy sector. Camatkar is a web based application with unique user experience interfaces for different target user groups")

st.write("The use of colour on both interfaces is meant to be relaxing, while still highlighting the important aspects (ie. red cancelled icons) for visibility. Some common priorities in this user experience design include learnability, ease of use, and visibility. One common platform on both interfaces is a social media aspect, which is design to be calming but facilitate engagement and social interaction")

# Embed Google Slides using an iframe
embed_url = "https://docs.google.com/presentation/d/1eAHKO7T8EwXnQ7gtUC5ckbVW1G20DTRx/edit?usp=sharing&ouid=111635917264286027934&rtpof=true&sd=true"
components.iframe(embed_url, height=600, scrolling=False)

st.divider()

#Seneca number 2
st.subheader("Seneca Affordable Housing Hackathon")

# Embed Google Slides using an iframe
embed_url="https://docs.google.com/presentation/d/1JFNADpHyP_yeM1TNMzdi0Hj8jDWej2VM/edit?usp=sharing&ouid=111635917264286027934&rtpof=true&sd=true"
components.iframe(embed_url, height=600, scrolling=True)

#Hack ITE
st.subheader("Hack ITE")

st.write("My first hackathon, a 3-day competition with the Institution of Transportation Engineers (ITE). I worked in a cross functional team of accountants, engineers, and myself; who created the prototype and business analysis. This was my first time using Figma, and I created a design incorprating important design priciples and consideration for the user experience within it. For this interface, it was important to consider the use case; a user using their device to locate a parking space while on the go. As such, I designed an easy-to-navigate, clearly visible interface. Our solution won first place in this competion, and judges cited a simple solution with a great user experience design as the reason for the award.")

ParkSmart1 = PIL.Image.open(f'hackathons_images/ITE_1.png')
st.image(ParkSmart1)

col3, col4 = st.columns([1.5, 1.5])

with col3:
    ParkSmart2 = PIL.Image.open(f'hackathons_images/ITE_2.png')
    st.image(ParkSmart2)

with col4:
    ParkSmart3 = PIL.Image.open(f'hackathons_images/ITE_3.png')
    st.image(ParkSmart3)

ParkSmart4 = PIL.Image.open(f'hackathons_images/ITE_overall.png')
st.image(ParkSmart4)

st.link_button(label= 'Try it out in Figma', url='https://www.figma.com/design/MvxZ16VElje4nDLR43XM23/Park-Smart?node-id=202%3A5106&t=tMD5OwMYjQhsEi85-1')

st.divider()