#!/bin/bash
# raw PNG/JPEG -> web webp (+ og jpg). Usage: ./process.sh
set -e
S=/home/kali/webexpress-site/demo

w() { # src dst width quality
  magick "$1" -resize "${3}x>" -strip -quality "${4:-80}" "$2"
}

# --- kafejnica ---
K=$S/kafejnica/assets
w $K/raw/hero-cup.png        $K/hero-cup.webp       900
w $K/raw/hero-iced.png       $K/hero-iced.webp      700
w $K/raw/hero-shelf.png      $K/hero-shelf.webp     700
w $K/raw/hero-counter.png    $K/hero-counter.webp   700
w $K/raw/menu-espresso.png   $K/menu-espresso.webp  800
w $K/raw/menu-latte.png      $K/menu-latte.webp     800
w $K/raw/menu-filter.png     $K/menu-filter.webp    800
w $K/raw/pastry.png          $K/pastry.webp        1400
w $K/raw/interior-wide.png   $K/interior-wide.webp 1600
magick $K/raw/reveal-green.png   -resize 1200x900^ -gravity center -extent 1200x900 -strip -quality 80 $K/reveal-green.webp
magick $K/raw/reveal-roasted.png -resize 1200x900^ -gravity center -extent 1200x900 -strip -quality 80 $K/reveal-roasted.webp
magick $K/raw/og.png -resize 1200x630^ -gravity center -extent 1200x630 -strip -quality 82 $K/og.jpg

# --- detailing ---
D=$S/detailing/assets
w $D/raw/hero-car-clean.png  $D/hero-car.webp      1600
w $D/raw/hero-car-dark.png   $D/car-rear.webp      1200
w $D/raw/polish.png          $D/polish.webp         800
w $D/raw/beading.png         $D/beading.webp        800
w $D/raw/wheel.png           $D/wheel.webp          800
w $D/raw/interior.png        $D/interior.webp       800
w $D/raw/engine.png          $D/engine.webp         800
w $D/raw/tools.png           $D/tools.webp         1400
magick $D/raw/reveal-dirty.png -resize 1200x675^ -gravity center -extent 1200x675 -strip -quality 80 $D/reveal-dirty.webp
magick $D/raw/reveal-clean.png -resize 1200x675^ -gravity center -extent 1200x675 -strip -quality 80 $D/reveal-clean.webp
magick $D/raw/og.png -resize 1200x630^ -gravity center -extent 1200x630 -strip -quality 82 $D/og.jpg

# --- dental ---
T=$S/dental/assets
w $T/raw/hero-implant.png    $T/hero-implant.webp   928 88
w $T/raw/tray.png            $T/tray.webp           800
w $T/raw/aligner.png         $T/aligner.webp        800
w $T/raw/veneers.png         $T/veneers.webp        800
w $T/raw/scanner.png         $T/scanner.webp        800
w $T/raw/hygiene.png         $T/hygiene.webp        800
w $T/raw/chair.png           $T/chair.webp         1400
magick $T/raw/og.png -resize 1200x630^ -gravity center -extent 1200x630 -strip -quality 82 $T/og.jpg
