[app]
title = Skin Scanner AI
package.name = skinscanner
package.domain = org.ai.skin
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
