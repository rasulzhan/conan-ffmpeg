#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
from conans import tools
from bincrafters import build_template_default


def disable_opus(build):
    build.options.update({'ffmpeg:opus': False})
    return build


if __name__ == "__main__":

    builder = build_template_default.get_builder()

    if 'CONAN_VISUAL_VERSIONS' in os.environ:
        if os.environ['CONAN_VISUAL_VERSIONS'] == '12':

            builder.builds = map(disable_opus, builder.items)

    builder.run()
