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