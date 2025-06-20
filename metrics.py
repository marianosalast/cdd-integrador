import math
from collections import Counter

def calculate_metrics(original_text, compressed_bits, codes):
    # Tamaños
    original_size_bits = len(original_text) * 8
    compressed_size_bits = len(compressed_bits)

    # Frecuencias y probabilidades
    freq = Counter(original_text)
    total_chars = len(original_text)
    prob = {char: count/total_chars for char, count in freq.items()}

    # Longitud promedio de codigo
    avg_code_length = sum(len(code) * prob[char] for char, code in codes.items())

    # Entropia (limite teorico)
    entropy = -sum(p * math.log2(p) for p in prob.values())

    efficiency = entropy / avg_code_length if avg_code_length > 0 else 0

    return {
        "original_size_bits": original_size_bits,
        "compressed_size_bits": compressed_size_bits,
        "compression_ratio": compressed_size_bits / original_size_bits,
        "avg_code_length": avg_code_length,
        "entropy": entropy,
        "efficiency": efficiency,
        "symbols_table": [
            {
                "char": char,
                "frequency": freq[char],
                "code": code,
                "code_length": len(code)
            } for char, code in codes.items()   
        ]
    }
