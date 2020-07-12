import json
import requests
import time
import random

''' rpc interface
https://github.com/FISCO-BCOS/group-signature-server/blob/master/doc/rpc_interface.md
'''

def setup_ring(ring_name, bit_len = 2048):
    # bit_len is set to 2048 as default
    data = {
        "jsonrpc": "2.0",
        "params": {
            "ring_name": ring_name,
            "bit_len": bit_len
        },
        "id": 1,
        "method": "setup_ring"
    }
    r = requests.post('http://127.0.0.1:8005', data = json.dumps(data))
    res = json.loads(r.text)
    if res["result"]["ret_code"] == 0:
        print("setup_ring::success#" + str(res["result"]["ret_code"]))
        print("\tring_info:", res["result"]["result"])
    else:
        print("setup_ring::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])


def join_ring(ring_name):
    data = {
        "jsonrpc": "2.0",
        "params": {
            "ring_name": ring_name
        },
        "id": 1,
        "method": "join_ring"
    }
    r = requests.post('http://127.0.0.1:8005', data = json.dumps(data))
    res = json.loads(r.text)
    if res["result"]["ret_code"] == 0:
        print("join_ring::success#" + str(res["result"]["ret_code"]))
        print("\tprivate_key:", res["result"]["private_key"])
        print("\tpublic_key:", res["result"]["public_key"])
        print("\tmember_pos:", res["result"]["result"])
        return int(res["result"]["result"])
    else:
        print("join_ring::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])
        return 0


def linkable_ring_sig(ring_name, message, member_pos, ring_size):
    data = {
        "jsonrpc": "2.0",
        "params": {
            "ring_name": ring_name,
            "message": message,
            "id": member_pos,
            "ring_size": ring_size
        },
        "id": 1,
        "method": "linkable_ring_sig"
    }
    r = requests.post('http://127.0.0.1:8005', data = json.dumps(data))
    res = json.loads(r.text)
    if res["result"]["ret_code"] == 0:
        print("linkable_ring_sig::success#" + str(res["result"]["ret_code"]))
        print("\tparam_info:", res["result"]["param_info"])
        print("\tsig:", res["result"]["sig"])
        print("\tmessage:", res["result"]["message"])
    else:
        print("linkable_ring_sig::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])


def linkable_ring_verify(ring_name, message, sig):
    data = {
        "jsonrpc": "2.0",
        "params": {
            "ring_name": ring_name,
            "message": message,
            "sig": sig
        },
        "id": 1,
        "method": "linkable_ring_verify"
    }
    r = requests.post('http://127.0.0.1:8005', data = json.dumps(data))
    res = json.loads(r.text)
    if res["result"]["ret_code"] == 0:
        print("linkable_ring_verify::success#" + str(res["result"]["ret_code"]))
        print("\tis_valid:", res["result"]["result"])
    else:
        print("linkable_ring_verify::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])


def get_ring_param(ring_name):
    data = {
        "jsonrpc": "2.0",
        "params": {
            "ring_name": ring_name
        },
        "id": 1,
        "method": "get_ring_param"
    }
    r = requests.post('http://127.0.0.1:8005', data = json.dumps(data))
    res = json.loads(r.text)
    if res["result"]["ret_code"] == 0:
        print("get_ring_param::success#" + str(res["result"]["ret_code"]))
        print("\tring_info:", res["result"]["result"])
    else:
        print("get_ring_param::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])


def get_public_key(ring_name, member_pos):
    data = {
        "jsonrpc": "2.0",
        "params": {
            "ring_name": ring_name,
            "id": member_pos
        },
        "id": 1,
        "method": "get_public_key"
    }
    r = requests.post('http://127.0.0.1:8005', data = json.dumps(data))
    res = json.loads(r.text)
    if res["result"]["ret_code"] == 0:
        print("get_public_key::success#" + str(res["result"]["ret_code"]))
        print("\tpublic_key:", res["result"]["result"])
    else:
        print("get_public_key::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])


def get_private_key(ring_name, member_pos):
    data = {
        "jsonrpc": "2.0",
        "params": {
            "ring_name": ring_name,
            "id": member_pos
        },
        "id": 1,
        "method": "get_private_key"
    }
    r = requests.post('http://127.0.0.1:8005', data = json.dumps(data))
    res = json.loads(r.text)
    if res["result"]["ret_code"] == 0:
        print("get_private_key::success#" + str(res["result"]["ret_code"]))
        print("\tprivate_key:", res["result"]["result"])
    else:
        print("get_private_key::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])


'''interface function test'''
# if __name__ == "__main__":
#     ring_name = "name of ring"
#     message = "m0"
#     ring_size = None
#     ring_info = "ewogICAiZyIgOiAiMy4iLAogICAicCIgOiAiMTY2Nzk0MDMzNjMxMDQxNTU2ODY2NjEzNjAzMDIyNDE3Nzc4MzIxNzU3Njc3NzA1MzMxMzM5NDA1MDc0MDk1MTQxODM5Njk3MDE2NzAyMjQ5MjYzNTQ0MzY2MTM5NzI5NzkwODc3MTU3MTM1MTMzMDQxMzM0MTg5NDM3MDkwNzQzMTM0NTM4NjgwNzk4ODMxNDc3MTc1OTYyNjk2NTY2MDQzODEwNzI5NjQ5NjA3NTI2MDIxMjczODUxMzUzOTkxNjc5MTYyNzQ0NjQzMjY5NzIxNDM2ODY5MDA1ODEyODM2NzM5NjE1NTI4NjgyMjkyNzI1MTIxMzAzNTE0NTMyMDc5NzkwMjAyMDk0MjM4MzMwNjMyMjI0MzI0MjA1NjI4MjQ1NzAxNTQyMjY3NzYwNTMxNzk1NDMwODM2MjM0MDg5NjUxMTk0MTgxMjE4ODc2MTYwNTc5OTY4OTQ1NjI4MDIxNzg1MjgwMDYxMzkwMzk0MDI5MjU4NDcwMTMxNjEwMjczNTMxMzk5MzI4NjczNzA4MTY4ODg4OTQ3MDY3NzI1MTYwOTM5NDM0NzAxOTUyMjc5ODAwMzY0MDk0OTkzMDc5ODkxNTY4NzI5Mjc4NDU4MDY0NDYyNTUwMzMzOTk1NzU3NjM2ODc0MjAzMTc0NTM5Mjc4MzA5MDczMTY1Nzg1OTE3NDMzOTUxMDI4NzA5NjU0OTI3MTEwNTA3NjY3ODgzNDEzNDE0NjI3MDI1NDM2OTcxMDkyODkyMjAwMjk3ODEzNzkxNTE1NDgzNTYwNDY0OTYwODg4ODkyMjMwMzU5NzY2NjQ0NTkuIiwKICAgInEiIDogIjgzMzk3MDE2ODE1NTIwNzc4NDMzMzA2ODAxNTExMjA4ODg5MTYwODc4ODM4ODUyNjY1NjY5NzAyNTM3MDQ3NTcwOTE5ODQ4NTA4MzUxMTI0NjMxNzcyMTgzMDY5ODY0ODk1NDM4NTc4NTY3NTY2NTIwNjY3MDk0NzE4NTQ1MzcxNTY3MjY5MzQwMzk5NDE1NzM4NTg3OTgxMzQ4MjgzMDIxOTA1MzY0ODI0ODAzNzYzMDEwNjM2OTI1Njc2OTk1ODM5NTgxMzcyMzIxNjM0ODYwNzE4NDM0NTAyOTA2NDE4MzY5ODA3NzY0MzQxMTQ2MzYyNTYwNjUxNzU3MjY2MDM5ODk1MTAxMDQ3MTE5MTY1MzE2MTEyMTYyMTAyODE0MTIyODUwNzcxMTMzODgwMjY1ODk3NzE1NDE4MTE3MDQ0ODI1NTk3MDkwNjA5NDM4MDgwMjg5OTg0NDcyODE0MDEwODkyNjQwMDMwNjk1MTk3MDE0NjI5MjM1MDY1ODA1MTM2NzY1Njk5NjY0MzM2ODU0MDg0NDQ0NDczNTMzODYyNTgwNDY5NzE3MzUwOTc2MTM5OTAwMTgyMDQ3NDk2NTM5OTQ1Nzg0MzY0NjM5MjI5MDMyMjMxMjc1MTY2OTk3ODc4ODE4NDM3MTAxNTg3MjY5NjM5MTU0NTM2NTgyODkyOTU4NzE2OTc1NTE0MzU0ODI3NDYzNTU1MjUzODMzOTQxNzA2NzA3MzEzNTEyNzE4NDg1NTQ2NDQ2MTAwMTQ4OTA2ODk1NzU3NzQxNzgwMjMyNDgwNDQ0NDQ2MTE1MTc5ODgzMzIyMjkuIgp9Cg=="
#     private_key = "ewogICAicG9zIiA6ICIwIiwKICAgInBya194IiA6ICI4MjQ2Nzc2Njc3MDIxMzc2MTYwMzYxMjA3NzAyMzQ3NDYyNzYwMzM5OTY2NTk1NjkyNDE4OTI1ODU3MDQyMDkyMjc4MTQ2MDgyOTM5MTc1NDU3MDQyODUyNTU0NzA5MzU0OTM1MTc2NTQyNDc3NDAyNjk0MDkxOTczNjg1MDI2NTgzOTUwMjQ3NjY4NzE4Mjg3NjQzNDg0OTk4NTM0MzEwODMzODQ5MTc3MDEzMjU5MjYxMjc3NDEwODYyMjUzOTA0ODk2OTY5NTY0OTkwNTI5OTU0NDA3MDg4NzIzNDIxNTc0NDI0NTY2ODQzNzQ4MzAwNDM5OTQ5MDI3NTYzNzUxNTUwNTMzNDgyNzQ1MzA2Mzg1MjE2NjE1MzI1MjU0MTY2MjE1OTkxOTk0ODMxMzM0MzE1MTg3ODY5MjM3MzQ3OTM1MjY2ODk0OTUwMzM4MjQ0NDQ2MDk0NzYzMjI5MjA0NzEwNDE0MTgyODcxMzcyNDkwNTQwOTc5NDQ0NzcxOTk2MzEwMjMyNzkxMzUzOTQxODkyMTA3ODE1MDQ2NzY4Nzc5ODM4Mjg3NTA4NTg1Mjg0ODI1NjA1Nzc3Njk1MjMyNTQ1MTEyODgwMTE0NTI1ODUwOTY2Njk1MjkwNzM1NzQwNjA2ODY1MjM1NzIwOTEyMjIxMzY4MDYxNDMxMzM2NDI4MjE1NjYwNDI5MTU4MjM3MDQ0NTcxMjg4NTExMDYxMzQwNDczMDIwMzUxOTcyODA5NjAwNTkzOTk1MjY1NzIyOTU4NjYxNDY4MDYwNjI3OTgzMjY0OTYzNzAxNTU3MjcyOTA4MjkxLiIKfQo="
#     public_key = "MTM0MjgwMDUzMDYwNzYyNDY5MDQ3NDUzMzg1NzQ4NTM0OTI3ODk0MjUyMjQ2NDM0NjQ0MzQ2ODQ5NjExMzg5MjAzMTM1NjUxNTQ5NDk2NjUyMDU5NjA1ODA2NTE3ODQ0NDkxNjMxNjc2MTgzMzA3MzM0NTgxNjA1MTk3ODQxMjg3MjcwNjY3NTY0OTM4Mjk5MjQ0MTU4ODIxMTI1MjgxMTU1MDU3NjA0MjQ2OTk1MTY3OTQyODUzNDM0OTk2NjQ0NzYzODcyMDc0MzI3ODEwMDUwODI3ODI5OTM5MDgzNDQyOTQwMzAwNDQwMjE0MzUxMTA3NjExMjYwNTcxMDgyNDgwNzExNDQ4MTU1MjczNjQ5MjAxNDQ5NDU2MTc1MzY0NDg0Mjg1NDkzNTA4NzMyMTczOTE1MTYxNzU1MDM2MDc0MDEzMTM3OTc1Njg5NDc5NDU0NTczNjI0NDM5MDE2ODg5NzYwMDM0NjE2ODg4MzA4NDU2NDYxNDk2OTMxMTYyNTEyMDc3OTY5NzkzNDc0NzIzNDk4OTU1Nzk5OTQ4MTc1OTgzNjU1ODMxODcyMTI0NDQ5NzY1NTg2MDg5ODU2NzE2NTMxOTY0OTE5NzgxNzY0ODk5MjE4OTYxMDAxMTUxNDQ1Mzg3ODUwNzc5MzIyODUwNjQ4MTkxNjUxMTE2NTQ5Nzg5MDg1OTcwNjM4Mjc5MDYyMDc5ODU5MzEyNDcwNDc4NTUzNDc3NTM4NDU1MzQzOTExNTExODU0OTMwNjc2Mjc0NjQ0MDE1OTk5MzkwMTE1MjU3MzI3MzU5MzUxMTI2NDQ0ODAyMzgu"
#     sig = "ewogICAiQyIgOiAiMTA2NjQwNjExMDQ0NTg4ODgzOTY0ODM0Mzc1NjkwMDUyMzYxMTIwMDIzNjQzOTUyNzE3MDk4MTQ3ODE3MjY1MjIyNzA2MTM0MzA1OTIwLiIsCiAgICJZIiA6ICIxNTc3MTA2ODA0NTQ2Nzk0NzY2NTU4MzAzNjc4ODE4NjI2OTAzNjU3MjEzNzQxMjIzOTc5NjE0Nzc1MjMzNzA4MTMwOTM3MjMyNjY3OTUwMTg2OTgzNzE1Mjg0NTE3MjMyMTcwNzgzOTIyNDgxOTI2MjgwOTg3MzUwOTA2MzU2MTAxODMyNzU4NDYyODMzMjkxNjcyMjYwOTcyNzk3NDg3MDY1Mjk1MTY5OTQxODcyMjU5NjEzMTA5ODM1NTg0Nzg5NTk0NzI4Njc2Nzc5MTI4ODM4ODM5NzM0NDkyOTA2NDMwODQ0MzU5NTA4MzQ1MTI0NDg0NTIyMDg3NTcyMzY5MzM0NDYxNzc3MjEyOTUyNzYzODg3NTY0MDQ4NTg4NTkwMDI3NzYyODY0Njk0NDA1MDgxOTIzNzk0MzI4ODI0OTY1NTMxMTMxODI1NDQ0MzQ2NDQ1MjcxNzU5MzM4NjQ1NDE5ODYyMzEzNjA3MDA4MTk3ODIwMTMzOTI3MTEzNzYzNjIzNzM3Mzk1MzAzMTI5ODQxMTMzNTQ2ODgyNTI2OTMxODU5OTI5MTY1ODUxNzQ0OTk4MDk2MjM3NTcyMzU0NDA2NTcyOTk3ODExODIzMDIwNTg0NTg3NzU1OTQxOTg0NDU1MjI2NDAyNjE0NjAzNzExOTg4OTQ4NzU0MzE0Mzg0MzE5MTE4NjE0MzQzNjkxNTYwNDA5NzQwOTkzNjkyMDA4MjMwMzQyMTU5MjE4MzIxOTAwNTc1MTQ1MjYzNTkzMjMwODg4Njk2NTEyNDIxODg2NTQ2Mjg2NjQ1MTcyOTE3NDg3Nzc1My4iLAogICAibnVtIiA6ICI1IiwKICAgInBrMCIgOiAiMjYwMzExNjk0Mzc4MjQ4NjQwMTQyNTQ5NzY4MjQ5Njk0NjEyOTg2NTQzNzM2ODAxODE2NTM2MjU2NzE2MzY3NzM1MDM0MTAyMjEzMzc1NzkwOTc5MzM2NDUwOTE4MDUxNzkxNzgyMjU4NjE0MTQ1MDAzMTQ3NzU1OTYxNjIwMzUzMzU2OTQ5MDE1NTA4MjYyMjkwMTk2NjM5ODYxODI3NDQ0MzE2MjY2Mzk4ODQ1NTQyNzk1OTUyNjAxMDM1MTcwOTg1OTk5Nzk4MTUzNTQwMTQ2Nzg0OTc2MzI3MDkzNzc3MjQ1OTg0NjI1NDIzNjEyMzQzNzYzMzYyMTQ3ODE1MzE0MjQwODYxNjgyNzY1MzA5NTI5NTUzMzI2MzI1MDI4MDI1MDg1NDYzNjY2MjQ3MTI2MTIyNjg2OTYwOTQ3NjQzMTQ5OTM4OTgyODM1MjU0MjIwMTY4NjkyNDc5MDg5MTk5NjkwMDE1NDA1Mzc1NDk4NzAwMjQ1NDMwMjYxMTcxNTA0NTMyMDMzMTEzMzU4NDc2ODI3NTYyNjE3MzUxMzA3NzAzMzcxOTg1Mjk5OTYxNjQyNzM1OTAxOTgwODQ1MzA2ODgwMjc2NDI0MzU0ODc3MDE5MjMxNTAyNTA0NjczMjE4OTQyNTI2NzQ4NjE1ODMwMzExMzcxNjg3NDU0Mjk0MDQwNTE0MTMzNTkwNzQyMzY2MjU1Mjc5ODg1MjUwODAxNTkyNjI4MjMwMTg4MDE2MTU4MzE1MjgzMTYwMzE4NjQzNzA5Njg5NjY1NzI1OTE0MjExMzU5MDUwNzM1MTQ3NDI0MDg3OS4iLAogICAicGsxIiA6ICI3NDMyNzE1ODU1Mjg0MDQxMzEzNjMyMTk2OTQ0NTQ4OTU5NjYxNzIyNDU2MzY3NzkyNTk2OTc5ODQyNjkyNDYwMDQxODM2NTg0OTUxNjcwODE1OTE0MzYxMjE3NTAzMTMxNjU5MjY0ODA0NzIyNzc1MDYwNjkyOTEzMTk4MjA0NDg0NzIwMTI1MTM3NDY2Nzg2MzUwNDI5MjI5MDg0MzI5MTIxOTgzMjY5MjUxMzI2MzM1NjY1NjkwOTU0MTQ0NzU3MzAwMTcwNTkzNzE0NTY5NDg1Nzc0ODE3NzYzMTY2NjIyODQ3MDc1OTc3MDA5MzQ0Nzg1NTMwOTM2MDYxNDM2MDU0MjMwMDgyMDg3ODEyMzMwMTUzODA1MTk1MzA3NzY5Mzc2NDc0NzI1MjE2MDQ5NzI1NDM3ODY4MjQ0OTQ4NTM4ODg0Njc0NzM1MTA5NzEwNDE1MDI1MDQ2NjE1MDY1NTgwNzUwNjIzMzI1MjgwNjUyMzY3MTgyMjI4NTY3MzQ5NjQwMjEyNTkyMzk1NDU5NjE4NTQxMTI2ODE5Njk2OTQ2NTY1OTY2OTA4NzIzMDc4MDI3ODY5NTE4NjczMzYxNzg2NTE4MDYzMDUxODAyOTM3OTcwNDMwMTY3NDMzODQzNjgxNTIzNTkxNTQ1Njg5MjY0Mzk5Njc4NDE3Njk5NTQ0Nzc0ODA0MzI4NzM3MTQzNTk4NjM3MTE0NTcxMjY5NjgwMjAyMjczNzUyMDkyMDAxMTc1MDQ4MTIxODE3Mjg3MTc3ODc1ODUyMjcyNDY1NTM0Mzk1ODgxMjc5NjgyNzI2NTI5OTQxLiIsCiAgICJwazIiIDogIjEzMzU3MjkzNTA3NzgyNjYzMzQ0NDY0MjY1NjgyNjM4OTE1NjU0OTYzNDEzNDM2NjE4NzUyMjk5OTc1NDYxNjUzNTIzMzg1ODc4NDc2Mjc4MDQwMjMwODA2NTc0MzIzNzg4NzAxNTk5NTgzNjk4MjQzMzE2NDM0Nzk0NzUwNDcxNjY2MjgwMzI0NTg2NTA3Mzk1OTI0MzU5MDg0MzUyODE0OTQwMDU5NzMzMzkyNjQ2Mjc4NjIyNzkzNTYzOTAwNzAwMzM4NDQ4OTA4NTc4MzQ5MTYzMjA1NTI3OTgyNTY0NTAwMTQ0MTE1Nzk1NjUyODU5MjYwNzgwNDAzOTk0NzM2NjA1ODU1MDcwMTkwNTg5ODIwODIxODc5OTQwMDg5MDUxMzgwNjkzMDAwODIzMzU4NzU4NzUyMjY3NzgzNTEwNDc3NzY3ODcwMjMxNjQ4NjMwODgwMjEyODIzNzYzNjg3MzM0NzEyMTM0NjU4OTQ1MjE5ODg1MTU4NTAzODM5MTgyNjU0NTcyMjg0OTE1NTA5OTE2MDk5Mjk5MDMxMjkwMDMyNjg2NzcxNzQ1MDUyMjM3ODcyOTc2NjA4MDcwODgwNzU2NTc2NjI5NjM0NDM0OTEwOTg3Mjk5MDM1NDc2NDg3NTgyMTAxMDMzOTk2MTAxMzUxNzk2ODk3Njc4MjI3NjQ0MTc5NTc4NTAxOTU5MTY1NjcyMTIwMTExNDAxNjc2NjQ5NDcyNjAxNjQ0Mjk5MDk5NTY0OTg5OTkzNjIzMjU4NDgyNTQzNTIyODIwOTM4Nzc3MzQ4MTY2ODc2MzY1MzAxNDkxMzYzLiIsCiAgICJwazMiIDogIjE5NzAyNTYwNzA2NjU3NTM3MjE2NTY2NTE5NTk1NTQ1MzMxOTMzMjE1NzkwODI4ODI1MDUxODQyMDY0MzkxMTQ1NjE5ODAyNzAzNTQzNDE3NjAwNjYzMDc3NjgyOTYyNDU3MDUwODk5NTA4NjM0MDg0NzIwMDkyMDc1NDEwNzYxNzA5NTQyOTA0MTQwNTQyMzI1MjkxODI2MjI3MDY4NDAzOTkzMTE4NzkyMDc0MjM1ODY1Mzg5NjQ4MTQyOTMwNzM4NDg1NDk1OTc5MTkyNzkyMzc0MTUxOTE3MTM2MDgyMjA1NTI3MDgxNTQ3MTQ5MzkyODU2NzYyNDkyMTk4NTQ2ODE1Mjk0MjE4NzkyNzQ0NzE3MzgyNDY0ODcyMjAxMzgxOTYyNzQ3NTIwMTU4ODUwNTEyOTkwNjk5MzMyMzIyMzM4NjE5NzEyMTM5NjY2MTEzNzkyNjIzNDk1MTk2NTU0MDg2MDk3MzA1NDQ5NDU3NzkyODEyNjU1OTM0Nzc0OTM2ODk5NjI1NDUwNzU0MTY5MTc5MjMzNzgzNzc1MTAzMTM4Nzg5ODgxNTYyNjQ4NTkwOTUzMjQ4ODE3NDExODc1OTMzMTA5ODI5MzA2ODk3NzA2MTgzMTMwNzE2NDYxODAyMjM3MDE0ODQ4MDY4NTg0ODk0MDkwMjU0NDg5OTAyMTc5Njg2MzEwODM0ODk4OTAyMzAxNTg1Mzg1MDE5NjEwOTc0MjA0OTUxNjEzODk2MjA5NTA2MjU4ODE0OTA5MjMzMTc4OTIwMTY3MTY1OTA3NjU0MDkxMzkxMTU1NzU0MTQ5MDMxMzA1LiIsCiAgICJwazQiIDogIjk1MTg2MDMzMTQwODg1MzM2MDY0NTU4MTQ5MjU0Nzc2NzU0MzIzNTAyODI3OTU0ODE4NzM2MzQ3MDA5OTIwNTg0ODI0MDQxMTgyNDUxOTQ2MTc1NDg3NDUxMzgyNzM3NzM1ODQ4ODA0NDQxMTA2MjIxNTM1MTEwMjU4NjA0NjY2NTkxNDUzNjE1Mjc3MDA1Nzg2OTE0OTM2OTc5NjQyNDE0NTgyMjcxNzIyNzE0MTg2ODAxNjMxMTk5MzE4NTk3MDQwMTE2NjYwMDY0MTIyODg2ODQxODU2Njg0NjIzNzQwOTgxODk5NDY1NjU0NjYyNzY5NDc2MTE4ODgxNzIwNTE1NzkxMzgxNTkzNTgzMTE2NjI2NTQ0MTI3MzEwOTA0NTg3MzU0MjkzMDA0OTg1NTU5NjIzOTgyMTE3MDQ5MTU1OTY2OTQ1NTc3MDAzMTk5MzczODUzMzcxMjIzOTkxNjkzNDU5NDgyNzA3OTMwNjA1NzE2OTAzNDY5Nzg3ODE4Njc3NDAzNjU1ODc2ODMyOTg4MTkxNTcyNTMwMTg3NTcyNTQxMTAyMTg4NDEzNzEwMjczOTkxNzMwNTcxOTIxMTUwMzk1NzcwNzc2NDk1OTg2NDE2NDMxOTE1MTkzMzEyNTI5MjI0OTQ5Mjk4MjMzNjUyOTAzMTY2MzMwODcwMDIwNzAwOTUxMjA2NDAwNDc0Mjk3OTQxMjgyMzQ1NzkzMzc5OTAwODg2ODU0NzkyMjg5NjE0MTQyOTY5MDIyNjI2ODM0NDI3NTQyNTExNDIyMjEyNzYwODYzMzE0OTI5MDc4MjMwNzkzMzguIiwKICAgInMwIiA6ICI3MTY4NTAzMzQ3MDA4MjMwMTQxNjI1MDg4ODc3Mzk3OTYzMDkyNjQ0NTY5NTY5NzExNjc5NTMzMDUwMTk5MjQ3NTcyMDk4NzI0Mjk3NzE3NTAwOTgzNTUyNzgzOTYwNzk5Njg3NzAxNTYxMzEwNTAzNDkxNjU0NDQzODk2NjEzOTA3MTAxOTg0NjQ5NDc4OTc1NjgwNjg3NjIwMjE4MTI0MTA5NTA0NzcyNzQxNzQ1ODA4NzQwNzczMjM3ODY5MzIxOTQzMjc0NDE0OTk1ODQwMjIwOTUxOTg4Mjk3NDU3NzI1MjIyODE1OTY3ODA2MDczNTg5NTk3MjI0MzgxNzM5Mjc2MzY3NTM0NjA2MTE5MDI3MjA0MTQyMjIwODA2NjU0NTY2Nzk2Mjc1ODEwNjk0MzM2ODg5NzIxNjU3NDM4NDUzMjg2OTM4OTU5MTQ4MDA4OTkyMTY3OTQ0OTU2MzIzMjI3OTM0Njg3NDEyMjc0Mzg5NjM2MzI5OTAwNDA4NDAzNjMzNjgyOTc4ODM0MjI4MTY5NjQwNDQwMTcwOTcyMjkzODExMjg1MzgwNjE0ODA4MDMxOTI5NzY0NDU4MjYxNTUzNzM2NjI2MTYxMTcwMzMzMTM0NTIzNDM2MDQ5MDE5NzI2MDk3NTM4Mjc0NTYzMjE5MjEwNzQzNTE3NDI3MzMxMzc0MzM3NzIyNTQ1Mjg3NTYzODI4MjQ0Mjg3NTI0Nzg4NTI1NjYzMzkyMjA3NDg1OTYyMDk2ODY4NzM3NjEwODg3MzEyMDIyNDAzMDkwNzg1NjIwNDM0Mjg1ODA2MzgzMzg5MDUzLiIsCiAgICJzMSIgOiAiNTkyNTU2MTA5MjYxMzgxMTExMjUzNDYyMDA4NjY3MjY5ODQyNjkwNDM1MTkwODE0OTI2MTYxOTY5MzgyOTU3OTczOTc1MDAzMjI3NDc4MDE4MTI5MjczMDg0NTA2MzEwNzI5NTg0MzczNDM0MjQwOTIyODIzNTQwMzA0MjY1NTM5MTY3MTI4MjgyNzg4NzE1NjUzMjI1OTc0NzI2NzE0NzcwMzA4NjM4MjAxNDI3MzkyODQ0NDQzMzU4MzY3NTg1MDA4NzQyNzU0MjM3NjQ2NjMyNjY2MjgyNTk5MjU1NTQyMDM5OTcwMjU3NjEyMjY1OTk5MjMxNjcwNDk0MTk1Mzg0MDcxODc1ODkyNDQwMjAyNDc3NDI3MjM3MjA3NDUzODM4NzE3NTI2NzkzMTk4OTQ5ODIwNTE3MTM0NjQ0NjE1MzI2MDcyMTgxNDIxNjM2MTM3NTc5MzkxMjY5MzY2NTA0MDIxNDc3OTc1OTIzNzUxOTY5Mjg5MjgxMzQ2ODg2MzgwOTIwNjIyNjUyMTM4MjA3MjI0Nzg4MDk1NjM1ODM4MTY4MzYyMjQwNzk1MDk4ODQ4MDQ4MjM1MzE2NDMyMjU1NDg5MTI2MzA1NTM4NTk5OTU0Nzc1NjIyMTEzNDI1MTY1ODYyMzgzMDYxNjc0NzExODk2NDQ4NDEzOTY1Mjk0NDAzNzQwODUxMzIyNTU4ODI3NzA0NTgwODE4MDk2MjE3ODIxMzYwMzg0NDQyOTg2OTg3NDkxMzc3OTE0ODQwNTU2NDA5NzYyMTgyMDg4MDg3MjY3MjYwMDA3ODU3NDE2MjczMzgxMS4iLAogICAiczIiIDogIjEzMzQzNDAwNTc5Nzc2NDYwNjI0OTg3MTM5NDgxMDQ2MjQzMDYzMjU1NTg4MjQyNTEyOTgyOTMwNDA5MzY4Mjc4MjMyODQ4NjUzNzE4NDAzNjg2NzYyNTE2NjU0OTY5NTQ5ODE4MzA0OTk5Mjk1MzQyNDg0NTgxOTY1Mjc4MzA1NDE1MDUyNzg4NDM5ODgzMzIwNDUwOTQyNjAwNDIxNzE1MDQ1ODU2NTE0MTc1NTMwMTg2MDc4ODkzMDA5MjUzNDc0NjM0NzkyMTM0Mjc2ODAwMTM5Nzg4MTY2OTIwNjI5NTI4MzMwMjYzMjE5MTUxMDk3NjkxMDAzNDk0OTQ1NDg0ODg1NzU2ODM2MzQ1ODAwMjEyMTgyMzQyNzE3NzQ1NDYwMDY3MjMzMzc0MjM5MDkwNjE4ODc2NjIzMzExMjYwNjYyODEzMTg3ODQwODc5OTc0NzgyODkxNDkyODgzOTkzODUzMzExNjYyMjk2MzE4NDc5MDQ4OTc3MjEwMjQ0NTU4MDgyNzg3NDQzNzM3MzM3MzIwNjQwNTM2MzM1NzAxNTYxNjE3MDQ1NzgwNjkzMjU3NDE4MTI1NTU2NzQ1NzQ4OTE5OTgyNjQxMzY5ODQyNDUzODE5ODU4NjUxNjE4NDg5MTU2ODM3NjYwMTMzNTc0MDMwMTA1MTc3OTczNzEwMTE1MzczNDMzMTQ4NDY4MjY1NTA3MjEyNjk5MTI5NDg4NDk4MDg5Mjc3MjU0NDQ0MTczOTgxMzYxMDM1MzE0MjgxODMzODI2OTY5NzUyNDE5NTA0NDQ2NDU4MjgwMTM3OTk0MzA3MDA3LiIsCiAgICJzMyIgOiAiMjM2OTE4NDc4NTA0MjI4MzA4NDIyODQ5MDk2MTIwNTQyODEyMTYyNTkxNzcyMDAzNDAxNDk2NzAzMDc3MDQ1NzEwMTUzMjk2NzkxMzM0NjYyNDQ2OTcwMDc5MTc4NTMzNDM5MzQxNjcwNTYzMDk4NzIyNDEwMjM2OTU4Njk5Mjg1MjYzNzk4ODQyMzg0MTgxMTY1Mzg3MTAzOTMyMTg0NTU2NzgwNjE4MDAzNzE0MzIzODk5MTQ3NTYxMjY1NjYzMzA5MDQ1ODc5OTkyMjc1MDc0NzAwMDg0NzM4MjQzNDA5MzE1OTYzNjQwMTIwMjg2NTYxNDQ1MTUxMjQ1MjQ3MzY5ODY1NDAxOTQ3NjY1MjI2MzUyNzQ4ODY5NjAwMzczNDY1Mjg0NzAxMzUxOTcwMzk0NzYxNjc1NDg5MjY0OTA5Mjg0NjczMDA1NDUzMTAzNjI2OTg5MTU2MjA5NjI1NjY1MjcwNTA3OTkxMzcxMTI2NDE5NzI3MTEzOTgxODAxNjQyODg0MjMzNTkwNjQ5MDIzNDIxNzU2NTI4Njg4NDg0NzA4NTQ4OTkyODIyMzM1NTgzMTExMjY3ODc2NDA3ODk3Mjk2MjY3MDczNzkyNDI4MTk2NjY2NDU5ODU2MTU3MTgxODQwMDUyMzQ3ODQzOTkwNDY2MTQ0NDE2MjYwMjc0OTM1OTY1ODU2OTg1Njk5OTI4NjM4MTEzNDYxNzUzOTYwMjQxMTc3NzQwOTM5MDE2ODM5MzQ0ODcwOTg4MjY0Mjc3NzgzMzA2ODcyMjM1NTE3ODQwNzkzMzk3MDQ2Mjc1MzUwMTUzNS4iLAogICAiczQiIDogIjEyMzA2Nzg0NTMwMzE2ODQ0NDY0NTg4MTgwOTk4NDI0NTU4NDgxMTM5MTQyMDgyOTE3ODEwODkxNTU5MjM1MjQ5MTQ4NjcyNDE3Nzc3NTc1NTIwODEyMzY0MDExNzk5MTMyODIwNTIwMjg0NDEzMDY5NjEyNzg2Nzc0OTUxMjc1NzI0MTA5MzQ3NjY3MDQ3MzIyNDMzMTA4OTMwMDkwNzk0NjgyNDg4MDkwMjY5NDA2MTAwODIxNDU0MTgyMzAyNjgwMjE1NTU1Njg2NTE2NDM3OTQzMDcxNTE4MzI5NDE0MDk3Nzc3OTg0MDU4Mjk1ODQyMzg1NzY0NTAzNDQyODk1MTUwMjYwMDAzNjkyOTYyNzcwMDQxMjQ0OTg1NzM2MTQ3MjU0NDE0NjE3NzMzODY1MTQ2OTkwMTIzMDg2ODIyNTgzNjA5MTAyNDYxNzg3NTcwNTUyNjE0MDc5MzUyMjgxODYxNTA0MzgzNDc4NzQzNTcyNDI5OTgwMTExMzU2Mzk1MzYzNDkxMzMxOTk0NjMwOTIzMzgwODAzODA4MzY4MzA0MTQyNTgxNTAwNjk2MjA0NDAyNzY1ODQyMTM3MDQ2NTczMTIxNzY5Njk4MTkxMjI5NTYzNzg1OTEzNjk3MTY2MDUxNTgyMzQ2NDgyMDEwNDE0OTYwODQxNDc2ODU2Njg0MzEzNzIxMjc4MzczMjUwODQ4MjUxMjA4NjU5NTY0NDgwNTEzMTkwMjIxNDY0MjczNDcxNzUzMDIxMjk4NTEwMjkxMTE3NTU2MDc0ODMzNDA2NjY0OTE1ODQxMDMwNTMyNzQyMjQzLiIKfQo="

#     setup_ring(ring_name)
#     member_pos starts from 0
#     ring_size = join_ring(ring_name) + 1
#     if ring_size <= 1:
#         exit(0)
#     member_pos = str(random.randrange(0, ring_size))
#     linkable_ring_sig(ring_name, message, member_pos, ring_size)
#     linkable_ring_verify(ring_name, message, sig)
#     get_ring_param(ring_name)
#     get_public_key(ring_name, member_pos)
#     get_private_key(ring_name, member_pos)


