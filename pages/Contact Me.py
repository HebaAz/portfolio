import streamlit as st

# Define the HTML contact form
contact_form = """
<form id="contactForm" action="https://formsubmit.co/your@email.com" method="POST" style="display: none;">
    <input type="hidden" name="email" id="emailField">
    <input type="hidden" name="message" id="messageField">
</form>
<script>
    function submitForm() {
        document.getElementById("emailField").value = document.getElementById("streamlitEmail").value;
        document.getElementById("messageField").value = document.getElementById("streamlitMessage").value;
        document.getElementById("contactForm").submit();
    }
</script>
"""

# Render the hidden contact form HTML
st.markdown(contact_form, unsafe_allow_html=True)

# Streamlit form for user input
with st.form(key="email_form"):
    user_email = st.text_input("Your email address:", key="streamlitEmail")
    message = st.text_area("Write a message:", key="streamlitMessage")
    
    submit_button = st.form_submit_button("Submit")

    # On form submission
    if submit_button:
        st.success("Submitted!")
        # Trigger the hidden form submission using JavaScript
        st.markdown("<script>submitForm()</script>", unsafe_allow_html=True)
