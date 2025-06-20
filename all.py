import huffman
import shannon_fano
import metrics
from datetime import datetime

def compress_all(text):
    huff_encoded, huff_codes = huffman.compress(text)
    huff_metrics = metrics.calculate_metrics(text, huff_encoded, huff_codes)
    huff_tree = huffman.build_tree_with_structure(huff_codes)

    sf_encoded, sf_codes = shannon_fano.compress(text)
    sf_metrics = metrics.calculate_metrics(text, sf_encoded, sf_codes)

    return {
        "huffman": {
            "encoded_data": huff_encoded,
            "codes": huff_codes,
            "metrics": huff_metrics,
            "tree": huff_tree
        },
        "shannon_fano": {
            "encoded_data": sf_encoded,
            "codes": sf_codes,
            "metrics": sf_metrics
        }
    }

'''
def main():
    text = "abracadabra"
    results = compress_all(text)

    print("=== Huffman ===")
    print("Comprimido:", results["huffman"]["encoded_data"])
    print("Tabla de códigos:", results["huffman"]["codes"])
    print("Métricas:", results["huffman"]["metrics"])
    print("Árbol:", results["huffman"]["tree"])

    #with open(f"compressed.huff_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}", "w") as f: f.write(results["huffman"]["encoded_data"])  # Guarda los bits como texto (para prueba)

    decoded_text = huffman.decompress(results["huffman"]["encoded_data"], results["huffman"]["codes"])
    print(f"Texto descomprimido: {decoded_text}")

    print("\n=== Shannon-Fano ===")
    print("Comprimido:", results["shannon_fano"]["encoded_data"])
    print("Tabla de códigos:", results["shannon_fano"]["codes"])
    print("Métricas:", results["shannon_fano"]["metrics"])

    decoded_text = shannon_fano.decompress(results["shannon_fano"]["encoded_data"], results["shannon_fano"]["codes"])
    print(f"Texto descomprimido: {decoded_text}")
    #with open(f"compressed.shannon_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}", "w") as f: f.write(results["shannon_fano"]["encoded_data"])  # Guarda los bits como texto (para prueba)

if __name__ == "__main__":
    main() 
'''
