Achieve anonymity-yet-accoutability in VANET systems by using group signature and zk-SNARK

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

+---------+  generate zk-SNARK proof for proving valid  +---------------+
|         |  identity with submitted message (prover)   |               |
| vehicle | +-----------------------------------------> | SC (verifier) |
|         |                                             |               |
+---------+                                             +---------------+

+------+                                +------+
|      |  run locally, verified online  |      |
|  SC  | +----------------------------> |  BC  |
|      |                                |      |
+------+                                +------+
