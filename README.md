# Nothing Phone (2) stock camera

Extraction and integration files for the NothingOS camera on AOSP.

Clone this repo to `device/nothing/Pong-camera`, then extract from NothingOS dump:

```sh
cd device/nothing/Pong-camera
./extract-files.py /path/to/Pong_dump
```

The extractor writes the proprietary payload and generated build files to
`vendor/nothing/Pong-camera`.

Inherit the source-side product configuration from the Pong device makefile:

```make
$(call inherit-product-if-exists, device/nothing/Pong-camera/nothing-camera.mk)
```
