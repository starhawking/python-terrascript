IMAGE_FAMILY = "debian-9"
MACHINE_TYPE = "n1-standard-1"

import terrascript
import terrascript.provider
import terrascript.resource
import terrascript.data

config = terrascript.Terrascript()

    # Google Cloud Compute provider
config += terrascript.provider.google(credentials='${file("account.json")}',
                                      project='myproject', region='us-central1')

# Google Compute Image (Debian 9) data source
image = terrascript.data.google_compute_image("image", family=IMAGE_FAMILY)
config += image

# Add Google Compute Instance resource
config += terrascript.resource.google_compute_instance("myinstance",
                                                       name="myinstance",
                                                       machine_type=MACHINE_TYPE,
                                                       zone="us-central1-a",
                                                       boot_disk={
                                                            "initialize_params": {
                                                                "image": image.self_link
                                                            }    
                                                       },
                                                       network_interface={
                                                           "network": "default",
                                                           "access_config": {}
                                                       })
