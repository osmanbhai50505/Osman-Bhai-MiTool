# Changelog

## 1.6.0
- Converger to a CLI tool
- Improvements and performance optimization
- Now supporting all operating systems instead of Termux only
- Added `miapply` module

## 1.5.9
- Improvements and minor fixes

## 1.5.7
- MiTools App Launched!: github.com/offici5l/MiTools

💡 **Note:** If you are facing issues recognizing your device through ADB & Fastboot commands, use Termux or Termux Monet:
- **Termux:** [Download APK](https://www.mediafire.com/file/88p4ekllryzd3ml/Termux.apk/file)
- **Termux API:** [Download APK](https://www.mediafire.com/file/8lh4qsrxsnk5l9m/Termux.api.apk/file)
- **Termux Monet:** github.com/Termux-Monet/termux-monet/releases
- **Termux API Monet:** github.com/Termux-Monet/termux-api/releases

### MiTool version 1.5.7:
- Previously, you could only flash the same version. Now, with MiAssistantTool V1.2, you can flash other suggested versions using the option:
  `Mi-Assistant => 2 => ROMs that can be flashed`
- Added **Firmware-Content-Extractor**: A new option (6) that **gets file.img** from a ROM without downloading the full ROM!
- Minor fixes and improvements

## 1.5.6
- Minor fixes and improvements

## 1.5.5
- Improvements
- Added `pycryptodomex-3.21` to solve the issue of conflict between `pycryptodomex-3.20` and `python3.12`

### MiUnlockTool-1.5.6:
- Removed manual mode and unnecessary functions.
- Fixed the issue with Termux (`fastboot: error: cannot load /sdcard/encryptData`). `encryptData` is now saved in `$PREFIX/bin`.
- Improvements in the installation process for Termux.

## 1.5.4
- Improvements

## 1.5.3
- Fixed installation for `termux-adb`
- Fixed `flashf` issue ("termux-api popup appears! But the flashing process does not start")

### MiUnlockTool version 1.5.2:
- Fixed `"device is not recognized but termux-api popup appears!"`
- Improvements

### MiAssistantTool version 1.1:
- Reboot (to system)
- Display the list of options before connecting the device
- Many fixes and improvements

- Added a step to verify storage access (`termux-setup-storage`)

### MiUnlockTool version 1.5.3:
- Added global variable `connect` to track connection status, reducing redundant checks and cutting process time by half.

### MiUnlockTool version 1.5.4:
- Changed `encryptData` save path to `/sdcard/encryptData` instead of `/sdcard/Download/encryptData`.

## 1.5.2
- Added MiAssistantTool for `arm` & `aarch64` architectures.

## 1.5.1
- Added MiAssistantTool version 1.0 (Recovery mode > Mi Assistant without unlocking bootloader):
  - Read-Info
  - Check-ROM-Compatibility (With MD5)
  - Flash-Official-Recovery-ROM
  - Format-Data with Mi Assistant

## 1.5.0
- MiTool now directly utilizes MiUnlockTool for bootloader unlocking.
- MiTool now directly utilizes MiBypassTool for bypassing.
- Converted MiTool from `mitool.sh` to `mitool.py`.
- Removed unnecessary features and optimized code.

## 1.4.9
- Improved handling to prevent `securityStatus16` error.
- Other general improvements.

## 1.4.8
- Added Bypass HyperOS BootLoader Restrictions.
- Fixed bypass message `"Couldn't verify, wait a minute or two and try again"` for MIUI and HyperOS.

## 1.4.6
- Improved `Flash-Fastboot-ROM` and `Fastboot-Flash-Rom-V2`.

## 1.4.5
- Improved bootloader unlock flow (browser login confirmation).
- Added in-app support/suggestion tool (`m` command).

## 1.4.4
- Added automatic device verification and mode switching.
- Added trial version for Flashing Fastboot ROM v2 (`mitool t`).
- Improved error handling for unlock errors (e.g., error code 10000).
- Removed manual region selection requirement during unlock.
