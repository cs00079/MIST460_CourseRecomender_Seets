import streamlit as st
from fetch_data import fetch_data

def validate_user_ui():
    if "app_user_id" not in st.session_state:
        st.session_state.app_user_id = None

    st.header("Validate User")

    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")

    if st.button("Validate User"):
        if not username.strip():
            st.error("Username is required.")
            return

        if not password.strip():
            st.error("Password is required.")
            return

        input_params = {
            "username": username.strip(),
            "password": password.strip()
        }

        df = fetch_data("validate_user/", input_params)

        if df is not None and not df.empty:
            st.success("User validated successfully!")
            output_string = (
                "App User ID: "
                + str(df["AppUserID"].values[0])
                + ", Full Name: "
                + str(df.iloc[0, 1])
            )
            st.write(output_string)
            st.session_state.app_user_id = df["AppUserID"].values[0]
        else:
            st.info("Invalid username or password.")