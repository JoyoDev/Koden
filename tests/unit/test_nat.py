import unittest
from koden.nat.port import Port


class TestNat(unittest.TestCase):

    def test_check_port_range(self):
        self.assertTrue(Port.check_port_range(8080))
        self.assertFalse(Port.check_port_range(700000))
        self.assertFalse(Port.check_port_range(0))
        self.assertFalse(Port.check_port_range(-8000))

    def test_parse_port_range_when_valid_range(self):
        ports = "80-8080"
        start, end, error = Port.parse_port_range(ports)

        assert start == 80
        assert end == 8080
        assert error is None

    def test_parse_port_range_when_invalid_range(self):
        ports = "8080-80"
        start, end, error = Port.parse_port_range(ports)

        assert start == 0
        assert end == 0
        assert error == f"Invalid range specified for the Port: 8080-80"

    def test_parse_port_range_when_invalid_range_string(self):
        ports = "-8081-81"
        start, end, error = Port.parse_port_range(ports)

        assert start == 0
        assert end == 0
        assert error is not None

    def test_parse_port_range_to_int_when_valid_port(self):
        raw_port = "6443"
        start, end, error = Port.parse_port_range_to_int(raw_port)

        assert start == 6443
        assert end == 6443
        assert error is None

    def test_parse_port_range_to_int_when_valid_port_range(self):
        raw_port = "6443-6543"
        start, end, error = Port.parse_port_range_to_int(raw_port)

        assert start == 6443
        assert end == 6543
        assert error is None

    def test_parse_port_range_to_int_when_empty_port(self):
        raw_port = ""
        start, end, error = Port.parse_port_range_to_int(raw_port)

        assert start == 0
        assert end == 0
        assert error is None

    def test_port_creation_when_valid_config(self):
        protocol = "tcp"
        port_str = "5001"

        port = Port(protocol, port_str)

        assert port.port == "5001/tcp"
        assert port.error is None

    def test_port_creation_when_valid_config_2(self):
        protocol = "tcp"
        port_str = "5001-8081"

        port = Port(protocol, port_str)

        assert port.port == "5001-8081/tcp"
        assert port.error is None

    def test_port_creation_when_invalid_config(self):
        protocol = "tcp"
        port_str = "no_port"

        port = Port(protocol, port_str)

        assert port.port == ""
        assert port.error != ""

