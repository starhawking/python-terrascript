== tests/configs ==

This folder contains Terraform configurations or fragments in JSON format.
They are used to verify the configurations generated in the test modules
against an expected outcome.

Files ending in ``.tf.json`` are complete Terraform configurations whereas files
ending just in ``.json`` are only incomplete fragments.

Running ``test_configs.sh`` will execute ``terraform init`` and ``terraform validate``
against all complete configurations ending in ``.tf.json``.