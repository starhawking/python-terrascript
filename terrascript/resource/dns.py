# terrascript/resource/dns.py
import terrascript


class dns_a_record_set(terrascript.Resource):
    pass


class dns_aaaa_record_set(terrascript.Resource):
    pass


class dns_cname_record(terrascript.Resource):
    pass


class dns_mx_record_set(terrascript.Resource):
    pass


class dns_ns_record_set(terrascript.Resource):
    pass


class dns_ptr_record(terrascript.Resource):
    pass


class dns_srv_record_set(terrascript.Resource):
    pass


class dns_txt_record_set(terrascript.Resource):
    pass


__all__ = [
    "dns_a_record_set",
    "dns_aaaa_record_set",
    "dns_cname_record",
    "dns_mx_record_set",
    "dns_ns_record_set",
    "dns_ptr_record",
    "dns_srv_record_set",
    "dns_txt_record_set",
]
