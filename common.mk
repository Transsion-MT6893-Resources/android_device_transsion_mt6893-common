#
# Copyright (C) 2025 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

COMMON_PATH := device/transsion/mt6893-common

# Dynamic partitions
PRODUCT_USE_DYNAMIC_PARTITIONS := true

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH) \
    hardware/transsion

# Inherit the proprietary files
$(call inherit-product, vendor/transsion/mt6893-common/mt6893-common-vendor.mk)
