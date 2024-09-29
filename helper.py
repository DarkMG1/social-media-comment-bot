def read_tokens(file_path):
    """
    Reads API tokens from a file and returns them as a dictionary.
    """
    tokens = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            key_value = line.split('=', 1)
            if len(key_value) == 2:
                key, value = key_value
                tokens[key.strip()] = value.strip()
            else:
                print(f"Warning: '{line}' is not in 'key=value' format.")
    return tokens