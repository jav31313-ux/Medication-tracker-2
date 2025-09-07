[app]

# (str) Title of your application
title = Tracker de Medicamentos

# (str) Package name
package.name = medicamentostracker

# (str) Package domain (needed for android/ios packaging)
package.domain = com.juanita.medicamentos

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy,plyer

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK / AAB will support
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (int) Android SDK version
android.sdk = 33

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,VIBRATE

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature
android.allow_backup = True

# (str) XML file for custom backup rules
# android.backup_rules =

# (str) If you need to insert variables into your AndroidManifest.xml file
# android.manifest_placeholders = [:]

# (list) Java classes to add as activities to the manifest
# android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category
# android.ouya.category = GAME

# (str) Filename of OUYA Console icon
# android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
# android.manifest.intent_filters =

# (str) launchMode to set for the main activity
# android.manifest.launch_mode = standard

# (list) Android additional libraries to copy into libs/armeabi
# android.add_libs_armeabi = libs/android/*.so
# android.add_libs_armeabi_v7a = libs/android-v7/*.so
# android.add_libs_arm64_v8a = libs/android-v8/*.so
# android.add_libs_x86 = libs/android-x86/*.so
# android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on
# android.wakelock = False

# (list) Android application meta-data to set (key=value format)
# android.meta_data =

# (list) Android library project to add
# android.library_references = @jar/foo.jar:@jar/bar.jar

# (list) Android shared libraries
# android.uses_library =

# (str) Android logcat filters to use
# android.logcat_filters = *:S python:D

# (bool) Android logcat only display log for tags specified in filters
# android.logcat_pid_only = False

# (str) Android additional adb arguments
# android.adb_args = -H host.docker.internal

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1

# (int) overrides automatic versionCode computation
# android.numeric_version = 1

# (bool) If True, then skip trying to update the Android sdk
# android.skip_update = False

# (bool) Automatically accept SDK license agreements
android.accept_sdk_license = True

# (str) The Android arch to build for
# android.arch = arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1

# (str) Path to build artifact storage
# build_dir = ./.buildozer

# (str) Path to build output
# bin_dir = ./bin

# ---------------------------------------------------------------------------
# Profiles
#
#[app@demo]
#title = My Application (demo)
#[app:source.exclude_patterns@demo]
#images/hd/*
