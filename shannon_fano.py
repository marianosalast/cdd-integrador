import heapq
from collections import defaultdict, Counter

def compress(text):
    freq = Counter(text)
    sorted_chars = sorted(freq.items(), key=lambda x: -x[1])

    def build_codes(char_list, code=""):
        if len(char_list) == 1:
            return [(char_list[0][0], code)]
        total = sum([freq for char, freq in char_list])
        half = 0
        split_index = 0
        for i, (char, f) in enumerate(char_list):
            half += f
            if half >= total / 2:
                split_index = i
                break
        left = char_list[:split_index + 1]
        right = char_list[split_index + 1:]
        return build_codes(left, code + "0") + build_codes(right, code + "1")
    
    codes = dict(build_codes(sorted_chars))
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
    

