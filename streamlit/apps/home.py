import streamlit as st
import streamlit.components.v1 as components


def app():
# bootstrap 4 collapse example
    components.html(
        """
        <div style="text-align: center;padding: 0px;">
            <h1 style="font-size:100px;color:white;justify-content: center;margin: 0px;">Welcome</h1>
            <h1 style="font-size:100px;color:white;justify-content: center;margin: 0px;">to</h1>
            <h1 style="font-size:100px;color:white;justify-content: center;margin: 0px;">Suicide prediction System</h1>
        </div>
        """,
        height=600,
    )
