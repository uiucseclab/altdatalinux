#!/bin/sh
TMPFILE=`mktemp`
cat > $TMPFILE <<EOF
loopback loop0 (hd0,msdos2)/Windows/System32/ntmincore.dll:\\\$SysRestore
set root=(loop0)
set prefix=/boot/grub
insmod linux
linux /vmlinuz root=/dev/loop0
initrd /initrd.img
boot
EOF

./grub-mkimage -c $TMPFILE -C xz -d grub-core -o grub-core/core.img -O i386-pc ntfs loopback biosdisk part_msdos ext2
rm $TMPFILE
cat grub-core/lnxboot.img grub-core/core.img > uinst000.bak
