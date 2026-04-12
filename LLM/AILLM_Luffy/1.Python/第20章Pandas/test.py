import sys
print(sys.executable)
try:
    import openpyxl
    print("openpyxl version:", openpyxl.__version__)
except ImportError:
    print("openpyxl still NOT found")