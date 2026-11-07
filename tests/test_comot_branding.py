"""Brand-asset acceptance checks. Run: python -m unittest discover -s tests -p test_comot_branding.py -v"""
import pathlib, unittest, re, subprocess, xml.etree.ElementTree as ET
from PIL import Image
ROOT=pathlib.Path(__file__).resolve().parents[1]
SOURCE=ROOT/'tests/fixtures/comot-original.png'
BASE='443fb2a33648a86733c4360544cd8f291f5aeaae'

class ComotBranding(unittest.TestCase):
    def test_launcher_pngs_match_existing_comot_mark(self):
        source=Image.open(SOURCE).convert('RGBA')
        for size in [16,32,64,128,256,512]:
            with self.subTest(size=size):
                target=Image.open(ROOT/f'assets/icons/concat_logo_{size}.png').convert('RGBA')
                expected=source.resize((size,size),Image.Resampling.LANCZOS)
                self.assertEqual(target.size,(size,size))
                self.assertEqual(target.tobytes(),expected.tobytes(),'launcher still has upstream logo')

    def test_windows_ico_has_comot_image(self):
        source=Image.open(SOURCE).convert('RGBA')
        icon=Image.open(ROOT/'assets/icons/concat.ico')
        self.assertIn((256,256),icon.ico.sizes())
        self.assertEqual(icon.ico.getimage((256,256)).convert('RGBA').tobytes(),source.resize((256,256),Image.Resampling.LANCZOS).tobytes())
        icon.close()

    def test_embedded_and_readme_marks_are_comot(self):
        source=Image.open(SOURCE).convert('RGBA')
        for path,size in [('assets/concat_logo_512.png',512),('assets/concat-mark-dark.png',512),('src/crates/concat/ui/assets/concat-logo.png',64)]:
            with self.subTest(path=path):
                self.assertEqual(Image.open(ROOT/path).convert('RGBA').tobytes(),source.resize((size,size),Image.Resampling.LANCZOS).tobytes())
        readme=(ROOT/'README.md').read_text(encoding='utf-8')
        self.assertIn('alt="Comot"',readme[:500])
        self.assertNotIn('cdn.jsdelivr.net/gh/jub0t/Concat@main/assets/concat-mark-dark.png',readme[:500])

    def test_theme_svg_marks_embed_comot(self):
        import base64,io
        source=Image.open(SOURCE).convert('RGBA')
        files=list((ROOT/'assets').glob('new_concat_logo_512_*.svg'))
        self.assertEqual(len(files),4)
        for p in files:
            text=p.read_text();ET.fromstring(text)
            m=re.search(r'data:image/png;base64,([A-Za-z0-9+/=]+)',text)
            self.assertIsNotNone(m,p.name)
            self.assertEqual(Image.open(io.BytesIO(base64.b64decode(m.group(1)))).convert('RGBA').tobytes(),source.tobytes())

    def test_original_licenses_and_attribution_are_untouched(self):
        files=['LICENSE','LICENSING.md','CLA.md','TRADEMARK.md','THIRD_PARTY_NOTICES.md']
        changed=subprocess.check_output(['git','-C',str(ROOT),'diff','--name-only',BASE,'--',*files],text=True).strip()
        self.assertEqual(changed,'')

if __name__=='__main__':unittest.main()
