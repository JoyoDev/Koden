from typing import Dict


class Port:
    """
    Class for manipulation of strings describing network ports.
    """

    def __init__(self, protocol: str, port: str):
        port_start, port_end, error = Port.parse_port_range_to_int(port)
        if error is not None:
            self.port = ""
            self.error = error
        else:
            if port_start == port_end:
                self.port = f"{port_start}/{protocol}"
                self.error = None
            else:
                self.port = f"{port_start}-{port_end}/{protocol}"
                self.error = None

    @staticmethod
    def parse_port_range_to_int(raw_port: str) -> (int, int, str):
        """Parse raw port(s) and return int from it"""
        if len(raw_port) == 0:
            return 0, 0, None

        start, end, error = Port.parse_port_range(raw_port)
        if error is not None:
            return 0, 0, error

        return int(start), int(end), None

    @staticmethod
    def parse_port_range(ports: str) -> (int, int, str):
        """Parse passed port range and return starting and ending port"""

        if not ports:
            return 0, 0, "Empty string specified for ports."

        if "-" not in ports:
            start = int(ports)
            end = start
            return start, end, None

        parts = ports.split("-")

        try:
            start = int(parts[0])
            end = int(parts[1])
        except Exception as e:
            return 0, 0, str(e)

        if not Port.check_port_range(start):
            return 0, 0, f"Port {start} out of range"

        if not Port.check_port_range(end):
            return 0, 0, f"Port {end} out of range"

        if end < start:
            return 0, 0, f"Invalid range specified for the Port: {ports}"

        return start, end, None

    @staticmethod
    def check_port_range(port: int) -> bool:
        """Check if port number is valid"""
        return 1 <= int(port) < 65535


"""
PortSet as alias
"""
PortSet = Dict[Port, Dict]
