for img in skins/$1/*.png; do
  ffmpeg -y -i "$img" -vf "scale=iw/5:ih/5,scale=iw*5:ih*5:flags=neighbor" "pixelated/$1/$(basename "$img")"
done