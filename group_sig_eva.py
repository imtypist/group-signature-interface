import json
import requests
import time

''' rpc interface
https://github.com/FISCO-BCOS/group-signature-server/blob/master/doc/rpc_interface.md
'''

def create_group(group_name, gm_pass):
    data = {
        "jsonrpc": "2.0",
        "params": {
            "group_name": group_name, 
            "gm_pass": gm_pass,
            "pbc_param": "{\"linear_type\":\"a\", \"q_bits_len\": 256, \"r_bits_len\":256}"
        },
        "id": 1,
        "method": "create_group"
    }
    r = requests.post('http://127.0.0.1:8005', data = json.dumps(data))
    res = json.loads(r.text)
    if res["result"]["ret_code"] == 0:
        print("create_group::success#" + str(res["result"]["ret_code"]))
        print("\tgpk_info:", res["result"]["result"])
    else:
        print("create_group::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])


def join_group(group_name, member_name, auth_pass = None):
    data = {
        "jsonrpc": "2.0",
        "params": {
            "group_name": group_name, 
            "member_name": member_name, 
            "pass": auth_pass
        },
        "id": 1,
        "method": "join_group"
    }
    r = requests.post('http://127.0.0.1:8005', data = json.dumps(data))
    res = json.loads(r.text)
    if res["result"]["ret_code"] == 0:
        print("join_group::success#" + str(res["result"]["ret_code"]))
        print("\tmember_sk:", res["result"]["result"])
    else:
        print("join_group::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])


def group_sig(group_name, member_name, message):
    data = {
        "id": 1,
        "jsonrpc": "2.0",
        "method": "group_sig",
        "params": {
            "group_name": group_name,
            "member_name": member_name,
            "message": message
        }
    }
    r = requests.post('http://127.0.0.1:8005', data = json.dumps(data))
    res = json.loads(r.text)
    if res["result"]["ret_code"] == 0:
        print("group_sig::success#" + str(res["result"]["ret_code"]))
        print("\tsig:", res["result"]["sig"])
        print("\tgpk:", res["result"]["gpk"])
        print("\tpbc_param:", res["result"]["pbc_param"])
        print("\tmessage:", res["result"]["message"])
    else:
        print("group_sig::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])


def group_verify(group_name, group_sig, message):
    data = {
        "id": 1,
        "jsonrpc": "2.0",
        "method": "group_verify",
        "params":{
            "group_name": group_name,
            "group_sig" : group_sig,
            "message": message
        }
    }
    r = requests.post('http://127.0.0.1:8005', data = json.dumps(data))
    res = json.loads(r.text)
    if res["result"]["ret_code"] == 0:
        print("group_verify::success#" + str(res["result"]["ret_code"]))
        print("\tresult:", res["result"]["result"])
    else:
        print("group_verify::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])


def open_cert(group_name, group_sig, message, gm_pass):
    data = {
        "id": 1,
        "jsonrpc": "2.0",
        "method":"open_cert",
        "params":{
            "group_name": group_name,
            "group_sig": group_sig,
            "message": message,
            "gm_pass": gm_pass
        }
    }
    r = requests.post('http://127.0.0.1:8005', data = json.dumps(data))
    res = json.loads(r.text)
    if res["result"]["ret_code"] == 0:
        print("open_cert::success#" + str(res["result"]["ret_code"]))
        print("\tcert_of_the_owner_of_the_signature:", res["result"]["result"])
    else:
        print("open_cert::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])


def get_public_info(group_name):
    data = {
        "id": 1,
        "jsonrpc": "2.0",
        "method": "get_public_info",
        "params": {"group_name": group_name}
    }
    r = requests.post('http://127.0.0.1:8005', data = json.dumps(data))
    res = json.loads(r.text)
    if res["result"]["ret_code"] == 0:
        print("get_public_info::success#" + str(res["result"]["ret_code"]))
        print("\tgpk:", res["result"]["result"])
    else:
        print("get_public_info::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])


if __name__ == "__main__":
    group_name = "name of group"
    gm_pass = "password of group manager"
    member_name = "v0"
    message = "m0 from v0"
    group_sig_str = "ewogICAiVDEiIDogIjEwZjkzMzUwZjdiNzNkMzg4ZDgyZGIyZWQxZDE0MGY5MTdjMDRjM2I1OTkxN2JkNGRjMjNhMDRhMDRmOTQ4MTQxMDBmYjA5NmI2ZGM2ZDc0YjJiOWYxMDVmYWFlMWE2OWYzNzcxNTE2MDg1YmQ5OGNiMDQyZTkwOGM4M2Q4NDJjZDNkZiIsCiAgICJUMiIgOiAiMWJjMjgyZDU5ZmQ4NWQxNmM5ZTk2YzA5YWI3MTM5ODQwNjUwZWQ3ZTQ4MGRiOGJmM2U2MmZjMDNjMGY4Mzc2ZTAyMTI2NDdkZjE2ZTNkMjNiNTBhOTdjYzRhODA1Y2EwNTY0OTE2NWZjZGRjN2EyODI0YTc2N2NmYTllZDdmZmFiMWRjIiwKICAgIlQzIiA6ICIwMzVmZTQ0NmE0NDgyOGEzNmQ4ZTJkMmY3NzM0YTQ4YmZlMGQzMGNlYmNhMjc2OTc1MjM0ZDIwZWM1OWI3OGY1Y2UxNmRkYWQ5MzdiZDc1ZjJjZGMzZjYxZDM1Y2M4ZDRiZTFkZWM5MThkZGE5NGFiYTY5MjI4YTNmYjdhMDFjNjIwMmEiLAogICAiYyIgOiAiMjhmYzJiODg2MTVmY2Y1Yzc3OTBjNjhlY2JkODNhMGNiMGIxZTQyMGYyMmFkNTgzOGIzYjc0ZjcyN2M2YTE4OCIsCiAgICJyYWxwaGEiIDogIjFiZGU5YzY2N2RhMDE5Y2QwMThkNjA2ODUwNzliNmM3M2YxNjcwNzVhZDc5YmM0YWExNDBjMGUzMTdhYzg3YjciLAogICAicmJldGEiIDogIjM4Y2NhYTBkNDdhYzk3ZWJlMDc5NDk5MDA3ZGY1OGVhMWUzMGI1Mjg2ZGJiNzA3NGY3ODI0MGRjNmIzZDQ3Y2YiLAogICAicmRlbHRhMSIgOiAiNTkyYmEwYzIyNzczYzM4M2EzODRlYTdlM2M4MDQ2NDMxMjZmY2M5NGIyMjk1NGYzOWQyMGFmYTBiMmU2MmU0OCIsCiAgICJyZGVsdGEyIiA6ICIzM2ZkNTBiNjE5NjA5ODkxMTkyYTJiM2YyNzBmOGY5YzczODVlZTkxZTZmNTUwZTA2NjAwYTgzMzJmOGE0ZDE5IiwKICAgInJ4IiA6ICIyMzc5NmExNDQyYjUzZjkwM2E3YTI0MzIxMjI5N2FmMjFmY2Q3ODFlNjg3NTQwMzkyNGIxMjQxMGJjMzI2YjVmIgp9Cg=="
    member_sk = "ewogICAiQSIgOiAiMTZhZTFhZmViNWU0NmJkZTkzN2RlYzk2MjFiYjAwNWYxNzQzZWI5M2EwNGZlZDZlMTJiYWY2YWJkYWU0NjEwZTlhMGVhYTA1YTBlNGNiYjNkZTQ2MDZhMzk4ODE2Y2JhM2E4NDc3MTI0ZTc1MzU3YjMxY2RmNWY0MzcwNTQ0MDk5YTI0IiwKICAgInByX0FfZzIiIDogIjA4YWRkOTQ0Zjg2NWNkMWM5NWZhNjE3Yzg3ODhhMzg4ODdmYWQwY2UwNTlmMWIyNzZhNWNkMzEzMGJhMzExYjgyNDBhMzEwNDQ0MmNiYWVkYjdmN2ZkZDkyZjliNjhiYWQwMmE5OWZjYmY1NGFlOTU4YTg5YjBlYzY4MTliMjRkOTdkYyIsCiAgICJ4IiA6ICI2NzA1YzNjMmFhMmE4ZmY3ZDdjYTExNGFhZWU4YjgzOWRjNzA0YTExM2JhOTExOGFhODA1ZmQxNTI5NmUyNGY3Igp9Cg=="

    # create_group(group_name, gm_pass)
    # join_group(group_name, member_name)
    # group_sig(group_name, member_name, message)
    # group_verify(group_name, group_sig_str, message)
    # open_cert(group_name, group_sig_str, message, gm_pass)

    get_public_info(group_name)