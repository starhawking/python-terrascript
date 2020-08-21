# terrascript/data/ns1.py
import terrascript


class ns1_zone(terrascript.Data):
    pass


class ns1_dnssec(terrascript.Data):
    pass


class ns1_datasource(terrascript.Data):
    pass


class ns1_datafeed(terrascript.Data):
    pass


__all__ = [
    "ns1_zone",
    "ns1_dnssec",
    "ns1_datasource",
    "ns1_datafeed",
]
