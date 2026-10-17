"""Refresh real StockScan marketing assets; never draw or modify native app UI.

Requires Pillow. Run with --source pointing to the app's marketing/1.5.1
directory. --package-only rebuilds the downloadable kit and manifest using only
the committed website files, for example after updating copy via build.py.
"""
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
import argparse
import hashlib
import json
import shutil
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
MEDIA = ROOT / 'assets/marketing'
SCREENS = ROOT / 'assets/screens'
ARCHIVE = 'StockScan-Media-DE-EN-2026-10-17.zip'
# Website filenames stay stable; native states follow the approved new campaign.
MOTIFS = [
    ('01-inventory', '01-inventory', '01-capture'),
    ('02-quantity', '04-quantity', '04-calculator'),
    ('03-review', '02-review', '02-review'),
    ('04-data', '05-data', '05-import'),
    ('05-export', '03-export', '03-export'),
    ('06-lists', '06-history', '06-repeat'),
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def describe(path, name=None):
    row = {'file': name or path.name, 'bytes': path.stat().st_size,
           'sha256': digest(path)}
    if path.suffix.lower() in {'.png', '.jpg', '.webp'}:
        with Image.open(path) as image:
            image.verify()
        with Image.open(path) as image:
            row.update(width=image.width, height=image.height)
    return row


def fit_artwork(source, target, size, jpeg=False):
    # Fit the ENTIRE approved artwork. No cropping, UI overlay, or new claims.
    with Image.open(source) as image:
        rgb = image.convert('RGB')
        background = rgb.getpixel((0, 0))
        contained = ImageOps.contain(rgb, size, Image.Resampling.LANCZOS)
        canvas = Image.new('RGB', size, background)
        canvas.paste(contained, ((size[0] - contained.width) // 2,
                                (size[1] - contained.height) // 2))
        canvas.save(target, quality=91, optimize=True) if jpeg else canvas.save(target, optimize=True)


def refresh(source):
    exports = source / 'open-assets/exports'
    provenance = {
        'prepared': '2026-10-17', 'source_campaign': 'StockScan marketing/1.5.1',
        'public_release_claim': None,
        'policy': 'Real native app captures. WebP conversion resizes/compresses only. '
                  'Full-size compositions and creatives are byte-identical originals. '
                  'Social derivatives contain complete approved artwork without cropping.',
        'capture_build': json.loads((source / 'capture-provenance.json').read_text()),
        'screen_mapping': [], 'files': [],
    }
    # Avoid shipping absolute developer-machine paths or local test outputs.
    capture = provenance['capture_build']
    provenance['capture_build'] = {key: capture[key] for key in
        ['source_commit', 'xcode', 'sdk', 'app_version', 'app_build', 'production_source_edits']}

    def record(target, original, transformation='byte-identical copy'):
        provenance['files'].append({
            **describe(target, target.relative_to(ROOT).as_posix()),
            'source': 'marketing/1.5.1/' + original.relative_to(source).as_posix(),
            'source_sha256': digest(original), 'transformation': transformation,
        })

    for device in ['iphone', 'ipad']:
        width = 660 if device == 'iphone' else 1000
        for language in ['de', 'en']:
            for website, native, composition in MOTIFS:
                raw = source / f'raw/{device}/marketing-{language}-{native}.png'
                target = SCREENS / f'{device}-{language}-{website}.webp'
                with Image.open(raw) as image:
                    size = (width, round(image.height * width / image.width))
                    image.resize(size, Image.Resampling.LANCZOS).convert('RGB').save(
                        target, 'WEBP', quality=88, method=6)
                record(target, raw, 'Lanczos resize; WebP quality 88, method 6')
                provenance['screen_mapping'].append({
                    'website': target.name, 'native_state': native,
                    'composition': composition})
                variant = 'iphone-large' if device == 'iphone' else 'ipad-13'
                original = exports / f'{device}/{language}/{variant}/{composition}.png'
                name = (f'{website}-{language}-1320x2868.png' if device == 'iphone'
                        else f'ipad-{language}-{website}-2064x2752.png')
                target = MEDIA / name
                shutil.copyfile(original, target)
                record(target, original)

    for language in ['de', 'en']:
        for kind in ['header', 'search']:
            original = exports / f'creatives/{language}/{kind}.png'
            target = MEDIA / f'{kind}-{language}.png'
            shutil.copyfile(original, target)
            record(target, original)
        derivatives = [
            ('header', f'release-banner-{language}.png', (1600, 900), False),
            ('header', f'social-{language}.jpg', (1200, 630), True),
            ('search', f'square-{language}-1080x1080.png', (1080, 1080), False),
        ]
        for kind, name, size, jpeg in derivatives:
            original = exports / f'creatives/{language}/{kind}.png'
            target = MEDIA / name
            fit_artwork(original, target, size, jpeg)
            record(target, original, 'Complete artwork contained in canvas; Lanczos resize')
        original = exports / f'iphone/{language}/iphone-large/01-capture.png'
        target = MEDIA / f'story-{language}-1080x1920.png'
        fit_artwork(original, target, (1080, 1920))
        record(target, original, 'Complete artwork contained in canvas; Lanczos resize')

    original = source / 'open-assets/public/apple/license.rtf'
    target = MEDIA / 'apple-frames-license.rtf'
    shutil.copyfile(original, target)
    record(target, original)
    (MEDIA / 'provenance.json').write_text(json.dumps(provenance, indent=2, ensure_ascii=False) + '\n')


def package():
    # Deliberately curate files rather than sweeping source folders: no capture
    # logs, developer workspaces, credentials, or draft release state in the kit.
    included = sorted(p for p in MEDIA.iterdir() if p.suffix in {'.png', '.jpg', '.txt', '.rtf'})
    included += [MEDIA / 'provenance.json']
    target = MEDIA / ARCHIVE
    with ZipFile(target, 'w', compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for path in included:
            if path.suffix == '.png' and (path.name[:2].isdigit() or path.name.startswith('ipad-')):
                folder = 'screenshots/'
            elif path.name.startswith(('header-', 'search-')):
                folder = 'creatives/'
            elif path.suffix in {'.png', '.jpg'}:
                folder = 'web-social/'
            else:
                folder = ''
            info = ZipInfo(folder + path.name, (2026, 10, 17, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compresslevel=9)
        info = ZipInfo('README.md', (2026, 10, 17, 0, 0, 0))
        info.compress_type = ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        archive.writestr(info, (ROOT / 'marketing/README.md').read_bytes(), compresslevel=9)
    obsolete = MEDIA / 'StockScan-1.4.0-Marketing.zip'
    obsolete.unlink(missing_ok=True)
    manifest = [describe(path) for path in sorted(MEDIA.iterdir())
                if path.is_file() and path.name != 'manifest.json']
    (MEDIA / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps({'archive': describe(target), 'media_files': len(manifest),
                      'screens': len(list(SCREENS.glob('*.webp')))}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path,
                        default=ROOT.parent / 'StockScan/marketing/1.5.1')
    parser.add_argument('--package-only', action='store_true')
    args = parser.parse_args()
    if not args.package_only:
        refresh(args.source.resolve())
    package()
