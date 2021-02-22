# terrascript/data/vault.py
import terrascript


class vault_approle_auth_backend_role_id(terrascript.Data):
    pass


class vault_auth_backend(terrascript.Data):
    pass


class vault_aws_access_credentials(terrascript.Data):
    pass


class vault_azure_access_credentials(terrascript.Data):
    pass


class vault_generic_secret(terrascript.Data):
    pass


class vault_identity_entity(terrascript.Data):
    pass


class vault_identity_group(terrascript.Data):
    pass


class vault_kubernetes_auth_backend_config(terrascript.Data):
    pass


class vault_kubernetes_auth_backend_role(terrascript.Data):
    pass


class vault_policy_document(terrascript.Data):
    pass


__all__ = [
    "vault_approle_auth_backend_role_id",
    "vault_auth_backend",
    "vault_aws_access_credentials",
    "vault_azure_access_credentials",
    "vault_generic_secret",
    "vault_identity_entity",
    "vault_identity_group",
    "vault_kubernetes_auth_backend_config",
    "vault_kubernetes_auth_backend_role",
    "vault_policy_document",
]
