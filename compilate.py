import os
import subprocess

root_dir = './src'
dist_dir = './dist'

# Asegúrate de que la carpeta de salida exista
os.makedirs(dist_dir, exist_ok=True)

def minificar_archivos(ruta):
    for archivo in os.listdir(ruta):
        archivo_ruta = os.path.join(ruta, archivo)
        
        # Si es un directorio, se llama recursivamente
        if os.path.isdir(archivo_ruta):
            minificar_archivos(archivo_ruta)
        else:
            # Si es un archivo .py, se ofusca
            if archivo.endswith('.py'):
                # Crear la ruta de salida, manteniendo la estructura del directorio
                salida_ruta = os.path.join(dist_dir, os.path.relpath(archivo_ruta, root_dir))
                salida_dir = os.path.dirname(salida_ruta) 
                os.makedirs(salida_dir, exist_ok=True)

                # Comando para ofuscar el archivo
                comando = ['/app/.venv/bin/pyarmor', 'gen', archivo_ruta, '--output', salida_dir]
                resultado = subprocess.run(comando, capture_output=True, text=True)

                # Manejo de errores
                if resultado.returncode != 0:
                    print(f"Error al procesar {archivo_ruta}: {resultado.stderr}")

minificar_archivos(root_dir)
