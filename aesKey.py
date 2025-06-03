import os

def generate_log_key_hex():
    key_bytes = os.urandom(16)  # 16 bytes = 32 hex characters
    return ':'.join(f"{b:02x}" for b in key_bytes)

def print_32_log_keys():
    print("Generated 32 Log Keys:\n")
    for i in range(1, 33):
        log_key = generate_log_key_hex()
        print(f"{i:02}: {log_key}")

print_32_log_keys()
