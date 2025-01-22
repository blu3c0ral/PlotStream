# PlotStream

PlotStream provides a streamlined way to create interactive dashboards for Python functions using Streamlit. It allows users to decorate their functions with a single decorator to dynamically register them and automatically launch a Streamlit application for visualization and interaction.

---

## Features

- **Seamless Integration**: Users only need to apply the `@register_function` to their functions. The rest is handled automatically.
- **Dynamic Input Generation**: Function parameters are converted into interactive widgets (e.g., sliders, text boxes) on the Streamlit app.
- **Automatic App Launch**: The Streamlit app launches automatically when the script is executed, requiring no additional user intervention.
- **Centralized Dashboard**: All decorated functions are displayed in a single dashboard, allowing users to select and execute them dynamically.