import heapq
from collections import defaultdict, Counter

def build_tree(freq):
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)

        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return sorted(heap[0][1:], key=lambda p: (len(p[-1]), p))

def build_tree_with_structure(freq):
    heap = [[weight, [char, {}]] for char, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        node = {
            "frequency": lo[0] + hi[0],
            "left": lo[1][1] if len(lo[1][1]) > 0 else {"char": lo[1][0], "frequency": lo[0]},
            "right": hi[1][1] if len(hi[1][1]) > 0 else {"char": hi[1][0], "frequency": hi[0]}
        }
        heapq.heappush(heap, [node["frequency"], ["", node]])
    return heap[0][1][1]  # Retorna la raíz del árbol

def compress(text):
    freq = Counter(text)
    huffman_tree = build_tree(freq)
    codes = {char: code for char, code in huffman_tree}
    encoded_text = ''.join([codes[char] for char in text])
    return encoded_text, codes

def decompress(encoded_text, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    current_code = ""
    decoded_text = []
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text.append(reverse_codes[current_code])
            current_code = ""
    return ''.join(decoded_text)
