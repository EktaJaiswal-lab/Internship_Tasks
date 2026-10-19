def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    
    lines = []
    for i in range(size):
        current_chars = alpha[i:size]
        row = "-".join(current_chars[::-1] + current_chars[1:])
        lines.append(row.center(4 * size - 3, "-"))
    full_rangoli = lines[::-1] + lines[1:]
    
    # Print directly instead of returning
    print("\n".join(full_rangoli))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)