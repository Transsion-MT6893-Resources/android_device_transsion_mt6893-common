#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

blob_fixups: blob_fixups_user_type = {
    ('vendor/lib/hw/vendor.mediatek.hardware.pq@2.15-impl.so', 'vendor/lib64/hw/vendor.mediatek.hardware.pq@2.15-impl.so'): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),
}   # fmt: skip

namespace_imports = [
    'device/transsion/mt6893-common',
    'hardware/mediatek',
    'hardware/transsion',
]

module = ExtractUtilsModule(
    'mt6893-common',
    'transsion',
    blob_fixups=blob_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
