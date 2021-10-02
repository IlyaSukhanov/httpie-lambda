from io import BytesIO
from unittest import TestCase
from unittest.mock import patch

from httpie.context import Environment
from httpie.core import main
from httpie.plugins.registry import plugin_manager

from httpie_lambda import DEFAULT_SCHEME, LambdaTransportPlugin


def http(*args, **kwargs):
    with BytesIO() as stdout, BytesIO() as stderr:
        env = Environment(stdout=stdout, stderr=stderr)
        main(args=["http", *args], env=env)
        stdout.seek(0)
        stderr.seek(0)
        output = stdout.read()
        error = stderr.read()
    return output.decode("utf8"), error


class TestHTTPieLambda(TestCase):
    @patch("lambda_requests.lambda_request.boto3")
    def test_transport_from_requests_response(self, boto3):
        boto3.client().invoke().__getitem__().read.return_value = b'{"body": "ewogICJmb3JtIjoge30sIAogICJoZWFkZXJzIjogIlVzZXItQWdlbnQ6IHB5dGhvbi1yZXF1ZXN0cy8yLjI1LjFcclxuQWNjZXB0LUVuY29kaW5nOiBnemlwLCBkZWZsYXRlXHJcbkFjY2VwdDogKi8qXHJcbkNvbm5lY3Rpb246IGtlZXAtYWxpdmVcclxuRm9vOiBiYXJcclxuXHJcbiIsIAogICJwYXJhbSI6ICJmb3JtIiwgCiAgInF1ZXJ5X3N0cmluZ3MiOiB7fQp9Cg==", "isBase64Encoded": "true", "statusCode": 200, "headers": {"Content-Type": "application/json", "X-Request-ID": "", "Content-Length": "208"}}'  # noqa: E501
        plugin_manager.register(LambdaTransportPlugin)
        try:
            response, _ = http(f"{DEFAULT_SCHEME}example.com", "--pretty=none")
            assert "200 OK" in response
            assert "Content-Type: application/json" in response
        finally:
            plugin_manager.unregister(LambdaTransportPlugin)
