import cowsay

import platform


def modern_print(data: dict[str, ...]) -> None:
    system_info = data.get('system')

    system_release = data.get('release')

    system_version = data.get('version')

    system_node = data.get('node')

    system_processor = data.get('processor')

    template_message: str = """

    Hello, Stranger!



    Here's your info you requested:

    SYSTEM INFO: {}

    SYSTEM RELEASE: {}

    SYSTEM VERSION: {}

    SYSTEM NODE: {}

    SYSTEM PROCESSOR: {}

    """

    cowsay.beavis(template_message.format(

        system_info,

        system_release,

        system_version,

        system_node,

        system_processor

    ))


request_data: dict[str, ...] = {

    "system": platform.system(),

    "release": platform.release(),

    "version": platform.version(),

    "node": platform.node(),

    "processor": platform.processor(),

}

if __name__ == "__main__":
    modern_print(request_data)