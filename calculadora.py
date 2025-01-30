import streamlit as st

def calcular_costo(tarifa, horas_por_dia, dias_por_semana, semanas):
    costo_diario = tarifa * horas_por_dia
    costo_semanal = costo_diario * dias_por_semana
    costo_mensual = costo_semanal * semanas
    return costo_diario, costo_semanal, costo_mensual

st.title("Calculadora de Costo de Cuidado de Perros")

st.sidebar.header("Parámetros de Cálculo")

tarifa = st.sidebar.number_input("Tarifa por hora ($)", min_value=0, value=3000, step=500)
horas_por_dia = st.sidebar.number_input("Horas por día", min_value=1, max_value=24, value=8)
dias_por_semana = st.sidebar.number_input("Días por semana", min_value=1, max_value=7, value=5)
semanas = st.sidebar.number_input("Número de semanas", min_value=1, max_value=6, value=4)

if st.sidebar.button("Calcular"):
    costo_diario, costo_semanal, costo_mensual = calcular_costo(tarifa, horas_por_dia, dias_por_semana, semanas)
    
    st.subheader("Resultados")
    st.write(f"Costo diario: **${costo_diario:,.2f}**")
    st.write(f"Costo semanal: **${costo_semanal:,.2f}**")
    st.write(f"Costo mensual: **${costo_mensual:,.2f}**")

st.sidebar.info("Ajusta los valores en la barra lateral y presiona 'Calcular' para ver los costos.")
