# nomixplorer
Attempt to index and display some useful data from Nomic chain

Simple python tool to listen and decode new "tx" event from tendermint RPC websocket


```
++Rcv raw: b'\x81~\x03\xf1{"jsonrpc":"2.0","id":"sub-0","result":{"query":"tm.event = \'Tx\'","data":{"type":"tendermint/event/Tx","value":{"TxResult":{"height":"10753650","tx":"eyJtc2ciOlt7InR5cGUiOiJjb3Ntb3Mtc2RrL01zZ0RlbGVnYXRlIiwidmFsdWUiOnsiYW1vdW50Ijp7ImFtb3VudCI6IjM3MDAwMDAwIiwiZGVub20iOiJ1bm9tIn0sImRlbGVnYXRvcl9hZGRyZXNzIjoibm9taWMxcXFnZ2E3ejdmcnptbWF2cWg0YTN5cHloMHo1aGQyeTdrbHdscmQiLCJ2YWxpZGF0b3JfYWRkcmVzcyI6Im5vbWljMWxqNGR6NHAycnRhYzhtbHp6ejg2N3FqNnk3MDd6Z3Q3Z2dkZHgwIn19XSwiZmVlIjp7ImFtb3VudCI6W3siYW1vdW50IjoiMCIsImRlbm9tIjoidW5vbSJ9XSwiZ2FzIjoiMTAwMDAifSwibWVtbyI6IiIsInNpZ25hdHVyZXMiOlt7InB1Yl9rZXkiOnsidHlwZSI6InRlbmRlcm1pbnQvUHViS2V5U2VjcDI1NmsxIiwidmFsdWUiOiJBd0J5cFJUbkVGM2RLYkFIRTU4WmdqSHF2SDRpSEd5SVcwT0R1c1I2TW8zcyJ9LCJzaWduYXR1cmUiOiIzM3dWZGxpbmNZaEtLeXlEZEhTelZBRkhkdngvdXQwTTllTTdhN2pZUC8wTE95SHJ1eHV5ckRrWUNpcHJnZXhxa1F0dEFRUmF5YVZZclpXRHF1ekVRUT09In1dfQ==","result":{}}}},"events":{"tm.event":["Tx"],"tx.hash":["EBDFE78FB6929B7BEBD777D2A4C8F40435AF761F8969CE0A65C54587EA91C997"],"tx.height":["10753650"]}}}'
++Rcv decoded: fin=1 opcode=1 data=b'{"jsonrpc":"2.0","id":"sub-0","result":{"query":"tm.event = \'Tx\'","data":{"type":"tendermint/event/Tx","value":{"TxResult":{"height":"10753650","tx":"eyJtc2ciOlt7InR5cGUiOiJjb3Ntb3Mtc2RrL01zZ0RlbGVnYXRlIiwidmFsdWUiOnsiYW1vdW50Ijp7ImFtb3VudCI6IjM3MDAwMDAwIiwiZGVub20iOiJ1bm9tIn0sImRlbGVnYXRvcl9hZGRyZXNzIjoibm9taWMxcXFnZ2E3ejdmcnptbWF2cWg0YTN5cHloMHo1aGQyeTdrbHdscmQiLCJ2YWxpZGF0b3JfYWRkcmVzcyI6Im5vbWljMWxqNGR6NHAycnRhYzhtbHp6ejg2N3FqNnk3MDd6Z3Q3Z2dkZHgwIn19XSwiZmVlIjp7ImFtb3VudCI6W3siYW1vdW50IjoiMCIsImRlbm9tIjoidW5vbSJ9XSwiZ2FzIjoiMTAwMDAifSwibWVtbyI6IiIsInNpZ25hdHVyZXMiOlt7InB1Yl9rZXkiOnsidHlwZSI6InRlbmRlcm1pbnQvUHViS2V5U2VjcDI1NmsxIiwidmFsdWUiOiJBd0J5cFJUbkVGM2RLYkFIRTU4WmdqSHF2SDRpSEd5SVcwT0R1c1I2TW8zcyJ9LCJzaWduYXR1cmUiOiIzM3dWZGxpbmNZaEtLeXlEZEhTelZBRkhkdngvdXQwTTllTTdhN2pZUC8wTE95SHJ1eHV5ckRrWUNpcHJnZXhxa1F0dEFRUmF5YVZZclpXRHF1ekVRUT09In1dfQ==","result":{}}}},"events":{"tm.event":["Tx"],"tx.hash":["EBDFE78FB6929B7BEBD777D2A4C8F40435AF761F8969CE0A65C54587EA91C997"],"tx.height":["10753650"]}}}'
{
    "msg": [
        {
            "type": "cosmos-sdk/MsgDelegate",
            "value": {
                "amount": {
                    "amount": "37000000",
                    "denom": "unom"
                },
                "delegator_address": "nomic1qqgga7z7frzmmavqh4a3ypyh0z5hd2y7klwlrd",
                "validator_address": "nomic1lj4dz4p2rtac8mlzzz867qj6y707zgt7ggddx0"
            }
        }
    ],
    "fee": {
        "amount": [
            {
                "amount": "0",
                "denom": "unom"
            }
        ],
        "gas": "10000"
    },
    "memo": "",
    "signatures": [
        {
            "pub_key": {
                "type": "tendermint/PubKeySecp256k1",
                "value": "AwBypRTnEF3dKbAHE58ZgjHqvH4iHGyIW0ODusR6Mo3s"
            },
            "signature": "33wVdlincYhKKyyDdHSzVAFHdvx/ut0M9eM7a7jYP/0LOyHruxuyrDkYCiprgexqkQttAQRayaVYrZWDquzEQQ=="
        }
    ]
}
```



Not all messages can be decoded, maybe protobuf encoded or other:
```
++Rcv raw: b'\x81~\x01\xe5{"jsonrpc":"2.0","id":"sub-0","result":{"query":"tm.event = \'Tx\'","data":{"type":"tendermint/event/Tx","value":{"TxResult":{"height":"10753641","tx":"/wEfDR8DyCj8GJ0LwwKKXFHITH9gatIiJ0oY/Ydq/DEIwStuRGruJWUWK6hDD+R7QYFNIVKDKev4rhU00whqJkxyAQL3uWyutnlx1/EcY+m0Q7SijwIEPkE81TU0B7FDhm0ADQBub21pYy1zdGFrZW5ldC0zAQAAAAAACLHzAAAAAAIBRQAAAAFA","result":{}}}},"events":{"tm.event":["Tx"],"tx.hash":["DC4B7AF9044624A063CD3F7CE1A137852C15B42D02BE3E9B25CAE84847986686"],"tx.height":["10753641"]}}}'
++Rcv decoded: fin=1 opcode=1 data=b'{"jsonrpc":"2.0","id":"sub-0","result":{"query":"tm.event = \'Tx\'","data":{"type":"tendermint/event/Tx","value":{"TxResult":{"height":"10753641","tx":"/wEfDR8DyCj8GJ0LwwKKXFHITH9gatIiJ0oY/Ydq/DEIwStuRGruJWUWK6hDD+R7QYFNIVKDKev4rhU00whqJkxyAQL3uWyutnlx1/EcY+m0Q7SijwIEPkE81TU0B7FDhm0ADQBub21pYy1zdGFrZW5ldC0zAQAAAAAACLHzAAAAAAIBRQAAAAFA","result":{}}}},"events":{"tm.event":["Tx"],"tx.hash":["DC4B7AF9044624A063CD3F7CE1A137852C15B42D02BE3E9B25CAE84847986686"],"tx.height":["10753641"]}}}'
Error decoding UTF-8 from transaction: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
```
