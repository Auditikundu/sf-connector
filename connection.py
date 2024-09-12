import snowflake.connector
 
conn = snowflake.connector.connect(
    user= 'AUDITI',
    password= '12qwaszx@12QW',
    account= 'vj46708.central-india.azure',
    database= 'SAMPLE_NEW'
    )
 
cur = conn.cursor()
try:
    cur.execute("select * from public.employee")
    one_row = cur.fetchall()
    print(one_row)
finally:
    cur.close()
conn.close()
 