# terrascript/resource/docker.py
import terrascript


class docker_container(terrascript.Resource):
    pass


class docker_image(terrascript.Resource):
    pass


class docker_network(terrascript.Resource):
    pass


class docker_volume(terrascript.Resource):
    pass


class docker_config(terrascript.Resource):
    pass


class docker_secret(terrascript.Resource):
    pass


class docker_service(terrascript.Resource):
    pass


__all__ = [
    "docker_container",
    "docker_image",
    "docker_network",
    "docker_volume",
    "docker_config",
    "docker_secret",
    "docker_service",
]
