import pytest


@pytest.mark.usefixtures("dataLoad")

class Loaddemo:
    def test_datatest(self,dataLoad):
        print(dataLoad)