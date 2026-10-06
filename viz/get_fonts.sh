#!/usr/bin/env bash
# Download the house font set (all SIL Open Font License) into brand/fonts/. Idempotent.
set -e; mkdir -p /home/user/brand/fonts; cd /home/user/brand/fonts
B=https://raw.githubusercontent.com/google/fonts/main/ofl
get(){ [ -s "$1" ] || curl -sfL --retry 2 -o "$1" "$2" || echo "font download failed: $1"; }
get Inter.ttf              "$B/inter/Inter%5Bopsz,wght%5D.ttf"
get Geist.ttf              "$B/geist/Geist%5Bwght%5D.ttf"
get GeistMono.ttf          "$B/geistmono/GeistMono%5Bwght%5D.ttf"
get SpaceGrotesk.ttf       "$B/spacegrotesk/SpaceGrotesk%5Bwght%5D.ttf"
get Archivo.ttf            "$B/archivo/Archivo%5Bwdth,wght%5D.ttf"
get Anton.ttf              "$B/anton/Anton-Regular.ttf"
get JetBrainsMono.ttf      "$B/jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf"
get InstrumentSerif.ttf    "$B/instrumentserif/InstrumentSerif-Regular.ttf"
get BricolageGrotesque.ttf "$B/bricolagegrotesque/BricolageGrotesque%5Bopsz,wdth,wght%5D.ttf"
get NotoSansDevanagari.ttf "$B/notosansdevanagari/NotoSansDevanagari%5Bwdth,wght%5D.ttf"
get OFL.txt                "$B/inter/OFL.txt"
