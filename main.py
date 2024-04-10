import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go


def main():

    st.title("TP 2: Curvas de demandas")
    col1, col2, col3 = st.columns(3)

    col1.write("Demanda 1")
    weight1 = col1.slider("Ingrese el valor de la pendiente 1:", value=1.0, min_value=0.0, max_value=10.0, step=0.1)
    bias1 = col1.slider("Ingrese el valor de la intersección 1:",value=1.0,  min_value=0.0, max_value=10.0, step=0.1)

    col2.write("Demanda 2")
    weight2 = col2.slider("Ingrese el valor de la pendiente 2:", value=1.0, min_value=0.0, max_value=10.0, step=0.1)
    bias2 = col2.slider("Ingrese el valor de la intersección 2:",value=1.0,  min_value=0.0, max_value=10.0, step=0.1)

    col3.write("Demanda 3")
    weight3 = col3.slider("Ingrese el valor de la pendiente 3:", value=1.0, min_value=0.0, max_value=10.0, step=0.1)
    bias3 = col3.slider("Ingrese el valor de la intersección 3:",value=1.0, min_value=0.0, max_value=10.0, step=0.1)

    x = np.linspace(0, 10, 20)

    fig = go.Figure()

    # Plot for pair 1
    y1 = weight1 * x + bias1
    fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='Demanda 1'))

    # Plot for pair 2
    y2 = weight2 * x + bias2
    fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='Demanda 2'))

    # Plot for pair 3
    y3 = weight3 * x + bias3
    fig.add_trace(go.Scatter(x=x, y=y3, mode='lines', name='Demanda 3'))

    st.plotly_chart(fig)

    pass


if __name__ == "__main__":
    main()