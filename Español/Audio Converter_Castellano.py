import os
import sys
import ffmpeg

def get_file_path_manual():
    path = input("Introduce la ruta completa del archivo de audio: ").strip('"').strip("'")
    return path

def get_file_path_drag_and_drop():
    print("\nArrastra y suelta el archivo en esta ventana de terminal y presiona Enter:")
    path = input().strip('"').strip("'")
    return path

def is_audio_file(path):
    return os.path.isfile(path)

def convert_audio(input_path, target_format):
    base, _ = os.path.splitext(input_path)
    output_path = f"{base}.{target_format.lower()}"

    try:
        ffmpeg.input(input_path).output(output_path).run(overwrite_output=True)
        print(f"Archivo convertido exitosamente y guardado como: {output_path}")
        return True
    except ffmpeg.Error as e:
        print(f"Error al convertir el archivo: {e}")
        return False

def main():
    print("=== AUDIO CONVERTER by armanson ===")
    print("Seleccione opción para elegir archivo de audio:")
    print("1: Ingresar ruta manualmente")
    print("2: Arrastrar y soltar archivo en esta terminal")
    
    option = input("Opción (1/2): ").strip()
    if option == '1':
        path = get_file_path_manual()
    elif option == '2':
        path = get_file_path_drag_and_drop()
    else:
        print("Opción inválida. Salida.")
        sys.exit(1)

    if not is_audio_file(path):
        print(f"Error: La ruta '{path}' no es un archivo válido.")
        sys.exit(1)

    target_format = input("Introduce el formato de audio al que deseas convertir (por ejemplo mp3, wav, flac): ").strip().lower()
    if not target_format.isalpha():
        print("Formato inválido.")
        sys.exit(1)

    success = convert_audio(path, target_format)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
