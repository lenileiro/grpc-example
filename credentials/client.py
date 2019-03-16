import grpc

class Credentials:
    @staticmethod
    def get_credentials():

        # read in certificate
        with open('keys/ca.crt', 'rb') as f:
            trusted_certs = f.read()

        with open('keys/client.key', 'rb') as f:
            client_key = f.read()

        with open('keys/client.crt', 'rb') as f:
            client_cert = f.read()

        # create credentials
        credentials = grpc.ssl_channel_credentials(
            root_certificates = trusted_certs,
            private_key = client_key,
            certificate_chain = client_cert)

        return credentials