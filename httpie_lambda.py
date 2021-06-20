from httpie.plugins import TransportPlugin
from lambda_requests import DEFAULT_SCHEME, LambdaAdapter


class LambdaTransportPlugin(TransportPlugin):
    name = "AWS Lambda invoke transport"

    prefix = DEFAULT_SCHEME

    def get_adapter(self):
        return LambdaAdapter()
