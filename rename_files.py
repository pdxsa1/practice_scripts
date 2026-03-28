import os
from datetime import date

today = date.today()
files = os.listdir("../dummy_files")

for file in files:
    os.rename(f"../dummy_files/{file}", f"../dummy_files/{today}_{file}")
