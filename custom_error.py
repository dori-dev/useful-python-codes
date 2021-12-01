"""Custom Error in python
"""

import requests


class Network:
    """`Netword` Class
    """

    class NetworkProblem(Exception):
        """Define custom exception
        subclass `Exception`
        """

    def communicate(self, url: str) -> requests.Response:
        """communicate to url

        Args:
            url (str): page url

        Raises:
            self.NetworkProblem: unable to establish connection

        Returns:
            requests.Response: page respones(request.get)
        """

        try:
            respones = requests.get(url)
        except requests.exceptions.ConnectionError:
            raise self.NetworkProblem(
                "unable to establish connection") from None

        return respones


if __name__ == "__main__":
    network = Network()
    # network.communicate('https://github.com/dori-dev')

    try:
        r = network.communicate('https://github.com/dori-dev')
    except network.NetworkProblem:
        print("exception raised, no connection to internet!")
    else:
        print(r.status_code)
