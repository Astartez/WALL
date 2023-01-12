# WALL

## nightTab

`fileserver.py` - run localhost server

`geturllist.py.py` - print server file URLs

## Upscaling

Upscayl - Ultramix balanced

### PNG -> rescaled JPG

fish script

```bash
for input in ./leftovers/sized/*.png
    magick.exe $input -resize 2560x1440^ -set filename:f '%t' +adjoin './leftovers/down/%[filename:f].jpg'
end
```

🥝
