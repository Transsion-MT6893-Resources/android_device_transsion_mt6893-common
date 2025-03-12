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
    'vendor/bin/factory': blob_fixup()
        .replace_needed('android.hardware.light-V1-ndk_platform.so', 'android.hardware.light-V1-ndk.so'),
    ('vendor/bin/hw/android.hardware.gnss-service.mediatek', 'vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so'): blob_fixup()
        .replace_needed('android.hardware.gnss-V1-ndk_platform.so', 'android.hardware.gnss-V1-ndk.so'),
    ('vendor/bin/hw/android.hardware.media.c2@1.2-mediatek', 'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b'): blob_fixup()
        .add_needed('libstagefright_foundation-v33.so')
        .replace_needed('libavservices_minijail_vendor.so', 'libavservices_minijail.so'),
    'vendor/bin/hw/vendor.mediatek.hardware.mtkpower@1.0-service': blob_fixup()
        .replace_needed('android.hardware.power-V2-ndk_platform.so', 'android.hardware.power-V2-ndk.so'),
    ('vendor/lib/hw/vendor.mediatek.hardware.pq@2.15-impl.so', 'vendor/lib64/hw/vendor.mediatek.hardware.pq@2.15-impl.so'): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),
    ('vendor/lib/libh264enc_sa.ca7.so', 'vendor/lib/libvp8dec_sa.ca7.so'): blob_fixup()
        .clear_symbol_version('__aeabi_memclr')
        .clear_symbol_version('__aeabi_memclr4')
        .clear_symbol_version('__aeabi_memcpy')
        .clear_symbol_version('__aeabi_memcpy4')
        .clear_symbol_version('__aeabi_memmove')
        .clear_symbol_version('__aeabi_memset')
        .clear_symbol_version('__gnu_Unwind_Find_exidx'),
    (
        'vendor/lib/libmp4enc_sa.ca7.so',
        'vendor/lib/libmp4enc_xa.ca7.so',
        'vendor/lib/libthha.so',
        'vendor/lib/libvcodec_oal.so',
        'vendor/lib/libvp9dec_sa.ca7.so'
    ): blob_fixup()
        .clear_symbol_version('__aeabi_memclr')
        .clear_symbol_version('__aeabi_memcpy')
        .clear_symbol_version('__aeabi_memset')
        .clear_symbol_version('__gnu_Unwind_Find_exidx'),
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
