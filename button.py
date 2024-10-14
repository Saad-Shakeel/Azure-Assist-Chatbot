import streamlit as st
def Button():
    # Define CSS for the rounded icon buttons with smaller size (40x40)
    button_style = """
    <style>
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');

    .button-container {
        display: flex;
        gap: 10px;
        margin-bottom: 20px;
        margin-top: -20px;
    }

    .icon-button {
        display: inline-block;
        width: 40px;
        height: 40px;
        line-height: 40px;
        font-size: 18px; /* Smaller icon size */
        color: white; /* Icon color */
        border-radius: 50%;
        text-align: center;
        text-decoration: none;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: box-shadow 0.3s ease, transform 0.3s ease;
    }

    .icon-button:hover {
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        transform: translateY(-4px);
    }

    .linkedin-button {
        background-color: #0077B5; /* LinkedIn Blue */
    }

    .github-button {
        background-color: #333; /* GitHub Black */
    }

    .gmail-button {
        background-color: #D44638; /* Gmail Red */
    }

    .linkedin-button i,
    .github-button i,
    .gmail-button i {
        color: #ffffff; /* White icon color */
    }
    </style>
    """

    # Add the CSS to the Streamlit app
    st.markdown(button_style, unsafe_allow_html=True)

    # Create a container for the buttons
    button_container = """
    <div class="button-container">
        <a href="https://www.linkedin.com/in/saad-shakeel-12oct03" class="icon-button linkedin-button">
            <i class="fab fa-linkedin-in"></i>
        </a>
        <a href="https://github.com" class="icon-button github-button">
            <i class="fab fa-github"></i>
        </a>
        <a href="mailto:saadshakeel804@gmail.com" class="icon-button gmail-button">
            <i class="fas fa-envelope"></i>
        </a>
    </div>
    """

    # Display the button container in the Streamlit app
    st.markdown(button_container, unsafe_allow_html=True)
