from plugin_api import PluginAPI


def register(api: PluginAPI):
    """
    Example legacy plugin using PluginAPI.
    Demonstrates how older plugins still work
    under the new unified plugin architecture.
    """

    def hello_command(*args):
        name = " ".join(args) if args else "there"
        return f"Hello, {name}!"

    api.register_command("hello", hello_command)
