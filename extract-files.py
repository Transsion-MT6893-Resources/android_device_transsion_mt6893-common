#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    ('vendor.mediatek.hardware.videotelephony@1.0',): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    'system_ext/lib64/libsink.so': blob_fixup()
        .add_needed('libaudioclient_shim.so'),
    'system_ext/lib64/libsource.so': blob_fixup()
        .add_needed('libui_shim.so'),
    'vendor/bin/factory': blob_fixup()
        .replace_needed('android.hardware.light-V1-ndk_platform.so', 'android.hardware.light-V1-ndk.so'),
    ('vendor/bin/hw/android.hardware.gnss-service.mediatek', 'vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so'): blob_fixup()
        .replace_needed('android.hardware.gnss-V1-ndk_platform.so', 'android.hardware.gnss-V1-ndk.so'),
    ('vendor/bin/hw/android.hardware.media.c2@1.2-mediatek', 'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b'): blob_fixup()
        .add_needed('libstagefright_foundation-v33.so')
        .replace_needed('libavservices_minijail_vendor.so', 'libavservices_minijail.so'),
    'vendor/bin/hw/vendor.mediatek.hardware.mtkpower@1.0-service': blob_fixup()
        .replace_needed('android.hardware.power-V2-ndk_platform.so', 'android.hardware.power-V2-ndk.so'),
    (
        'vendor/bin/mnld',
        'vendor/lib/libaalservice.so',
        'vendor/lib/librgbwlightsensor.so',
        'vendor/lib64/libaalservice.so',
        'vendor/lib64/librgbwlightsensor.so',
    ): blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so'),
    ('vendor/lib/hw/vendor.mediatek.hardware.pq@2.15-impl.so', 'vendor/lib64/hw/vendor.mediatek.hardware.pq@2.15-impl.so'): blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so')
        .replace_needed('libutils.so', 'libutils-v32.so'),
    (
        'vendor/lib/hw/awinic.audio.effect.so',
        'vendor/lib/hw/gatekeeper.default.so',
        'vendor/lib/hw/gatekeeper.trustonic.so',
        'vendor/lib/hw/kmsetkey.default.so',
        'vendor/lib/libnir_neon_driver_ndk.mtk.vndk.so',
        'vendor/lib/libspeech_enh_lib.so',
        'vendor/lib64/hw/gatekeeper.default.so',
        'vendor/lib64/hw/gatekeeper.trustonic.so',
        'vendor/lib64/hw/gf_fingerprint.default.so',
        'vendor/lib64/hw/kmsetkey.default.so',
        'vendor/lib64/libnir_neon_driver_ndk.mtk.vndk.so',
        'vendor/lib64/libspeech_enh_lib.so',
        'vendor/lib64/libwifi-hal-mtk.so'
    ): blob_fixup()
        .patchelf_version('0_17_2')
        .fix_soname(),
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
    'vendor/lib64/libmnl.so': blob_fixup()
        .add_needed('libcutils.so'),
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
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
