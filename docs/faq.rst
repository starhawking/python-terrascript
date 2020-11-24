Frequently Asked Questions
--------------------------

Questions I frequently asked myself ;-)

Why no error checking?
~~~~~~~~~~~~~~~~~~~~~~

**Python-Terrascript** does not perform any error checking whatsoever! This was a deliberate design decision to keep 
the code simple. Therefore it is perfectly possible to generate JSON output that Terraform will later reject.

.. code-block:: python

    import terrascript
    import terrascript.provider
    import terrascript.resource

    config = terrascript.Terrascript()

    config += terrascript.provider.aws(region='us-east-1')
        
    i = terrascript.resource.aws_instance('myinstance', foo='bar')
    config += i
        
    # AWS Instance resource does not have a `foo` argument but accepts it anyway.
    assert i.foo == 'bar'

.. code-block:: json
   :emphasize-lines: 12

    {
    "provider": {
        "aws": [
        {
            "region": "us-east-1"
        }
        ]
    },
    "resource": {
        "aws_instance": {
          "myinstance": {
              "foo": "bar"
          }
        }
    }


Terraform will reject the generated JSON as the `aws_instance` resource does not accept the `foo` argument.

.. code-block::

    on faq_no_error_checking.tf.json line 12, in resource.aws_instance.myinstance:
    12:         "foo": "bar"

    No argument or block type is named "foo".

At an early stage I contemplated parsing the Terraform Go source code and auto-create Python
code that does indeed verify whether the generated JSON configuration is valid Terraform input. This attempt
proved much too difficult so I abandonded that approach.

Why is provider XYZ not supported?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All provider specific code is auto-generated through the ``tools/makecode.py`` script
based on the list of providers in ``tools/providers.yml``. So if a provider is missing
it simply has not yet been added to ``tools/providers.yml``. 

If you believe a provider is missing simply open a new issue_ or submit a pull
request with the missing provider added to ``tools/providers.yml``.

.. _issue: https://github.com/mjuenema/python-terrascript/issues

Why is there sometimes so little progress in this project? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Python-Terrascript** is a hobby project which I can only work on in my very 
limited spare time. 

Professionally I am a Systems and Network Engineer working on an Intelligent Transport
Systems project. None of its infrastructure is in the Cloud, it's all very physcially
located on the freeways around Melbourne, Australia. Until someone writes Terraform
modules for traffic cameras or vehicle sensors my manager simply wouldn't appreciate 
if I spent time on **Python-Terrascript** during work hours.

Is Python-Terrascript better than writing configurations by hand?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I regard **Python-Terrascript** as an *alternative* to writing Terraform 
configurations by hand. Whether it is better or not is for everyone to
decide for themselves.

How can I contribute to the project?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There a various ways you can contribute to the development of **Python-Terrascript**.

* Issues: Do not hestiate to raise an issue_ if you believe you found a bug or simply have a question.
  As the maintainer of a small Github project it is amazingly satisfying to see that there are 
  other people out there who find **Python-Terrascript** useful. Do not get discouraged if I 
  don't respond immediately. As mentioned earlier I can only spend limited time on 
  **Python-Terrascript**. You will hear from me eventually.
* Pull Requests: Yes, `Pull Requests` are welcome but please bear in my that this is a 
  *personal* project and not a community project. I promise to provide an explanation if
  should I reject a Pull Request.
* Documentation: Documentation can always be improved so any support (Issues, Pull Requests) is
  very welcome. The biggest problem with documentation is always what may be obvious to me 
  may not be obvious to the reader at all. I also tend to be rather terse when writing 
  documentation which is not a good thing.
* Examples: I would like to include a collection of real-world examples of how **Python-Terrascript**
  is used. So if you are willing to share your code please come forward.
* Drinks: Anyone willing to catch-up for a chat over coffee (hot chocolate in my case) or beer
  when they are in Melbourne?
  
.. _`Pull Requests`: https://github.com/mjuenema/python-terrascript/pulls?q=is%3Apr+is%3Aclosed

Are there any alternatives to Python-Terrascript?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I know that there are comparable projects to **Python-Terrascript**. I just haven't managed
to compile a list yet. Please stand-by for updates... 