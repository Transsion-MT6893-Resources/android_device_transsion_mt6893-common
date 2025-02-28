#
# Copyright (C) 2025 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Properties
TARGET_SYSTEM_PROP += $(COMMON_PATH)/configs/properties/system.prop
TARGET_VENDOR_PROP += $(COMMON_PATH)/configs/properties/vendor.prop

# Inherit the proprietary files
include vendor/transsion/mt6893-common/BoardConfigVendor.mk
