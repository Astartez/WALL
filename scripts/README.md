# WALL

## nightTab

`fileserver.py` - run localhost server

`geturllist.py.py` - print server file URLs

## Upscaling

Upscayl - Ultramix balanced

### PNG -> rescaled JPG

fish script

```bash
for input in ./in/*.png
    convert $input -resize 2560x1440^ -set filename:f '%t' +adjoin './out/%[filename:f].jpg'
end
```

bash script

```bash
for file in ./in/*.png
do
  convert $file -resize 3840x2160^ -set filename:f '%t' +adjoin './out/%[filename:f].jpg'
done
```

🥝
