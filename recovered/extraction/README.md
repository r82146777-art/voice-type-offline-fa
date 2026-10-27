# Verified extraction from the supplied APK

The original APK is a Java/Kotlin Android package containing `classes.dex`, a binary `AndroidManifest.xml`, Kotlin runtime metadata, ONNX Runtime and sherpa-onnx JNI libraries, Persian and English dictionaries, and compressed ASR/VAD models. The presence of native `.so` libraries does **not** establish that the app is a Unity project.

## Important limitation

This directory contains inventory and DEX string recovery, not a complete decompiled Java/Kotlin source tree. Extracting the ZIP container is not the same as decompiling DEX. The original APK must be passed to a DEX decompiler such as JADX to recover readable Java/Kotlin-like code. Rebuilding requires the recovered source plus resources, Gradle configuration, dependencies, and any required model assets. No modified APK should be claimed until a build and install/package checks pass.

## Confirmed from the APK

- `classes.dex` (~1.35 MB)
- `libonnxruntime.so` and `libsherpa-onnx-jni.so` for arm64-v8a and armeabi-v7a
- `assets/dict/fa.tsv.gz`, `assets/dict/en.tsv.gz`, and `assets/dict/fa2en.txt`
- `assets/asr/model.int8v2.onnx.xz` and `assets/asr/silero_vad.onnx.xz`
- English ASR model files under `assets/asr/en/`

This is a verified inventory and recovery note, not a replacement APK.