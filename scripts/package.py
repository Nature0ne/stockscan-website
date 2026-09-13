"""Add web/social assets to the official app marketing kit without duplicate entries."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib, json
ROOT=Path(__file__).resolve().parent.parent
folder=ROOT/'assets/marketing'
archive=folder/'StockScan-1.4.0-Marketing.zip'
additions=[p for p in folder.iterdir() if p.suffix in ['.png','.jpg','.txt'] and not p.name[:2].isdigit()]
added_names={'web-social/'+p.name for p in additions}
tmp=archive.with_suffix('.new.zip')
with ZipFile(archive) as src, ZipFile(tmp,'w',compression=ZIP_DEFLATED) as dst:
 for item in src.infolist():
  if item.filename not in added_names:dst.writestr(item,src.read(item.filename))
 for p in sorted(additions):dst.write(p,'web-social/'+p.name)
tmp.replace(archive)
manifest=[]
for p in sorted(folder.iterdir()):
 if p.suffix in ['.png','.jpg','.txt','.zip']:
  manifest.append({'file':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(folder/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Packaged assets and checksums.')
