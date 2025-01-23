import os

from streamlit.web.cli import main

from src.funcs_def import plotstream_function, FUNCTIONS


from streamlit.web import cli
from streamlit import config as _config
from streamlit.web.bootstrap import run

# _config.set_option(
#     "server.headless", True
# )  # Required to run Streamlit in a non-interactive environment


# This import path depends on your Streamlit version
def run_plotstream_app():
    # Dynamically resolve the absolute path of app.py
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of this file
    app_path = os.path.join(
        current_dir, "../app.py"
    )  # Adjust the relative path to app.py
    app_path = os.path.abspath(app_path)  # Ensure it is an absolute path

    # Run the Streamlit app
    print(f"Running Streamlit app at: {app_path}")
    run(app_path, args=[], flag_options={}, is_hello=False)
