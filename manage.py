#!/usr/bin/env python
"""Django's command-line utility for administrative tasks.

For LIVE or UAT deployments, set DJANGO_SETTINGS_MODULE in the shell environment.

For example, in .bashrc, add

    # >>> EDC >>>
    conda deactivate
    export DJANGO_SETTINGS_MODULE=mapitio_edc.settings.live
    conda activate edc
    # <<< EDC <<<

"""
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mapitio_edc.settings.debug")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
