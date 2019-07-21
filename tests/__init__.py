
import tempfile
import subprocess


TMPDIR = None
"""Temporary directory that is shared in a test run for efficiency."""

OUTPUT = None
"""Stores output of most recent 'terraform ...' command for debugging."""


def setup():
    """Create a temporary directory for testing Terraform configurations."""
    
    global TMPDIR
    TMPDIR = tempfile.TemporaryDirectory()
    
def teardown():
    TMPDIR.cleanup()
    
def validate(config):
    """Validate a Terraform configuration."""
    
    global OUTPUT
    
    with tempfile.NamedTemporaryFile(mode='w', dir=TMPDIR.name, suffix='.tf.json') as tmpfile:

        tmpfile.write(str(config))
        tmpfile.flush()

        # Download plugins
        proc = subprocess.Popen(['terraform', 'init'], 
                                cwd=TMPDIR.name,
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.STDOUT)
        OUTPUT, _ = proc.communicate()
        assert proc.returncode == 0

        # Validate configuration
        proc = subprocess.Popen(['terraform',
                                 'validate'],
                                cwd=TMPDIR.name,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        OUTPUT, _ = proc.communicate()

    return proc.returncode == 0