# terrascript/vault/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class vault_alicloud_auth_backend_role(terrascript.Resource):
    pass


class vault_approle_auth_backend_login(terrascript.Resource):
    pass


class vault_approle_auth_backend_role(terrascript.Resource):
    pass


class vault_approle_auth_backend_role_secret_id(terrascript.Resource):
    pass


class vault_audit(terrascript.Resource):
    pass


class vault_auth_backend(terrascript.Resource):
    pass


class vault_aws_auth_backend_cert(terrascript.Resource):
    pass


class vault_aws_auth_backend_client(terrascript.Resource):
    pass


class vault_aws_auth_backend_identity_whitelist(terrascript.Resource):
    pass


class vault_aws_auth_backend_login(terrascript.Resource):
    pass


class vault_aws_auth_backend_role(terrascript.Resource):
    pass


class vault_aws_auth_backend_role_tag(terrascript.Resource):
    pass


class vault_aws_auth_backend_roletag_blacklist(terrascript.Resource):
    pass


class vault_aws_auth_backend_sts_role(terrascript.Resource):
    pass


class vault_aws_secret_backend(terrascript.Resource):
    pass


class vault_aws_secret_backend_role(terrascript.Resource):
    pass


class vault_azure_auth_backend_config(terrascript.Resource):
    pass


class vault_azure_auth_backend_role(terrascript.Resource):
    pass


class vault_azure_secret_backend(terrascript.Resource):
    pass


class vault_azure_secret_backend_role(terrascript.Resource):
    pass


class vault_cert_auth_backend_role(terrascript.Resource):
    pass


class vault_consul_secret_backend(terrascript.Resource):
    pass


class vault_consul_secret_backend_role(terrascript.Resource):
    pass


class vault_database_secret_backend_connection(terrascript.Resource):
    pass


class vault_database_secret_backend_role(terrascript.Resource):
    pass


class vault_database_secret_backend_static_role(terrascript.Resource):
    pass


class vault_egp_policy(terrascript.Resource):
    pass


class vault_gcp_auth_backend(terrascript.Resource):
    pass


class vault_gcp_auth_backend_role(terrascript.Resource):
    pass


class vault_gcp_secret_backend(terrascript.Resource):
    pass


class vault_gcp_secret_roleset(terrascript.Resource):
    pass


class vault_generic_endpoint(terrascript.Resource):
    pass


class vault_generic_secret(terrascript.Resource):
    pass


class vault_github_auth_backend(terrascript.Resource):
    pass


class vault_github_team(terrascript.Resource):
    pass


class vault_github_user(terrascript.Resource):
    pass


class vault_identity_entity(terrascript.Resource):
    pass


class vault_identity_entity_alias(terrascript.Resource):
    pass


class vault_identity_entity_policies(terrascript.Resource):
    pass


class vault_identity_group(terrascript.Resource):
    pass


class vault_identity_group_alias(terrascript.Resource):
    pass


class vault_identity_group_policies(terrascript.Resource):
    pass


class vault_identity_oidc(terrascript.Resource):
    pass


class vault_identity_oidc_key(terrascript.Resource):
    pass


class vault_identity_oidc_key_allowed_client_id(terrascript.Resource):
    pass


class vault_identity_oidc_role(terrascript.Resource):
    pass


class vault_jwt_auth_backend(terrascript.Resource):
    pass


class vault_jwt_auth_backend_role(terrascript.Resource):
    pass


class vault_kubernetes_auth_backend_config(terrascript.Resource):
    pass


class vault_kubernetes_auth_backend_role(terrascript.Resource):
    pass


class vault_ldap_auth_backend(terrascript.Resource):
    pass


class vault_ldap_auth_backend_group(terrascript.Resource):
    pass


class vault_ldap_auth_backend_user(terrascript.Resource):
    pass


class vault_mfa_duo(terrascript.Resource):
    pass


class vault_mount(terrascript.Resource):
    pass


class vault_namespace(terrascript.Resource):
    pass


class vault_okta_auth_backend(terrascript.Resource):
    pass


class vault_okta_auth_backend_group(terrascript.Resource):
    pass


class vault_okta_auth_backend_user(terrascript.Resource):
    pass


class vault_pki_secret_backend(terrascript.Resource):
    pass


class vault_pki_secret_backend_cert(terrascript.Resource):
    pass


class vault_pki_secret_backend_config_ca(terrascript.Resource):
    pass


class vault_pki_secret_backend_config_urls(terrascript.Resource):
    pass


class vault_pki_secret_backend_crl_config(terrascript.Resource):
    pass


class vault_pki_secret_backend_intermediate_cert_request(terrascript.Resource):
    pass


class vault_pki_secret_backend_intermediate_set_signed(terrascript.Resource):
    pass


class vault_pki_secret_backend_role(terrascript.Resource):
    pass


class vault_pki_secret_backend_root_cert(terrascript.Resource):
    pass


class vault_pki_secret_backend_root_sign_intermediate(terrascript.Resource):
    pass


class vault_pki_secret_backend_sign(terrascript.Resource):
    pass


class vault_policy(terrascript.Resource):
    pass


class vault_rabbitmq_secret_backend(terrascript.Resource):
    pass


class vault_rabbitmq_secret_backend_role(terrascript.Resource):
    pass


class vault_rgp_policy(terrascript.Resource):
    pass


class vault_ssh_secret_backend_ca(terrascript.Resource):
    pass


class vault_ssh_secret_backend_role(terrascript.Resource):
    pass


class vault_token(terrascript.Resource):
    pass


class vault_token_auth_backend_role(terrascript.Resource):
    pass


class vault_transit_secret_backend_key(terrascript.Resource):
    pass


class vault_transit_secret_cache_config(terrascript.Resource):
    pass
