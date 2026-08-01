[app]
title = SRP App Builder
package.name = srpappbuilder
package.domain = org.novaclaw.srp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,requests,sqlite3

orientation = portrait
fullscreen = 0
monolithic = 0

# Android permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Android API level
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 31

# Buildozer options
android.archs = arm64-v8a
