import streamlit as st

st.set_page_config(page_title="BIPOC Artist Hub", layout="centered")

st.header("BIPOC Artist Hub")
st.write("The BIPOC Artist Hub is an interactive exhibit with performances exploring the theme of world building and alternate worlds. Since September, students from the BIPOC Artist Hub at York University have been working towards bringing this showcase to life, this year focusing on the theme of world building and alternate worlds. With exhibits that range from visual art, board games, live performances, AI technology and more, we hope to transport you to other worlds with our personal stories, reflections and ideations.")

st.subheader("My role as a stage manager")
st.write("I spent 3 years as a stage manager with the BIPOC Artist Hub, from the beginning of it's creation, through to the first and the second showcase. Throughout my time as stage manager, I created 3 guide websites meant to be used during the walkthrough, so viewers could recieve additional information about the art they're looking at. These websites facilitated multimedia descriptions, accessibility accomodations, and several pages with unique codes.")

st.subheader("The Wix Walthrough Websites: ")
col1, col2 = st.columns([1.5, 1.5])

with col1:
    st.write("2023 Site")
    st.link_button(label="Access the site here!", url="https://hebaaz.wixsite.com/bipochubyu")
    st.image(f"HubPhotos/Site_23_s1.png")
    st.image(f"HubPhotos/Site_23_s2.png")
    st.image(f"HubPhotos/Site_23_s3.png")

with col2:
    st.write("2024 Site")
    st.link_button(label="Access the site here!", url="https://hebaaz.wixsite.com/bipochub2024/preformances")
    st.image(f"HubPhotos/Site_24_s1.png")
    st.image(f"HubPhotos/Site_24_s2.png")
    st.image(f"HubPhotos/Site_24_s3.png")

st.divider()

st.write("Additionally, I created a partially completed MERN stack website (Mongo DB, Extress, React JS, Node JS), with some HTMl and CSS components.")
st.link_button(label="Access On Github", url="https://github.com/HebaAz/BIPOCHub2024")