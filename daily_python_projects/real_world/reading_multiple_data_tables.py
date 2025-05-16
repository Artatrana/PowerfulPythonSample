import sys
from operator import index

s = get_secrets('retail.secrets')

db_name = 'retail_db'
conn = f"""postgresql://{s['username']}:{s[password]}@{s[host]}:{s[port]}"""

BASE_DIR = 'User/itversity/Research/Data/retail_db_json'
for table_neme in ['department','categories','products','order_items','customers']:
    try:
        df = json_to_df(BASE_DIR, table_neme)
        df.to_sql(table_neme, conn, if_exists='append', index=False)
        print(f"{table_neme} successfully populated....")
    except Exception as err:
        print(f"{table_neme} failed")
        err_type, err_obj, traceback = sys.exc_info()
        line_num = traceback.tb_lineno
        print("\npsychopg2 ERROR: ", err, "on line number", line_num )
        print("psychopg2 traceback:", traceback, "-- type:", err_type)
