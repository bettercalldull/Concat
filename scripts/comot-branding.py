#!/usr/bin/env python3
"""Regenerate Comot logo assets from the existing Comot header mark (128px raster).
Requires Pillow only for this developer utility, not for the editor runtime.
The SVG containers embed the authentic raster; they are not a vector redraw.
"""
from pathlib import Path
from PIL import Image
import base64, io
ROOT=Path(__file__).resolve().parents[1]
source=Image.open(ROOT/'tests/fixtures/comot-original.png').convert('RGBA')
for size in [16,32,64,128,256,512]:
    source.resize((size,size),Image.Resampling.LANCZOS).save(ROOT/f'assets/icons/concat_logo_{size}.png')
for rel,size in [('assets/concat_logo_512.png',512),('assets/concat-mark-dark.png',512),('src/crates/concat/ui/assets/concat-logo.png',64)]:
    source.resize((size,size),Image.Resampling.LANCZOS).save(ROOT/rel)
source.resize((256,256),Image.Resampling.LANCZOS).save(ROOT/'assets/icons/concat.ico',format='ICO',sizes=[(16,16),(24,24),(32,32),(48,48),(64,64),(128,128),(256,256)])
b=io.BytesIO();source.save(b,format='PNG');data=base64.b64encode(b.getvalue()).decode()
svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512"><title>Comot</title><image width="512" height="512" href="data:image/png;base64,{data}"/></svg>\n'
for name in ['dark_theme_rounded','rounded_light_theme','square_dark_theme','square_light_theme']:
    (ROOT/f'assets/new_concat_logo_512_{name}.svg').write_text(svg,encoding='utf-8')
print('Generated Comot PNG, ICO and theme SVG assets from original 128x128 Comot mark')
