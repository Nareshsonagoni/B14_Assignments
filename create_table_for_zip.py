import psycopg2

try:

    conn = psycopg2.connect(host = "localhost",
                            port = "5432",
                            database="postgres",
                            user = "postgres",
                            password = "ilaiahs",
                            )

    cursor = conn.cursor()

    query = "CREATE TABLE FILE_Attr15(File_id SERIAL, filename VARCHAR(255)," \
            "filesize VARCHAR(50)," \
            "extension VARCHAR(10)," \
            "uploadedtime DATE," \
            "uploadedby VARCHAR(255)," \
            "sub_files_ext VARCHAR(255)," \
            "Files_count INTEGER)"
    cursor.execute(query)
    conn.commit()

except Exception as e:
    print("Exception occured:", e)

finally:
    print("Closing cursor and connection to postgres")
    cursor.close()
    conn.close()