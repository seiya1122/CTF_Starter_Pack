#!/usr/bin/env python3
import sys
from pwn import *
from Crypto.Util.number import *
import requests

print("="*50)
print(f"[*] Python Version: {sys.version.split()[0]}")
print(f"[*] Pwntools Version: {pwnlib.__version__}")
print("[*] PyCryptodome: OK")
print("[*] Requests: OK")
print("="*50)
print("[+] CTF Starter Pack is ready.")
print("Good luck, have fun!")
print("="*50)