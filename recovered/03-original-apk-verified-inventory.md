# Verified inventory of the exact uploaded APK

Generated from `4_5949663322923081136.apk` in the current working session.

- Archive validation: passed (ZIP/APK structure, root `AndroidManifest.xml`, DEX present)
- APK size: 127,035,379 bytes
- SHA-256: `06ed8804e10ca832a3a15304f9f35399cfe4d28da9786933507eade3f6c74367`
- ZIP entries: 426
- App package observed in recovered BuildConfig: `com.plus9.shahrbanoo`
- Version observed in recovered BuildConfig: `5.80` (version code `90`)

## Actual ASR assets in the original APK

| Asset | Compressed size in APK | What it indicates |
|---|---:|---|
| `assets/asr/model.int8v2.onnx.xz` | 77,191,148 bytes | Main quantized ONNX speech model |
| `assets/asr/silero_vad.onnx.xz` | 379,440 bytes | Voice activity detection model |
| `assets/asr/tokens.txt` | 12,236 bytes | Main recognizer token vocabulary |
| `assets/asr/en/encoder_model.ort.xz` | 5,576,636 bytes | English recognizer encoder |
| `assets/asr/en/decoder_model_merged.ort.xz` | 21,982,884 bytes | English recognizer decoder |
| `assets/asr/en/tokens.txt.xz` | 166,832 bytes | English recognizer token vocabulary |

## Native runtime included

- `lib/arm64-v8a/libonnxruntime.so` — 22,249,560 bytes
- `lib/arm64-v8a/libsherpa-onnx-jni.so` — 4,771,760 bytes
- `lib/armeabi-v7a/libonnxruntime.so` — 15,359,592 bytes
- `lib/armeabi-v7a/libsherpa-onnx-jni.so` — 3,428,780 bytes

The original APK also contains `res/layout/keyboard.xml` (1,300 bytes). The earlier decompiled ZIP is incomplete: it omits this layout and the ASR model assets that are present in the original APK.

## Important implementation finding

The package contains Unity/IL2CPP-related assets, including `assets/bin/Data/Managed/Metadata/global-metadata.dat`, `assets/bin/Data/data.unity3d`, and Unity resource bundles. The recovered Java source is mostly framework/plugin glue, not the full app logic. A source-level fix to microphone/TalkBack interaction, recognition settings, or app UI cannot safely be claimed from the few recovered Java files alone. The next recovery step must inspect the original APK's Unity/IL2CPP payload and its actual model configuration.

## Reproducibility

Run:
```bash
python recovered/tools/apk_inventory.py path/to/original.apk --out apk-inventory
```

The script rejects a ZIP of decompiled sources when it lacks the APK manifest and DEX files. Do not feed `base_source.zip` to an APK build step.
