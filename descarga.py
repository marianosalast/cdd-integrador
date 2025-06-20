import json
import os

def bits_to_bytes(bitstring):
    padding = (8 - len(bitstring) % 8) % 8
    bitstring += '0' * padding
    byte_data = int(bitstring, 2).to_bytes(len(bitstring) // 8, byteorder='big')
    return byte_data, padding

def guardar_como_archivo_binario(encoded_text, codes, filename_base, output_dir="compressed"):
    os.makedirs(output_dir, exist_ok=True)

    # Convertir bits a bytes
    byte_data, padding = bits_to_bytes(encoded_text)

    # Guardar archivo binario (.huff)
    filepath_bin = os.path.join(output_dir, f"{filename_base}.huff")
    with open(filepath_bin, "wb") as f:
        f.write(bytes([padding]))  # Primer byte: padding
        f.write(byte_data)

    # Guardar archivo de códigos
    filepath_json = os.path.join(output_dir, f"{filename_base}.codes.json")
    with open(filepath_json, "w") as f:
        json.dump(codes, f)

    return filepath_bin, filepath_json