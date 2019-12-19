import http.client

conn = http.client.HTTPSConnection("dev-g-e5tghp.auth0.com")

payload = "{\"client_id\":\"B0rVe3D40YHOicByZYZDw84DwPXQTex8\",\"client_secret\":\"QBpNoTFsquyaWAxcJvjKAdgGTSq9zQzVlhw9SqI9N3FRcVYRnvuFqCH8iaqFbJm2\",\"audience\":\"https://faq-extractor/\",\"grant_type\":\"client_credentials\"}"

headers = {'content-type': "application/json"}

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
'''
{"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlFrSXlSRU5CUVVZM1EwSkNRMEUxTmpGRE1EVTBNak16UlVNMlFqQXpPVVl3TTBFeFFUTTNNdyJ9.eyJpc3MiOiJodHRwczovL2Rldi1nLWU1dGdocC5hdXRoMC5jb20vIiwic3ViIjoiQjByVmUzRDQwWUhPaWNCeVpZWkR3ODREd1BYUVRleDhAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vZmFxLWV4dHJhY3Rvci8iLCJpYXQiOjE1NzYxNDU2ODEsImV4cCI6MTU3ODczNzY4MSwiYXpwIjoiQjByVmUzRDQwWUhPaWNCeVpZWkR3ODREd1BYUVRleDgiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.dAAMGHJLFuA3pds0NPS7VY13-s9mMrKu6yfaE7n6SG5_Svn5gSuz7jLILGrAzAYuEAbXf7-YMWHCjjpmEvjHfDEEuDBVk7dTJvXIPi5p46huPEfeKtQxeHsvJFMYfG2kH8HLmzYFYHtdgcfCQoLpSTS3GQgrNEJL2-K806AL_Ap1QoLOFUeFad39yW6OvEqiHF34FlvHq12DN04rUFQzLFtXKT8-pQEztTI6TOt46RmebKW5vmT1-Atiq285P2g4Wc-7QoZM9MieBTDt4OnrUjIRSBIQHBLOx0KdlEJzmqGmMlzh3Jq2S2_TGlg6a-g6XKP3GXMQQ2WvFzPZ4XWqAA","expires_in":2592000,"token_type":"Bearer"}
'''
