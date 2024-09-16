import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import pandas as pd
 
conn = snowflake.connector.connect(
    user= 'AUDITI',
    password= '12qwaszx@12QW',
    account= 'vj46708.central-india.azure',
    database= 'SAMPLE_NEW',
    schema= "dbo"
    )
 
cur = conn.cursor()
# try:
#     cur.execute("select * from public.employee")
#     one_row = cur.fetchall()
#     print(one_row[0:5])
# finally:
#     cur.close()
# conn.close()
#Upload from the Exported Data File.
original = r"C:\Users\aukundu\Documents\Employee.csv"
delimiter = ","
total = pd.read_csv(original, sep = delimiter)
print(total)
table = "EMPLOYEE_DETAILS"

write_pandas(conn, total, table,auto_create_table=True)
cur.close()
conn.close()
 