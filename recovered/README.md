# Recovered source from the user-supplied APK

These files are a first text-based transfer of files extracted from the supplied APK. They are not a complete Android Studio/Gradle project.

## Verified observations
- Original APK contains `AndroidManifest.xml`, `classes.dex`, native `libonnxruntime.so` and `libsherpa-onnx-jni.so` for ARM64 and ARMv7.
- Original APK contains offline ASR model assets: `assets/asr/model.int8v2.onnx.xz` and `assets/asr/silero_vad.onnx.xz`.
- The available extracted-source ZIP contains decompiled Java and smali plus resources, but it does **not** contain the ASR model assets listed above, and it is not a Gradle project.
- Decompiled app package observed in Java resources: `com.plus9.shahrbanoo`, version `5.80`, version code `90`.
- This repository must continue to use the supplied APK as the source of truth; do not silently replace it with an older Vosk project.

## Work remaining
1. Transfer the relevant app-specific smali/classes and decoded resource files.
2. Recover/verify the actual manifest and the code paths that call Sherpa-ONNX.
3. Apply the requested fixes (TalkBack echo prevention, recognition accuracy/noise handling, keyboard switching, clipboard read-aloud and offline TTS).
4. Rebuild, sign, and verify the APK before publishing a download link.

Files in this folder are intermediate recovered text, not a finished or tested build.