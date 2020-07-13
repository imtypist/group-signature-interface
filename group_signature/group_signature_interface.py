import json
import requests
import time
import random

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
        # print("create_group::success#" + str(res["result"]["ret_code"]))
        # print("\tgpk_info:", res["result"]["result"])
        return 1
    else:
        print("create_group::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])
        return 0


def join_group(group_name, member_name, member_pass = None):
    data = {
        "jsonrpc": "2.0",
        "params": {
            "group_name": group_name, 
            "member_name": member_name, 
            "pass": member_pass
        },
        "id": 1,
        "method": "join_group"
    }
    r = requests.post('http://127.0.0.1:8005', data = json.dumps(data))
    res = json.loads(r.text)
    if res["result"]["ret_code"] == 0:
        # print("join_group::success#" + str(res["result"]["ret_code"]))
        # print("\tmember_sk:", res["result"]["result"])
        return 1
    else:
        print("join_group::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])
        return 0


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
        # print("group_sig::success#" + str(res["result"]["ret_code"]))
        # print("\tsig:", res["result"]["sig"])
        # print("\tgpk:", res["result"]["gpk"])
        # print("\tpbc_param:", res["result"]["pbc_param"])
        # print("\tmessage:", res["result"]["message"])
        return res["result"]["sig"]
    else:
        print("group_sig::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])
        return 0


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
        # print("group_verify::success#" + str(res["result"]["ret_code"]))
        # print("\tresult:", res["result"]["result"])
        return 1
    else:
        print("group_verify::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])
        return 0


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
        # print("open_cert::success#" + str(res["result"]["ret_code"]))
        # print("\tcert_of_the_owner_of_the_signature:", res["result"]["result"])
        return 1
    else:
        print("open_cert::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])
        return 0


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
        # print("get_public_info::success#" + str(res["result"]["ret_code"]))
        # print("\tgpk:", res["result"]["result"])
        return len(res["result"]["result"])
    else:
        print("get_public_info::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])
        return 0


def get_gmsk_info(group_name, gm_pass):
    data = {
        "id": 1,
        "jsonrpc": "2.0",
        "method": "get_gmsk_info",
        "params": {
            "group_name": group_name,
            "gm_pass": gm_pass
        }
    }
    r = requests.post('http://127.0.0.1:8005', data = json.dumps(data))
    res = json.loads(r.text)
    if res["result"]["ret_code"] == 0:
        # print("get_gmsk_info::success#" + str(res["result"]["ret_code"]))
        # print("\tgmsk:", res["result"]["result"])
        return len(res["result"]["result"])
    else:
        print("get_gmsk_info::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])
        return 0


def get_gsk_info(group_name, member_name, member_pass = ""):
    data = {
        "id": 1,
        "jsonrpc": "2.0",
        "method": "get_gsk_info",
        "params": {
            "group_name": group_name,
            "member_name": member_name,
            "pass": member_pass
        }
    }
    r = requests.post('http://127.0.0.1:8005', data = json.dumps(data))
    res = json.loads(r.text)
    if res["result"]["ret_code"] == 0:
        # print("get_gsk_info::success#" + str(res["result"]["ret_code"]))
        # print("\tmember_gsk:", res["result"]["result"])
        return len(res["result"]["result"])
    else:
        print("get_gsk_info::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])
        return 0


def test_group_sig(group_name, gm_pass, message, max_group_size = 32):
    # create group
    st = time.time()
    ret = create_group(group_name, gm_pass)
    ed = time.time()
    if ret == 0:
        return ret
    print("create group running time (s): " + str(ed-st))
    # test group_size from 1 to max_size
    for i in range(max_group_size):
        print("=========================================================")
        print("CURRENT GROUP SIZE = " + str(i+1))
        print("=========================================================")

        # join group
        member_name = group_name + str(i)
        st = time.time()
        ret = join_group(group_name, member_name)
        ed = time.time()
        if ret == 0:
            return ret
        print("join group running time (s): " + str(ed-st))

        # group sig
        member_name = group_name + str(random.randint(0, i))
        st = time.time()
        ret = group_sig(group_name, member_name, message)
        ed = time.time()
        if ret == 0:
            return ret
        print("group sig running time (s): " + str(ed-st))

        sig_string = str(ret)

        # group verify
        st = time.time()
        ret = group_verify(group_name, sig_string, message)
        ed = time.time()
        if ret == 0:
            return ret
        print("group verify running time (s): " + str(ed-st))

        # # open cert
        st = time.time()
        ret = open_cert(group_name, sig_string, message, gm_pass)
        ed = time.time()
        if ret == 0:
            return ret
        print("open cert running time (s): " + str(ed-st))

    # key size
    print("*********************************************************")
    print("KEY SIZE")
    print("*********************************************************")
    print("signature size (bytes): " + str(len(sig_string)))
    print("group public key size (bytes): " + str(get_public_info(group_name)))
    print("group manager secret key size (bytes): " + str(get_gmsk_info(group_name, gm_pass)))
    print("group member secret key size (bytes): " + str(get_gsk_info(group_name, member_name)))


'''interface function test'''
if __name__ == "__main__":
    group_name = "test_group_sig18_"
    gm_pass = "test_group_sig"
    message = "0xd91c747b4a76B8013Aa336Cbc52FD95a7a9BD3D9xGPRMC,092927.000,A,2235.9058,N,11400.0518,E,0.000,74.11,151216,,Dx49"
    max_group_size = 1024
    test_group_sig(group_name, gm_pass, message, max_group_size)