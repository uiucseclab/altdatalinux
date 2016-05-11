Alt Data Linux
===

This directory contains files to enable a Linux system to be embedded within an alternate data
stream on a Windows NTFS partition and to enable booting that system through the Windows Boot
Manager.

Files
---
 - grub-ntfs.patch: This is patch for GRUB to enable rudimentary support for NTFS alternate data
   streams.
 - make\_grub\_image.sh: Run this script from within the grub source directory after applying the
   patch and running `./configure && make`. It will create a file named uinst000.bak.
 - uinst001.bak: This is a grub4dos stage1 file. Copy it and the generated uinst000.bak to the root
   of the NTFS filesystem.
 - filesystem.xz: This contains a compressed ext3 filesystem containing a base Debian 8.1 jessie
   installation. It must be extracted into `\Windows\System32\ntmincore.dll:$SysRestore`.

Setup Instructions
---
 1. You need to mount your NTFS partition on a Linux machine using ntfs-3g with
    `-o streams\_interface=windows`. If you create the alternate data stream from within Windows, it
    structures the filesystem in a way that the GRUB module can't handle. I did not have time to
    debug this.
 2. Copy uinst000.bak and uinst001.bak into the root of the filesystem.
 3. `xzcat filesystem.xz > /mnt/Windows/System32/ntmincore.dll:\$SysRestore`
 4. Boot into Windows.
 5. Open an Admin Command Prompt.
 6. `bcdedit /create /application BOOTSECTOR`. This will print a GUID that you need to copy for the
    following steps.
 7. `bcdedit /set {GUID} device partition=C:` (Assuming your Windows drive is C:)
 8. `bcdedit /set {GUID} path \uinst001.bak`
 9. `bcdedit /displayorder {GUID} /addlast`
 10. `shutdown /r /o /t 0`
 11. When you get the options menu, select "Advanced Options" -> "System Restore".
 12. Enjoy your Linux system.

Limitations
---
 - Only works on BIOS systems with MSDOS disklabels. Making it work on EFI/GPT systems should be
   straightforward but I ran out of time.
 - Does not work on Bitlocker-encrypted volumes, for obvious reasons.
 - Assumes Windows is installed on the second disk partition.

Demo
---
See [YouTube](https://youtu.be/1LxpyYqTQ_Q) for a demo.
