#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import re
from unmanic.libs.unplugins.settings import PluginSettings


class Settings(PluginSettings):
    settings = {}


def on_worker_process(data):
    """
    Runner function - enables additional configured processing jobs during the worker stages of a task.

    The 'data' object argument includes:
        exec_ffmpeg             - Boolean, should Unmanic run FFMPEG with the data returned from this plugin.
        file_probe              - A dictionary object containing the current file probe state.
        ffmpeg_args             - A list of Unmanic's default FFMPEG args.
        file_in                 - The source file to be processed by the FFMPEG command.
        file_out                - The destination that the FFMPEG command will output.
        original_file_path      - The absolute path to the original library file.

    :param data:
    :return:
    
    """
    new_file_path = data['original_file_path'] + '/frame%d.png'

    p = subprocess.run(['ffmpeg', '-i', data['original_file_path'], '-r', '30', new_file_path])
    
    return data

# data = { "original_file_path": "./file.mp4", "file_out": "./file_converted.mp4" }
# on_worker_process(data)   
