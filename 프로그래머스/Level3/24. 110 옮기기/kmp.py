def kmp_search(text):
    pattern = "110"
    indices = []
    i, j = 0, 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            indices.append(i - j)
            j = 0

        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = 0
            else:
                i += 1
    return indices

# 사용 예시
if __name__ == "__main__":
    s = "001110"
    result = kmp_search(s)
    print("Pattern found at indices:", result)