import streamlit as st
import plotly.graph_objects as go
import plotly.figure_factory as ff
from engine import NudgeEngine


st.set_page_config(
    page_title="Nudge Engine | Quantitative Research Tool",
    layout="wide"
)

st.markdown("""
    <style>
    [data-testid="stMetric"] {
        background-color: rgba(120, 120, 120, 0.1); 
        border: 1px solid rgba(120, 120, 120, 0.2);
        padding: 20px;
        border-radius: 12px;
    }
    [data-testid="stMetricLabel"] { color: #94a3b8 !important; font-size: 16px !important; font-weight: 600 !important; }
    </style>
    """, unsafe_allow_html=True)


st.title("Nudge Engine: Behavior Simulation")
st.caption("Herramienta de Investigación Cuantitativa de élite para simulación de Sesgos Cognitivos.")


with st.sidebar:
    st.header("Configuración")
    n_agents = st.select_slider("Muestra de Agentes", options=[1000, 5000, 10000, 20000], value=10000)
    friccion = st.slider("Fricción del Funnel", 0.1, 0.8, 0.25)
    nudge_base = st.slider("Potencia del Nudge B", 0.0, 0.5, 0.15)
    st.divider()
    st.info("Este motor simula la toma de decisiones individual basada en la Teoría de Perspectivas de Kahneman.")


@st.cache_data
def get_data(n, f, nb):
    en = NudgeEngine(n, f, nb)
    df = en.run_simulation()
    sA, sB, p_win = en.get_bayesian_analysis(df)
    return df, sA, sB, p_win

df_res, s_A, s_B, prob_win = get_data(n_agents, friccion, nudge_base)


conv_a, conv_b = df_res['convert_A'].mean(), df_res['convert_B'].mean()
uplift = (conv_b - conv_a) / conv_a if conv_a > 0 else 0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Conversión A", f"{conv_a:.2%}")
c2.metric("Conversión B", f"{conv_b:.2%}", delta=f"{uplift:+.1%}")
c3.metric("Prob. de Victoria", f"{prob_win:.2%}")
c4.metric("Muestra", f"{n_agents:,}")


tab1, tab2, tab3 = st.tabs(["Análisis Estadístico", "Diagnóstico Población", "Metodología"])

with tab1:
    st.subheader("Inferencia Bayesiana: Distribución Posterior")
    fig = ff.create_distplot([s_A, s_B], ['Variante A', 'Variante B'], show_hist=False, show_rug=False, colors=['#94a3b8', '#3b82f6'])
    fig.update_layout(xaxis_title="Tasa de Conversión", yaxis_title="Densidad", legend=dict(orientation="h", y=1.1, x=1))
    st.plotly_chart(fig, width='stretch')

with tab2:
    st.subheader("Validación de Sesgos Sintéticos")
    col_a, col_b = st.columns(2)
    with col_a:
        fig_l = go.Figure(data=[go.Histogram(x=df_res['loss_aversion'], marker_color='#3b82f6')])
        fig_l.update_layout(title="Aversión a la Pérdida (Log-Normal)")
        st.plotly_chart(fig_l, width='stretch')
    with col_b:
        fig_b = go.Figure(data=[go.Histogram(x=df_res['budget'], marker_color='#10b981')])
        fig_b.update_layout(title="Presupuesto Cognitivo (Beta)")
        st.plotly_chart(fig_b, width='stretch')

with tab3:
    st.markdown(r"""
    ### Arquitectura del Sistema
    - **Engine Layer**: Clase `NudgeEngine` encargada de la simulación estocástica y el muestreo bayesiano.
    - **UI Layer**: Interfaz reactiva construida en streamlit con visualizaciones interactivas de plotly.
    - **Ciencia de Datos**: Implementación mediante distribuciones no lineales para modelar el comportamiento humano de forma realista.
    """)

st.divider()
st.caption("Nudge Engine v2.0 | Proyecto de Quantitative Research | Karim Moya")