# terrascript/data/dme.py
import terrascript


class dme_custom_soa_record(terrascript.Data):
    pass


class dme_domain(terrascript.Data):
    pass


class dme_dns_record(terrascript.Data):
    pass


class dme_template(terrascript.Data):
    pass


class dme_vanity_nameserver_record(terrascript.Data):
    pass


class dme_transfer_acl(terrascript.Data):
    pass


class dme_secondary_dns(terrascript.Data):
    pass


class dme_secondary_ip_set(terrascript.Data):
    pass


class dme_failover(terrascript.Data):
    pass


class dme_folder_record(terrascript.Data):
    pass


class dme_template_record(terrascript.Data):
    pass


class dme_contact_list(terrascript.Data):
    pass


__all__ = [
    "dme_custom_soa_record",
    "dme_domain",
    "dme_dns_record",
    "dme_template",
    "dme_vanity_nameserver_record",
    "dme_transfer_acl",
    "dme_secondary_dns",
    "dme_secondary_ip_set",
    "dme_failover",
    "dme_folder_record",
    "dme_template_record",
    "dme_contact_list",
]
