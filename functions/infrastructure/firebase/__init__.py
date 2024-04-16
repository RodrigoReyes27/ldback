from os import getenv

from firebase_admin import credentials, initialize_app

creds = {
    "type": "service_account",
    "project_id": "frida-research",
    "private_key_id": "3f0287837cdfcd5c0455740ee45b05143f0c8a0a",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDVR1Ii3ehsqVdw\nPubk0lJwD4DEsDInr8tMYapgT2SjKVcdTiIufpuAu0FaoxvgM4TGI4V6ydxsI5vf\nwfWCQVYfnv3XbXO81m63xdxOBPxcIPFDxV44KiHf73ztiHHAgKaNq1fWWDO0zUQO\nSVfEMCGke5wD3y4xU2s7OBdyhcufrEumwDZnSHE4t+UdfoGQPcRPPcNjOuXGVf57\nVWAgzfAMgjKIKcGTP8K8knsDuDUXbn45a/vLZs3+v8MF1zEmpOVR37ojI362QxEd\nb8di+SDFiOv+L7cSHrGPU3fBHf1FOrGATtWeE+GnZR5pOUXZ3TrqfdR5y91my7wC\nmcP5IoazAgMBAAECggEAIbJniUe7SbPFs1/U1jFewgLJCwp1miydt780jovssBS/\nhUtLfkIVqpSrYjkkFdu97ho9pCVRlKpZndREyGQvScayf391ClBs5M83nAIQpzOz\nOsxrsv8BJCLv/42Pv2T0K6z3L0/3N2k5B/LRkZczMYwwHbJ812FBL3WQytDV16+0\nn0yBS4cz38YL0Fe72k2bLYk2RBWp5XAhUf6z73iOgO4X9iGj+XNedG12yjci5Rv+\n4P93nB9vGM0qRKH7mBvmfpdDnQ6keENkllgMtHbJ4i1mDPSv1XVKM2AZfNS8uLgv\nBWvPA2zVpcADzWVzlCpZWYU4Hb/IoK9gugnuEMVBcQKBgQD9Jq2E8C8gFonbiYDk\nNwbr9mrNQspI3jA93BtXpN0m/vsqbaIwWhiHAQDw6UfBmY+gbyEzGYAmPtFvoher\nRlqMGvoiMHXylnGHtvB337scMDBPe8jo8zJI63GDHL6C+E81d6g7MnIvtYkrRHAx\n6LjWS84L/qGPFkTU9xKJogWlsQKBgQDXrcV3hldNIP69NbTMiFBJPlkN8/ByTj4i\nxXk0GsPNLpfCg32psoM+jmNjOJdpqHJ9sJ7ajjL4sFYWuRmY/DQVFsMftZq7aRC/\nBRhyclsyCdlRCC/skHNx4ffp3UTGZo9+nWRSLCUyp0n34WUohXw5HBIH+NM+tvsx\nIZcSt0E3owKBgQCZoch6vj0LT0JYvqk/VvnXaBPHADq9YEKMuDDLztz8FpCdXi2p\nBHSQMha9HgYTQzt8FRVj6pzwGP2HryqIIkk/b/vPlfNuxsidoXNsfJYUdFZNVoVG\ngplI0cJw3Jft6f5AJ58sVeAgfh6B6KXiVCcgvp6MfvrTWKNrT4qrhm3A8QKBgHII\nBDFvq9Sxrz2mmZLSN3CiMD96TBSDXcLQmYZ86C0hh0dmchg4s79tVQrurs9EKlRd\n/38aU8S8pqeY8fm6zmagBEZNpCOWJy53qTdJUwIfxvBa3cu7i+4YRRU20df7/b45\nxQLVKE2huS//0ZYdDVK8jqP8YOP1ptWRJujUTvz1AoGBAOJ2/VKZ4UYfhpeA0Jyh\nh4e8P9Ocn28QByvf9AVK6upalPowjb2hw5H9FuQNPl5nwj2/c/KVOFal9B+8vB+Z\njcpfDJwXcHgzpCXH1veaIrjnjeqDxSJXFB94isRNEmY+35JNEcVRPDyzMDWvkTfT\n3TVh4R7fJX7WjZNvbmCNBjYd\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-krmnc@frida-research.iam.gserviceaccount.com",
    "client_id": "102526508680269228263",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-krmnc%40frida-research.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com",
}


FIREBASE_CREDENTIALS = credentials.Certificate(
    "./cert/frida-research-firebase-adminsdk-krmnc-3f0287837c.json"
)

FIREBASE_CONFIG = {
    "apiKey": getenv("API_KEY"),
    "authDomain": getenv("AUTH_DOMAIN"),
    "databaseURL": getenv("DATABASE_URL"),
    "projectId": getenv("PROJECT_ID"),
    "storageBucket": getenv("STORAGE_BUCKET"),
    "appId": getenv("APP_ID"),
}

FIREBASE_APP = initialize_app(FIREBASE_CREDENTIALS, FIREBASE_CONFIG)
