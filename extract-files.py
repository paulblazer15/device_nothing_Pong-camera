#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2026 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import blob_fixup, blob_fixups_user_type
from extract_utils.fixups_lib import lib_fixups
from extract_utils.main import ExtractUtils, ExtractUtilsModule


blob_fixups: blob_fixups_user_type = {
    'system_ext/lib64/libofflineproc_jni.so': blob_fixup()
        .add_needed('libofflineproc_shim.so'),
    'vendor/etc/init/vendor.noth.hardware.camera-service.rc': blob_fixup()
        .regex_replace(r'\bNtCamAlgoCapacity\b', 'CameraServiceCapacity'),
    'vendor/lib64/vendor.noth.hardware.camera-service-impl.so': blob_fixup()
        .add_needed('libui_shim.so'),
}  # fmt: skip


module = ExtractUtilsModule(
    'Pong-camera',
    'nothing',
    device_rel_path='device/nothing/Pong-camera',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=[
        'device/nothing/Pong-camera',
        'vendor/nothing/Pong',
    ],
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
