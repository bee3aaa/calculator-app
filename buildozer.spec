# This .spec config file tells Buildozer an app's requirements for being built.
#
# It largely follows the syntax of an .ini file.
# See the end of the file for more details and warnings about common mistakes.

[app]

# (str) Title of your application
title = Calculator

# (str) Package name
package.name = calculator

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (leave empty to include all the files)
source.include_exts = py

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (leave empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (leave empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
# Do not prefix with './'
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse, landscape-reverse, or all
orientation = portrait

# (list) List of services to declare
# This is currently only relevant to Android services.
# Each service consists of a name (a valid Java class name, with the first letter capitalized)
# followed by a colon, followed by the name of the Python script (.py file) that should be
# launched. This is optionally followed by ":foreground" for foreground service. The default is a background service.
# Bound services are not supported.
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

# Kivy version to use
osx.kivy_version = 2.2.0

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color
#android.presplash_color = #FFFFFF

# (string) Presplash animation using Lottie format.
#android.presplash_lottie = "path/to/lottie/file.json"

# (str) Adaptive icon of the application
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Permissions
#android.permissions = android.permission.INTERNET

# (list) features
#android.features = android.hardware.usb.host

# (int) Target Android API
#android.api = 33

# (int) Minimum API
#android.minapi = 24

# (int) Android SDK version
#android.sdk = 20

# (str) Android NDK version
#android.ndk = 23b

# (int) Android NDK API
#android.ndk_api = 21

# (str) Android NDK directory
#android.ndk_path =

# (str) Android SDK directory
#android.sdk_path =

# (str) ANT directory
#android.ant_path =

# (bool) If True, then skip trying to update the Android SDK
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only.
android.accept_sdk_license = True

# (str) Android entry point
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of Java Activity class
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) Extra manifest XML
#android.extra_manifest_xml = ./src/android/extra_manifest.xml

# (str) Extra application manifest XML
#android.extra_manifest_application_arguments = ./src/android/extra_manifest_application_arguments.xml

# (str) Python service class
#android.service_class_name = org.kivy.android.PythonService

# (str) Android app theme
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist
#android.whitelist =

# (bool) Home app
# android.home_app = False

# (str) Whitelist file
#android.whitelist_src =

# (str) Blacklist file
#android.blacklist_src =

# (list) Java JAR files
#android.add_jars =

# (list) Java source files
#android.add_src =

# (list) Android AAR archives
#android.add_aars =

# (list) APK assets
#android.add_assets =

# (list) APK resources
#android.add_resources =

# (list) Gradle dependencies
#android.gradle_dependencies =

# (bool) AndroidX
#android.enable_androidx = True

# (list) Java compile options
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Gradle repositories
#android.add_gradle_repositories =

# (list) Packaging options
#android.add_packaging_options =

# (list) Java activities
#android.add_activities =

# (str) OUYA category
#android.ouya.category = GAME

# (str) OUYA icon
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) Intent filters
#android.manifest.intent_filters =

# (list) XML resources
#android.res_xml = PATH_TO_FILE,

# (str) Launch mode
#android.manifest.launch_mode = standard

# (str) Screen orientation
#android.manifest.orientation = fullSensor

# (list) Android additional libraries
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so

# (bool) Keep screen on
#android.wakelock = False

# (list) Android metadata
#android.meta_data =

# (list) Android library project
#android.library_references =

# (list) Android shared libraries
#android.uses_library =

# (str) Android logcat filters
#android.logcat_filters = *:S python:D

# (bool) Android logcat PID
#android.logcat_pid_only = False

# (str) Android additional ADB arguments
#android.adb_args = -H host.docker.internal

# (bool) Copy libraries
#android.copy_libs = 1

# (list) Android architectures
android.archs = arm64-v8a, armeabi-v7a

# (int) Android numeric version
# android.numeric_version = 1

# (bool) Android auto backup
android.allow_backup = True

# (str) Android backup rules
# android.backup_rules =

# (str) Manifest placeholders
# android.manifest_placeholders = [:]

# (bool) Skip byte compile
# android.no-byte-compile-python = False

# (str) Release artifact
# android.release_artifact = aab

# (str) Debug artifact
# android.debug_artifact = apk


#
# Python for android (p4a) specific
#

#p4a.url =
#p4a.fork = kivy
#p4a.branch = master
#p4a.commit = HEAD
#p4a.source_dir =
#p4a.local_recipes =
#p4a.hook =
# p4a.bootstrap = sdl2
#p4a.port =
#p4a.setup_py = false
#p4a.extra_args =


#
# iOS specific
#

#ios.kivy_ios_dir = ../kivy-ios
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

#ios.ios_deploy_dir = ../ios_deploy
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.12.2

# (bool) Whether or not to sign the code
ios.codesign.allowed = false


[buildozer]

# (int) Log level
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1

# build_dir = ./.buildozer
# bin_dir = ./bin
