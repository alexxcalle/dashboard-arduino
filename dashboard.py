import streamlit as st
import serial
import time

# Configura la conexión serial (ajusta el puerto COM según tu configuración)
ser = serial.Serial('COM3', 9600, timeout=1)


def leer_datos_arduino():
    ser.flush()
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        return line
    return None
#lala
def main():
    st.title("Dashboard Arduino")

    # Crea un gráfico en tiempo real
    chart = st.line_chart()

    while True:
        dato = leer_datos_arduino()
        if dato:
            try:
                valor = float(dato)
                chart.add_rows([valor])
                st.write(f"Último valor leído: {valor}")
            except ValueError:
                st.write("Dato no válido")
        
        time.sleep(0.1)

if __name__ == "__main__":
    main()