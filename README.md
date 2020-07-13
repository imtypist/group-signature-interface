# Achieve anonymity-yet-accoutability in blockchain-based VANET systems by using group signature

### workflow

```
+----------------------------------------------------------------------------------------+

gpk: group public key
gsk: group secret key
gsk_ra: group secret key of RA
gsk_ve: group secret key of vehicle
pk_ve: public key of vehicle

+----------------------------------------------------------------------------------------+

+------+  create group: param  +------+
|      | +-------------------> |      |
|  RA  |                       |  RA  |
|      | <-------------------+ |      |
+------+  gpk, gsk, gsk_ra     +------+

+---------+  join group: gpk, pk_ve  +------+
|         | +----------------------> |      |
| vehicle |                          |  RA  |
|         | <----------------------+ |      |
+---------+  gsk_ve                  +------+

+---------+  sign message and post transaction  +------------+
|         | +---------------------------------> |            |
| vehicle |                                     | blockchain |
|         | <---------------------------------+ |            |
+---------+  return OK                          +------------+

+-------+  verify signature of message  +------------+
|       | +---------------------------> |            |
|  RSU  |                               | blockchain |
|       | <---------------------------+ |            |
+-------+  return OK                    +------------+

+------+  reveal someone's real identity by signature  +------------+
|      | +-------------------------------------------> |            |
|  RA  |                                               | blockchain |
|      | <-------------------------------------------+ |            |
+------+  pk_ve                                        +------------+
```

### group signature

![group signature](./group-sig.png)

### performance

The experiment setting is that using a virtual machine (VM) `ubuntu16.04` running on VirtualBox, the number of VM's CPU core is 2, the size of memory is 4GB; The localhost CPU is Intel i7-7700, the size of memory is 16GB. In this experiment, the implemented group signature scheme is [BBS04](http://crypto.stanford.edu/~dabo/abstracts/groupsigs.html) and the ring signature scheme is [LSAG](https://www.semanticscholar.org/paper/Linkable-Spontaneous-Anonymous-Group-Signature-for-Liu-Wei/3c63f7c90d79593fadfce16d54078ec1850bedc9).

- [test_group_signature.log](./test_group_signature.log)
- [test_ring_signature.log](./test_ring_signature.log)

> Note that maximum ring size is hard coded as 32 in [FISCO-BCOS/group-signature-server](https://github.com/FISCO-BCOS/group-signature-server/). Here I set it to 1024 for testing a larger ring size. You can change it by yourselves.

- [test_revoke_member_1024.log](./test_revoke_member_1024.log)
- [test_revoke_member_512.log](./test_revoke_member_512.log)
- [test_revoke_member_256.log](./test_revoke_member_256.log)
- [test_revoke_member_64.log](./test_revoke_member_64.log)
- [test_revoke_member_32.log](./test_revoke_member_32.log)

In this experiment result, I added the performance of `revoke` and `update member private key` operations. To achieve that, I implemented `revoke_member` and `revoke_update_private_key` RPC interfaces, which are not yet implemented in the original repository. If you want to use them directly, you can git clone from [imtypist/group-signature-server](https://github.com/imtypist/group-signature-server).