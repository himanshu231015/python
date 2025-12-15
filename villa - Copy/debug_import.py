import sys
import os

try:
    import villa.urls
    with open('debug_output.txt', 'w') as f:
        f.write(f"sys.path: {sys.path}\n")
        f.write(f"villa.urls file: {villa.urls.__file__}\n")
except Exception as e:
    with open('debug_output.txt', 'w') as f:
        f.write(f"Error: {e}\n")
