https://github.com/Auditikundu/sf-connector.git

mport snowflake.connector
 
conn = snowflake.connector.connect(
    user= 'AUDITI',
    password= '12qwaszx@12QW',
    account= 'myaccount',
    database= 'SAMPLE_NEW'
    )
 
cur = conn.cursor()
try:
    cur.execute("select * from dbo.employee")
    one_row = cur.fetchone()
    print(one_row)
finally:
    cur.close()
conn.close()
 