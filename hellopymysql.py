import json
from concurrent.futures import ThreadPoolExecutor

import pymysql
import requests
from threading import Thread

connection = pymysql.connect(host="localhost",
                             user="root",
                             password="root",
                             autocommit="True",
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()
connection.select_db("ndkm")

query1 = """
            select st.stone_id,st.type, c.color_name, sad.price
            from stone_type st
            inner join s_t_c stc on stc.stone_id = st.stone_id
            inner join color c on c.c_id = stc.c_id
            inner join stone_all_details sad on stc.stone_id = sad.s_id;
        """

# connection.select_db('Joins_Database')
# query= "SELECT customers.C_id,customers.C_name,customers.address, \
#         orders.C_id,orders.Order_id,orders.Shipper_id \
#         FROM orders \m
#         CROSS JOIN customers"

cursor.execute(query1)
values = cursor.fetchall()
URL = "http://689d2358.ngrok.io/api/demo"

passed_data = []
failed_data = []

def generate_api_request(data):
    req_data ={
        "id": data["stone_id"],
        "color": data["color_name"],
        "type": data["type"],
        "price": data["price"],
        "currency_sign": "dollar",
        "currency_converter_sign": "rupee",
        "converted_currency": "INR",
        "original_currency": "USD"
    }
    return req_data

# print(values)


executor = ThreadPoolExecutor(max_workers=1)

for x in values:
    print(executor.submit(generate_api_request(x)))
    # t = Thread(target=generate_api_request,args=(x,))
    # t.start()
    print(generate_api_request(x))

    # flag = requests.post(url=URL, data=json.dumps(generate_api_request(x)))
    # #print(flag)
    # # print(flag.json())
    # # if flag.status_code == 200:
    #     passed_data.append(x)
    # else:
    #     failed_data.append(x)

#print(failed_data)

# response = requests.post(url=URL,data=json.dumps(values))
#print(response.json())

#print(cursor.fetchall())