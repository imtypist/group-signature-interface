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
        # print("setup_ring::success#" + str(res["result"]["ret_code"]))
        # print("\tring_info:", res["result"]["result"])
        return 1
    else:
        print("setup_ring::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])
        return 0


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
        # print("join_ring::success#" + str(res["result"]["ret_code"]))
        # print("\tprivate_key:", res["result"]["private_key"])
        # print("\tpublic_key:", res["result"]["public_key"])
        # print("\tmember_pos:", res["result"]["result"])
        return 1
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
        # print("linkable_ring_sig::success#" + str(res["result"]["ret_code"]))
        # print("\tparam_info:", res["result"]["param_info"])
        # print("\tsig:", res["result"]["sig"])
        # print("\tmessage:", res["result"]["message"])
        return res["result"]["sig"]
    else:
        print("linkable_ring_sig::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])
        return 0


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
        # print("linkable_ring_verify::success#" + str(res["result"]["ret_code"]))
        # print("\tis_valid:", res["result"]["result"])
        return 1
    else:
        print("linkable_ring_verify::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])
        return 0


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
        # print("get_ring_param::success#" + str(res["result"]["ret_code"]))
        # print("\tring_info:", res["result"]["result"])
        return len(res["result"]["result"])
    else:
        print("get_ring_param::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])
        return 0


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
        # print("get_public_key::success#" + str(res["result"]["ret_code"]))
        # print("\tpublic_key:", res["result"]["result"])
        return len(res["result"]["result"])
    else:
        print("get_public_key::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])
        return 0


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
        # print("get_private_key::success#" + str(res["result"]["ret_code"]))
        # print("\tprivate_key:", res["result"]["result"])
        return len(res["result"]["result"])
    else:
        print("get_private_key::error#" + str(res["result"]["ret_code"]))
        print("\tfailed_reason:", res["result"]["details"])
        return 0


def test_ring_sig(ring_name, message, max_ring_size = 32):
    # setup ring
    st = time.time()
    ret = setup_ring(ring_name)
    ed = time.time()
    if ret == 0:
        return ret
    print("setup ring running time (s): " + str(ed-st))
    # test ring_size from 1 to max_size
    for i in range(max_ring_size):
        print("=========================================================")
        print("CURRENT RING SIZE = " + str(i+1))
        print("=========================================================")

        # join ring
        st = time.time()
        ret = join_ring(ring_name)
        ed = time.time()
        if ret == 0:
            return ret
        print("join ring running time (s): " + str(ed-st))

        # ring size must be larger than one
        if i == 0:
            continue

        # ring sig
        member_pos = str(random.randint(0, i))
        ring_size = i + 1
        st = time.time()
        ret = linkable_ring_sig(ring_name, message, member_pos, ring_size)
        ed = time.time()
        if ret == 0:
            return ret
        print("ring sig running time (s): " + str(ed-st))

        ring_sig = ret

        # ring verify
        st = time.time()
        ret = linkable_ring_verify(ring_name, message, ring_sig)
        ed = time.time()
        if ret == 0:
            return ret
        print("ring verify running time (s): " + str(ed-st))

    # key size
    print("*********************************************************")
    print("KEY SIZE")
    print("*********************************************************")
    print("signature size (bytes): " + str(len(ring_sig)))
    print("ring public param size (bytes): " + str(get_ring_param(ring_name)))
    print("group manager secret key size (bytes): " + str(get_public_key(ring_name, member_pos)))
    print("group member secret key size (bytes): " + str(get_private_key(ring_name, member_pos)))


'''interface function test'''
if __name__ == "__main__":
    ring_name = "test_ring_sig0"
    message = "0xd91c747b4a76B8013Aa336Cbc52FD95a7a9BD3D9xGPRMC,092927.000,A,2235.9058,N,11400.0518,E,0.000,74.11,151216,,Dx49"
    max_ring_size = 1024
    test_ring_sig(ring_name, message, max_ring_size)


