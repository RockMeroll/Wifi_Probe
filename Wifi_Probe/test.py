import os

print("#")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQL_DIR = os.path.join(BASE_DIR, 'sql')

print(BASE_DIR)
print(os.path.join(SQL_DIR, 'wifi_probeDB.db'))