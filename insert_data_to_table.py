import psycopg2
from pathlib import Path
from zipfile import ZipFile
from datetime import datetime

try:
    conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="ilaiahs",
                            host="localhost",
                            port="5432")

    cursor = conn.cursor()

    with Path('allfiles') as files:
        for file in files.iterdir():

            with ZipFile(file) as zip_files:
                files_count = len(zip_files.namelist())
                zip_files.extractall("extracted_files")

            with Path('extracted_files') as extracted:
                for inner_file in extracted.iterdir():
                    innerfile_extension = f'{inner_file.suffix}'

            date = datetime.now()
            uploadedby = 'MADHUNETTAM'

            cursor.execute(f"INSERT INTO FILE_Attr15 (filename, filesize, extension, uploadedtime, uploadedby, sub_files_ext, Files_count) "
                           f"VALUES ('{file.stem}', '{file.stat().st_size // 1024}KB', '{file.suffix}', '{date}', '{uploadedby}', '{inner_file.suffix}', '{files_count}')")
            # cursor.execute(f"INSERT INTO FILE_Attr4 (Files_count) VALUES ('{files_count}')")

    conn.commit()
    print("data inserted successfully")
except Exception as e:
    print(" Exception occured: ", e)

finally:
    print("closing everything: ")
    cursor.close()
    conn.close()