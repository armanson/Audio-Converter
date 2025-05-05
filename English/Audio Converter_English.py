import os
import sys
import ffmpeg

def get_file_path_manual():
    path = input("Enter the full path of the audio file: ").strip('"').strip("'")
    return path

def get_file_path_drag_and_drop():
    print("\nDrag and drop the file into this terminal window and press Enter:")
    path = input().strip('"').strip("'")
    return path

def is_audio_file(path):
    return os.path.isfile(path)

def convert_audio(input_path, target_format):
    base, _ = os.path.splitext(input_path)
    output_path = f"{base}.{target_format.lower()}"

    try:
        ffmpeg.input(input_path).output(output_path).run(overwrite_output=True)
        print(f"File successfuly converted and saved as: {output_path}")
        return True
    except ffmpeg.Error as e:
        print(f"Error converting the file: {e}")
        return False

def main():
    print("=== AUDIO CONVERTER by armanson ===")
    print("Select an option to choose the audio file:")
    print("1: Enter path manually")
    print("2: Drag and drop file in this terminal")
    
    option = input("Opción (1/2): ").strip()
    if option == '1':
        path = get_file_path_manual()
    elif option == '2':
        path = get_file_path_drag_and_drop()
    else:
        print("Invalid option. Exiting.")
        sys.exit(1)

    if not is_audio_file(path):
        print(f"Error: The path '{path}' is not a valid file.")
        sys.exit(1)

    target_format = input("Enter the audio format you want to convert to.").strip().lower()
    if not target_format.isalpha():
        print("Invalid format.")
        sys.exit(1)

    success = convert_audio(path, target_format)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
