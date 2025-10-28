import fitparse
import os
import sys  # <-- ¡NUEVO! Importamos la biblioteca del sistema

def analizar_sesion(filename):
    """Analiza un solo archivo .fit y muestra el resumen."""
    
    if not os.path.exists(filename):
        print(f"\n--- ❌ ERROR: No se encontró el archivo: {filename} ---")
        return

    try:
        # 1. Cargar el archivo .fit
        fitfile = fitparse.FitFile(filename)
        print(f"\n✅ === Análisis de: {filename} ===")

        # 2. Buscar los mensajes de "resumen de sesión"
        for record in fitfile.get_messages("session"):
            print("  Resumen de la Sesión:")
            
            # Convertimos los datos del registro en un diccionario fácil de usar
            data = {}
            for field in record:
                data[field.name] = field.value

            # 3. Extraer e imprimir los valores clave
            
            # Distancia (viene en metros -> la pasamos a km)
            dist_km = data.get('total_distance', 0) / 1000
            
            # Tiempo (viene en segundos -> lo pasamos a minutos)
            tiempo_min = data.get('total_timer_time', 0) / 60
            
            print(f"  📅 Fecha:            {data.get('start_time', 'N/A')}")
            print(f"  ⏱️ Tiempo Total:     {tiempo_min:.2f} minutos")
            print(f"  🏃 Distancia Total:  {dist_km:.2f} km")
            
            # Ritmo (minutos por km)
            if dist_km > 0 and tiempo_min > 0:
                ritmo_decimal = tiempo_min / dist_km
                ritmo_min = int(ritmo_decimal)
                ritmo_seg = (ritmo_decimal - ritmo_min) * 60
                print(f"  👟 Ritmo Promedio:   {ritmo_min}:{int(ritmo_seg):02d} min/km")

            # Frecuencia Cardíaca
            print(f"  ❤️ FC Promedio:     {data.get('avg_heart_rate', 'N/A')} lpm")
            print(f"  ❤️ FC Máxima:       {data.get('max_heart_rate', 'N/A')} lpm")
            
            # Cadencia (Suele venir en "rpm" (media cadencia), la duplicamos para "spm")
            avg_cad = data.get('avg_cadence', 0)
            if avg_cad > 0:
                print(f"  👣 Cadencia Prom:    {avg_cad * 2} spm") # spm = pasos por minuto

            max_cad = data.get('max_cadence', 0)
            if max_cad > 0:
                print(f"  👣 Cadencia Máx:     {max_cad * 2} spm")
                
            print(f"  🔥 Calorías:         {data.get('total_calories', 'N/A')} kcal")
            print("----------------------------------------")

    except Exception as e:
        print(f"\n--- ❌ ERROR al procesar {filename}: {e} ---")

# --- ¡NUEVO BUCLE PRINCIPAL! ---
# Esto verifica que el script se está ejecutando directamente
if __name__ == "__main__":
    
    # sys.argv es una lista. 
    # sys.argv[0] es el nombre del script ("analizar_fit.py")
    # sys.argv[1] es el primer argumento (el nombre del archivo)
    
    # Verificamos si se pasó al menos un argumento
    if len(sys.argv) < 2:
        print("--- ❌ ERROR ---")
        print("Debes especificar el nombre del archivo que quieres analizar.")
        print("\nUso: python analizar_fit.py <nombre_del_archivo.fit>")
        print("Ejemplo: python analizar_fit.py Zepp20251019062749.fit")
        sys.exit(1) # Salir del script con un código de error

    # Si todo está bien, tomamos el nombre del archivo de sys.argv[1]
    archivo_para_analizar = sys.argv[1]
    
    print(f"Iniciando análisis de {archivo_para_analizar}...")
    analizar_sesion(archivo_para_analizar)
    print("\n¡Análisis completado! 🚀")