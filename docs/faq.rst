Frequently Asked Questions
--------------------------

Questions I frequently asked myself ;-)

Why no error checking?
~~~~~~~~~~~~~~~~~~~~~~

**Python-Terrascript** does not perform any error checking whatsoever! This was a deliberate design decision to keep 
the code simple. Therefore it is perfectly possible to generate JSON output that Terraform will later reject.

.. literalinclude:: examples/faq_no_error_checking.tf.json

.. code-block:: python
    import terrascript
    import terrascript.provider
    import terrascript.resource

    config = terrascript.Terrascript()
    
    i = terrascript.resource.aws_instance('myinstance', foo='bar')
    config += i
    
    # AWS Instance resource does not have a `foo` but accepts it anyway.
    assert i.foor == 'bar'

.. literalinclude:: examples/faq_no_error_checking.tf.json

Terraform will reject the generated JSON as the `aws_instance` resource does not accept the `foo` argument.

At an early stage I contemplated parsing the Terraform Go source code and auto-create Python
code that does indeed verify whether the generated JSON configuration is valid Terraform input. This attempt
proved much too difficult so I abandonded that approach.
