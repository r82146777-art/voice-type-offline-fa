# Verified recovery notes for the supplied APK

## Verified facts
- APK package: `com.plus9.shahrbanoo`, version 5.80 (versionCode 90).
- The APK includes Sherpa-ONNX / ONNX Runtime native libraries and offline ASR assets.
- It also includes Unity/IL2CPP payloads (`global-metadata.dat`, `data.unity3d`, resource bundles).
- The APK does not appear to be the older Vosk-based Gradle project.
- Decompiled Java/Smali alone is not the full source for Unity/IL2CPP app logic.

## Why a safe patch cannot be claimed yet
The existing workflow assumed app-specific classes named `ir/offline/voicetype/AsrEngine.smali` and `VoiceImeService.smali`. Those names are not supported by the verified inventory and are likely from a different project. Do not patch guessed class names or label an unchanged repackage as the modified app.

## Correct next technical steps
1. Decode the exact original APK and preserve its hash.
2. Inventory the manifest, DEX classes, native libraries, ASR/TTS assets, Unity metadata and bundles.
3. Determine whether the speech/keyboard logic is implemented in DEX, Unity managed assemblies, or IL2CPP native code.
4. Only patch the verified implementation; if the relevant logic is IL2CPP-native and symbols/source are unavailable, document the limitation rather than inventing source.
5. Rebuild, sign with a new key, verify APK signature and package metadata, and publish only after a successful build.

## Requested features (not yet implemented)
- Prevent duplicate text insertion and TalkBack audio echo.
- Improve Persian/English offline recognition and noise handling.
- Keyboard switching.
- Bundled natural-sounding offline Persian and English TTS.
- Read pasted text and PDF content aloud with TalkBack-accessible controls.

A successful decode or repackage is not proof that any of these features work.