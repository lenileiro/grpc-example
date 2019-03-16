import grpc

class Credentials:
    @staticmethod
    def get_credentials():
        # read in certificate
        try:
            with open('keys/ca.crt', 'rb') as f:
                trusted_certs = f.read()
            
            with open('keys/server.key', 'rb') as f:
                server_key = f.read()

            with open('keys/server.crt', 'rb') as f:
                server_cert = f.read()

        except Exception as e:
            log.error('failed-to-read-cert-keys', reason=e)

        # create credentials
        credentials = grpc.ssl_server_credentials([(server_key, server_cert)], trusted_certs)
        return credentials