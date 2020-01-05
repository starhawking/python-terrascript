provider "google" {
    credentials = "${file("account.json")}"
    project     = "myproject"
    region      = "us-central1"
}

data "google_compute_image" "debian9" {
    family  = "debian-9"
    project = "debian-cloud"
}

resource "google_compute_instance" "myinstance" {
    name         = "test"
    machine_type = "n1-standard-1"
    zone         = "us-central1-a"
    boot_disk {
        initialize_params {
            image = data.google_compute_image.debian9.self_link
        }
    }
    network_interface {
        network = "default"
        access_config {
            // Ephemeral IP
        }
    }
}