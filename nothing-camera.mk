#
# Copyright (C) 2026 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    device/nothing/Pong-camera

# Shim
PRODUCT_PACKAGES += \
    libofflineproc_shim

# Properties
PRODUCT_SYSTEM_EXT_PROPERTIES += \
    persist.vendor.camera.privapp.list=com.nothing.camera \
    ro.com.google.lens.oem_camera_package=com.nothing.camera \
    vendor.camera.aux.packagelist=com.nothing.camera

# SEPolicy
include device/nothing/Pong-camera/sepolicy/SEPolicy.mk

# Inherit from camera-vendor.mk
$(call inherit-product-if-exists, vendor/nothing/Pong-camera/Pong-camera-vendor.mk)
