#!/usr/bin/env python3
import time
import sys

# ---------------------------------------------------
# [1] Library Check
# ---------------------------------------------------
def check_environment():
    print("[*] Checking combat capabilities...")
    try:
        # Pwntoolsのバージョン確認は pwnlib を使うのが確実です
        import pwn
        import pwnlib
        print(f"  [+] Pwntools: OK (v{pwnlib.__version__})")
        
        from Crypto.Util.number import long_to_bytes
        print("  [+] PyCryptodome: OK")
        
        import z3
        print(f"  [+] Z3 Solver: OK (v{z3.get_version_string()})")
        
        import requests
        print(f"  [+] Requests: OK (v{requests.__version__})")
        
    except ImportError as e:
        print(f"\n[!] CRITICAL ERROR: Missing library -> {e}")
        print("    Did you open this in the Docker container?")
        sys.exit(1)
    print("[*] System Green. Ready to hack.\n")
    time.sleep(1)

# ---------------------------------------------------
# [2] The Challenge (Simple Decryption)
# ---------------------------------------------------
def solve_challenge():
    print("[*] Intercepted encrypted message...")
    # Encrypted Flag (Just a simple XOR for demonstration)
    # Key: 0x55, Cipher: XORed bytes
    # Target: CTF{Welcome_to_the_Cyber_World}
    key = 0x55
    encrypted_data = [
        0x16, 0x01, 0x13, 0x2e,                                     # CTF{
        0x02, 0x30, 0x39, 0x36, 0x3a, 0x38, 0x30, 0x0a,             # Welcome_
        0x21, 0x3a, 0x0a,                                           # to_
        0x21, 0x3d, 0x30, 0x0a,                                     # the_
        0x16, 0x2c, 0x37, 0x30, 0x27, 0x0a,                         # Cyber_
        0x02, 0x3a, 0x27, 0x39, 0x31,                               # World
        0x28                                                        # }
    ]
    
    # Simulating calculation
    print("  [-] Analyzing encryption algorithm...", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(" Done.")

    print("  [-] Brute-forcing key...", end="")
    time.sleep(1)
    print(" Found! (Key: 0x55)")

    # Decryption Logic
    decrypted_chars = []
    for byte in encrypted_data:
        decrypted_chars.append(chr(byte ^ key))
    
    flag = "".join(decrypted_chars)
    
    print("\n" + "="*40)
    print(f"  FLAG ACQUIRED: {flag}")
    print("="*40)
    print("\nMission Accomplished. Your environment is All Green.")

if __name__ == "__main__":
    print("\n=== CTF Starter Pack : Welcome Protocol ===\n")
    check_environment()
    solve_challenge()