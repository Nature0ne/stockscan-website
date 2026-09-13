"""Build the static bilingual site with Python's standard library. No runtime build needed."""
from pathlib import Path
from html import escape as esc
import json
ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://nature0ne.github.io/stockscan-website/'
STORE = 'https://apps.apple.com/app/id6760256901'
APPLE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.9 12.8c0-2 1.6-3 1.7-3.1-1-1.5-2.6-1.7-3.2-1.7-1.4-.1-2.7.9-3.4.9-.7 0-1.7-.9-2.8-.8-1.5 0-2.9.9-3.7 2.2-1.6 2.7-.4 6.7 1.1 8.9.7 1.1 1.6 2.3 2.7 2.2 1.1 0 1.5-.7 2.9-.7 1.3 0 1.7.7 2.9.7 1.2 0 1.9-1.1 2.6-2.2.8-1.2 1.1-2.4 1.2-2.5-.1 0-2.1-.8-2.1-3.9zM15.6 6.5c.6-.8 1.1-1.9 1-3-.9.1-2.1.6-2.8 1.4-.6.7-1.2 1.8-1 2.9 1 .1 2.1-.5 2.8-1.3z"/></svg>'
C = {
'de': {
 'title':'StockScan – Deine Inventur. Mit Überblick.',
 'description':'Barcodes scannen, Mengen zählen und Inventuren abschließen. Freie und feste Inventuren, kostenloser CSV-Export und Pro mit Excel, Watch-Listen und privatem iCloud-Sync.',
 'nav':['Funktionen','Die App','Free & Pro','Support'],
 'download':'Kostenlos laden', 'store':'Im App Store laden', 'skip':'Zum Inhalt', 'media':'Presse & Medien', 'privacy':'Datenschutz', 'imprint':'Impressum',
 'hero_label':'Inventur für iPhone, iPad & Apple Watch',
 'hero_title':'Deine Inventur.<br>Mit <em>Überblick.</em>',
 'hero_text':'Vom ersten Scan bis zum fertigen Bericht. Zähle, was da ist. Behalte im Blick, was fehlt. Und mach aus deinem Bestand eine klare Liste.',
 'hero_secondary':'So funktioniert’s', 'hero_small':'1 aktive Inventur · 100 Artikel · CSV-Export kostenlos',
 'chip_top':'Frei zählen. Oder nach Plan.', 'chip_sub':'Dein Bestand. Dein Ablauf.', 'chip_bottom':'Gezählt. Bereit zum Teilen.', 'chip_bottom_sub':'CSV kostenlos · Excel mit Pro',
 'screen_note':'ECHTE APP-ANSICHT · BEISPIELDATEN',
 'benefits':['Kerninventur auch offline','Ohne StockScan-Konto','CSV kostenlos exportieren','Deutsch & Englisch'],
 'workflow_label':'Ein Ablauf. Alles im Blick.', 'workflow_title':'Weniger Zettel.<br>Mehr <em>Klarheit.</em>', 'workflow_intro':'Drei klare Bereiche begleiten dich durch deine Inventur: Erfassen, Listen und Daten.',
 'steps':[
  ['Erfassen','Scan rein.<br>Menge dazu.','Scanne einen Barcode oder gib die Artikelnummer ein. Rechne Gebinde direkt aus und speichere Menge, Einheit und Kommentar.','02-quantity'],
  ['Listen','Alles gezählt?<br>Siehst du sofort.','Organisiere deine Bestände. Mit fester Vorgabe erkennst du offene Artikel; Pro ergänzt die Soll-/Ist-Auswertung.','01-inventory'],
  ['Daten','Dein Ergebnis.<br>Zum Weiterarbeiten.','Artikelstamm importieren, Inventur abschließen, Bericht teilen. CSV ist kostenlos, angereicherte Excel-Berichte gibt’s mit Pro.','05-export']],
 'new_label':'Neu in 1.4', 'new_title':'Zähle frei.<br>Oder mit <em>festem Plan.</em>',
 'new_text':'Jede Inventur beginnt anders. Starte direkt mit den Artikeln vor dir – oder übernimm eine feste Artikelvorgabe aus Excel, CSV oder TSV.',
 'new_rows':[
  ['Deine Vorgabe. Deine Reihenfolge.','Scanne Vorgabeartikel in beliebiger Reihenfolge. Zusätzliche Artikel werden gesondert gekennzeichnet.'],
  ['Offen bleibt nicht unbemerkt.','Vor dem Abschluss zählst du offene Vorgabeartikel nach oder überspringst sie ausdrücklich. Gezählt mit null bleibt davon unterscheidbar.'],
  ['Beim nächsten Mal wieder bereit.','Setze die Zählungen zurück und verwende dieselbe Vorgabe erneut. Eindeutige Stammdaten-Treffer ergänzen fehlende Namen, EANs und Einheiten.']],
 'new_note':'Jeden Vorgabeartikel prüfen.<br>Bewusst abschließen.',
 'work_label':'Für deinen Arbeitsalltag', 'work_title':'Wo Bestand ist,<br>ist <em>StockScan.</em>',
 'work_text':'Ersatzteile im Lager, Material in der Werkstatt oder Ausstattung im Servicefahrzeug: Erfasse deinen Bestand dort, wo du ihn brauchst. Auch ohne Internetverbindung.',
 'work_tags':['Lager & Ersatzteile','Werkstatt & Handwerk','Service & Fahrzeug'],
 'features':[
  ['Rechnen beim Zählen','7 × 8 statt 56 einzutippen. Mengenberechnung, eigene Einheiten und Kommentare sind direkt in der Erfassung erreichbar.',False],
  ['Den Artikelstamm mitnehmen','Importiere Produkte sowie Hersteller- und Lieferantenzuordnungen. Vor der Übernahme prüfst du die erkannten Daten.',False],
  ['Abschließen und nachsehen','Bewahre den gezählten Stand in der unveränderlichen Historie. Bestehende Daten bleiben auch ohne Pro sichtbar.',False],
  ['Schneller im Scanfluss','Fast Scan ergänzt direkte Wiederholungszählungen und einstellbare Zählschritte für deine Gebinde.',True],
  ['Fortschritt im Blick','Live Activities zeigen den Inventurfortschritt auf dem Sperrbildschirm und in der Dynamic Island unterstützter iPhones.',False],
  ['Import mit Unterstützung','Intelligente Spaltenerkennung mit Apple Intelligence auf unterstützten Geräten, wenn verfügbar. Die normale Erkennung bleibt erhalten.',False]],
 'gallery_label':'Ein Blick in die App','gallery_title':'Klar im Aufbau.<br>Nah an deiner Arbeit.',
 'gallery_intro':'Echte Ansichten von StockScan 1.4 – mit Beispieldaten aus einer Werkstatt. Auf iPhone und iPad.',
 'previous':'Vorherige App-Ansicht','next':'Nächste App-Ansicht',
 'captions':['Inventur im Überblick','Mengen direkt berechnen','Vorgabeartikel prüfen','Daten übernehmen','CSV & Excel exportieren','Inventuren organisieren'],
 'ipad_label':'Deine Apple-Geräte', 'ipad_title':'Mehr Fläche auf dem iPad.<br>Ein Zähler am Handgelenk.',
 'ipad_text':'Nutze die native iPad-Oberfläche für deine Listen. Auf der Apple Watch zählst du einen Artikel kostenlos; Pro bringt ganze Inventurlisten ans Handgelenk. Bei unterbrochener Verbindung werden Änderungen bis zur Bestätigung durch das iPhone zwischengespeichert.',
 'price_label':'Free & StockScan Pro', 'price_title':'Klein anfangen.<br>Mit deinem Bestand <em>wachsen.</em>',
 'price_text':'Eine vollständige Inventur kostenlos. Mehr Möglichkeiten, wenn du sie brauchst.',
 'free_kicker':'Für den Anfang. Und mehr.', 'free_name':'StockScan Free','free_text':'Kostenlos laden und direkt loszählen.',
 'free_items':['1 aktive Inventur mit bis zu 100 unterschiedlichen Artikeln','Freie oder feste Inventur, Barcode-Scan und Mengenrechner','Produkt- und Herstellerdaten importieren','Abschluss und unveränderliche Historie','Unbegrenzter CSV-Export','Apple-Watch-Einzelzähler'],
 'pro_kicker':'Für deinen regelmäßigen Workflow','pro_name':'StockScan Pro','pro_text':'Als Monats- oder Jahresabo in der App erhältlich.',
 'pro_items':['Unbegrenzte aktive Inventuren und Artikel','Fast Scan mit einstellbaren Zählschritten','Angereicherte XLSX-Exporte','Vorlagen und Soll-/Ist-Auswertung','Historienvergleich und Differenzberichte','Ganze Inventurlisten auf der Apple Watch','Freiwilliger privater iCloud-Sync eigener Geräte','Apple Family Sharing für das Pro-Abo'],
 'pro_cta':'StockScan laden & Pro entdecken',
 'price_note':'Preise und ein gegebenenfalls verfügbarer Probezeitraum werden vor dem Kauf im App Store angezeigt. Abos verlängern sich automatisch und sind über dein Apple-Konto kündbar. Frühere Käufer der kostenpflichtigen App behalten dauerhaft Pro. Deine vorhandenen Daten bleiben ohne Pro lesbar und als CSV exportierbar.',
 'privacy_label':'Deine Daten bleiben deine Sache','privacy_title':'Lokal gespeichert.<br>Auf Wunsch <em>verbunden.</em>',
 'privacy_text':'Du brauchst kein StockScan-Konto. Deine Kerninventur arbeitet lokal – ohne Werbung und ohne Tracking in der App.',
 'privacy_points':[
  ['Offline zählen','Erfasse deinen Bestand ohne Internet. Lokale Inventurdaten bleiben die Grundlage deiner Arbeit.'],
  ['iCloud nur, wenn du willst','Mit Pro synchronisierst du Inventuren freiwillig über deine private iCloud-Datenbank zwischen eigenen Apple-Geräten. Importierte Stammdaten bleiben lokal.'],
  ['Abo teilen. Inventuren privat halten.','Apple Family Sharing teilt die Pro-Berechtigung mit deiner Familie. Es teilt keine Inventuren oder private iCloud-Datenbank.']],
 'faq_label':'Gut zu wissen','faq_title':'Noch eine Frage?', 'faq_text':'Hier sind die wichtigsten Antworten für deinen Start.', 'support_cta':'Zur Hilfe & zum Kontakt',
 'faqs':[
  ['Was ist kostenlos enthalten?','Eine aktive Inventur mit bis zu 100 unterschiedlichen Artikeln, freie oder feste Erfassung, Mengenberechnung, Stammdatenimport, Abschluss, Historie, unbegrenzter CSV-Export und der Apple-Watch-Einzelzähler.'],
  ['Was unterscheidet freie und feste Inventuren?','Bei einer freien Inventur erfasst du die Artikel, die du vorfindest. Eine feste Inventur beginnt mit einer importierten Artikelvorgabe. Jeder Vorgabeartikel muss vor dem Abschluss gezählt oder ausdrücklich übersprungen sein. Zusätzliche Artikel werden gekennzeichnet.'],
  ['Kann ich mit Excel und CSV arbeiten?','Ja. Importiere Produkt- und Herstellerdaten aus XLSX oder CSV. Feste Artikelvorgaben können zusätzlich als TSV vorliegen. CSV-Exporte sind kostenlos und unbegrenzt; angereicherte Excel-Berichte benötigen Pro. Numbers-Dateien exportierst du vorher als XLSX oder CSV.'],
  ['Funktioniert StockScan ohne Internet?','Die Kerninventur funktioniert offline. Käufe, Wiederherstellungen und die freiwillige iCloud-Synchronisierung benötigen eine Verbindung zu Apples Diensten. Watch-Zählungen werden bei unterbrochener Verbindung zwischengespeichert.'],
  ['Welche Geräte werden unterstützt?','StockScan läuft auf iPhone und iPad ab iOS beziehungsweise iPadOS 18. Die Begleit-App für die gekoppelte Apple Watch setzt watchOS 10 oder neuer voraus. Live Activities, Dynamic Island und Apple Intelligence hängen zusätzlich vom unterstützten Gerät und der Systemverfügbarkeit ab.'],
  ['Was passiert, wenn ich Pro kündige?','Bestehende Inventurdaten bleiben sichtbar und als CSV exportierbar. Für neue Listen und Artikel gelten wieder die Free-Limits. Pro-Funktionen wie XLSX und iCloud-Sync benötigen ein aktives Pro-Recht. Frühere Käufer der kostenpflichtigen App behalten ihren dauerhaften Pro-Zugriff.']],
 'cta_title':'Die nächste Inventur?<br>Beginnt mit <em>einem Scan.</em>', 'cta_text':'StockScan kostenlos laden. Deine erste Liste anlegen. Und loszählen.',
 'footer_line':'Für Bestände, die du im Blick behalten willst.','compat':'iOS / iPadOS 18+ · watchOS 10+',
 'media_title':'Material für<br>einen <em>klaren Auftritt.</em>', 'media_intro':'Offizielle StockScan-Materialien: echte App-Ansichten, fertige Motive und Texte für Website, Presse und Social Media. Auf Deutsch und Englisch.',
 'media_downloads':[
  ['Das komplette Marketingpaket','24 App-Store-Motive für iPhone und iPad, deutsche und englische Banner, Social-Posts, Stories, Texte und Übersichtsbögen.','Marketingpaket laden','StockScan-1.4.0-Marketing.zip'],
  ['Das Release-Motiv','StockScan 1.4 als PNG in 1600 × 900 Pixeln. Für Website, Newsletter und Präsentationen.','PNG herunterladen','release-banner-de.png'],
  ['Quadratischer Social-Post','Fertiges Motiv in 1080 × 1080 Pixeln mit echter App-Ansicht.','PNG herunterladen','square-de-1080x1080.png'],
  ['Story & Status','Hochformat in 1080 × 1920 Pixeln für Stories und Status-Beiträge.','PNG herunterladen','story-de-1080x1920.png'],
  ['Für geteilte Links','Social-Media-Grafik im Format 1200 × 630 Pixel. Für Link-Vorschauen und redaktionelle Beiträge.','JPG herunterladen','social-de.jpg']],
 'media_copy_title':'Texte, die du direkt nutzen kannst.',
 'media_copy':[
  ['Kurzbeschreibung','StockScan ist die Inventur-App für iPhone, iPad und Apple Watch. Erfasse Barcodes und Mengen, arbeite frei oder mit fester Artikelvorgabe und exportiere deine Ergebnisse kostenlos als CSV. Pro ergänzt unter anderem Excel-Berichte und private iCloud-Synchronisierung.'],
  ['Release-Post','Deine Inventur. Mit Überblick. StockScan 1.4 verbindet Erfassen, Listen und Daten in einem klaren Ablauf. Importiere feste Artikelvorgaben, prüfe offene Positionen vor dem Abschluss und nutze deine Vorgabe beim nächsten Mal erneut. Kostenlos starten: 1 aktive Inventur, bis zu 100 Artikel und unbegrenzter CSV-Export.'],
  ['Werkstatt-Post','Material im Regal. Mengen im Blick. Scanne Artikel, berechne Gebinde direkt in der App und nimm deinen Bestand als CSV mit. Für Lager, Werkstatt und Servicefahrzeug – mit einer Kerninventur, die auch offline funktioniert.'],
  ['Pro-Post','Für deine regelmäßige Inventur: StockScan Pro ergänzt unbegrenzte Listen und Artikel, Fast Scan, angereicherte Excel-Berichte, Soll-/Ist-Auswertung und ganze Zähllisten auf der Apple Watch. Optional hält privater iCloud-Sync deine eigenen Geräte auf demselben Stand.']],
 'media_terms':'Die Materialien dürfen zur Berichterstattung über StockScan und zur Bewerbung der App verwendet werden. App-Ansichten zeigen fiktive Beispieldaten. Bitte Pro-Kennzeichnungen und Einschränkungen bei Gerätefunktionen beibehalten. Markenrechte bleiben beim jeweiligen Rechteinhaber.',
},
'en': {
 'title':'StockScan – Your inventory. Clearly in view.',
 'description':'Scan barcodes, count quantities and complete inventories. Free and fixed inventories, free CSV export and Pro with Excel, Watch lists and private iCloud sync.',
 'nav':['Features','The app','Free & Pro','Support'],'download':'Get it free','store':'Download on the App Store','skip':'Skip to content','media':'Press & media','privacy':'Privacy','imprint':'Legal notice',
 'hero_label':'Inventory for iPhone, iPad & Apple Watch','hero_title':'Your inventory.<br>Clearly <em>in view.</em>',
 'hero_text':'From the first scan to your finished report. Count what’s there. See what’s missing. Turn your stock into a list that makes sense.',
 'hero_secondary':'See how it works','hero_small':'1 active inventory · 100 items · Free CSV export',
 'chip_top':'Count freely. Or follow a plan.','chip_sub':'Your stock. Your workflow.','chip_bottom':'Counted. Ready to share.','chip_bottom_sub':'Free CSV · Excel with Pro','screen_note':'REAL APP VIEW · SAMPLE DATA',
 'benefits':['Core inventory works offline','No StockScan account','Free CSV exports','English & German'],
 'workflow_label':'One workflow. All in view.','workflow_title':'Less paperwork.<br>More <em>clarity.</em>','workflow_intro':'Three clear workspaces take you through your inventory: Capture, Lists and Data.',
 'steps':[
  ['Capture','Scan the code.<br>Add the quantity.','Scan a barcode or enter an item number. Calculate packs right in the app and save quantity, unit and comment.','02-quantity'],
  ['Lists','All counted?<br>See for yourself.','Organise your stock. Fixed checklists show what’s still open; Pro adds target-versus-actual comparisons.','01-inventory'],
  ['Data','Your results.<br>Ready for work.','Import product data, complete your inventory and share a report. CSV is free; enriched Excel reports come with Pro.','05-export']],
 'new_label':'New in 1.4','new_title':'Count freely.<br>Or follow a <em>fixed plan.</em>',
 'new_text':'Every inventory starts differently. Begin with the items in front of you, or bring in a fixed checklist from Excel, CSV or TSV.',
 'new_rows':[
  ['Your checklist. Your order.','Scan required items in any order. Additional items are clearly marked separately.'],
  ['Uncounted doesn’t go unnoticed.','Before completing, count remaining required items or explicitly skip them. A counted zero stays distinct from a skipped item.'],
  ['Ready for the next round.','Reset counts and reuse the same checklist. Unique product-data matches fill in missing names, EANs and units.']],
 'new_note':'Check every required item.<br>Complete with confidence.',
 'work_label':'Built for your working day','work_title':'Where there’s stock,<br>there’s <em>StockScan.</em>',
 'work_text':'Spare parts in storage, materials in the workshop or equipment in your service van: capture your stock wherever you need to. Even without an internet connection.',
 'work_tags':['Storage & spare parts','Workshops & trades','Service & vehicles'],
 'features':[
  ['Calculate as you count','7 × 8 instead of typing 56. Quantity calculations, custom units and comments are right there in Capture.',False],
  ['Bring your product data','Import products and manufacturer or supplier mappings. Review the detected data before adding it.',False],
  ['Complete and look back','Keep an immutable record of your completed count. Existing inventory data stays readable even without Pro.',False],
  ['Stay in your scanning flow','Fast Scan adds repeat counting and configurable count steps for your packs.',True],
  ['Keep progress in sight','Live Activities show inventory progress on the Lock Screen and in the Dynamic Island on supported iPhones.',False],
  ['A helping hand with imports','Intelligent column recognition uses Apple Intelligence on supported devices when available. Standard recognition stays available.',False]],
 'gallery_label':'Inside the app','gallery_title':'Clear by design.<br>Made for your work.',
 'gallery_intro':'Real views of StockScan 1.4 with workshop sample data. On iPhone and iPad.',
 'previous':'Previous app view','next':'Next app view',
 'captions':['Inventory at a glance','Calculate quantities','Review required items','Bring in your data','Export CSV & Excel','Organise inventories'],
 'ipad_label':'Your Apple devices','ipad_title':'Room to work on iPad.<br>A counter on your wrist.',
 'ipad_text':'Use the native iPad interface for your lists. Count a single item on Apple Watch for free; Pro puts complete inventory lists on your wrist. When disconnected, changes are queued until your iPhone confirms them.',
 'price_label':'Free & StockScan Pro','price_title':'Start small.<br><em>Grow</em> with your inventory.',
 'price_text':'A complete inventory for free. More tools when you need them.',
 'free_kicker':'Start here. Keep going.','free_name':'StockScan Free','free_text':'Download for free and start counting.',
 'free_items':['1 active inventory with up to 100 different items','Free or fixed inventory, barcode scanning and quantity calculator','Product and manufacturer data imports','Completion and immutable history','Unlimited CSV exports','Apple Watch single-item counter'],
 'pro_kicker':'For your regular workflow','pro_name':'StockScan Pro','pro_text':'Available as a monthly or annual in-app subscription.',
 'pro_items':['Unlimited active inventories and items','Fast Scan with adjustable count steps','Enriched XLSX exports','Templates and target-versus-actual comparisons','History comparisons and difference reports','Complete inventory lists on Apple Watch','Optional private iCloud sync across your own devices','Apple Family Sharing for your Pro subscription'],
 'pro_cta':'Get StockScan & discover Pro',
 'price_note':'Prices and any available trial are shown in the App Store before purchase. Subscriptions renew automatically and can be cancelled through your Apple account. Previous buyers of the paid app keep permanent Pro access. Your existing data remains readable and exportable as CSV without Pro.',
 'privacy_label':'Your data is your business','privacy_title':'Stored locally.<br>Connected <em>by choice.</em>',
 'privacy_text':'No StockScan account required. Your core inventory works locally, without advertising or tracking in the app.',
 'privacy_points':[
  ['Count offline','Capture stock without an internet connection. Local inventory data stays the foundation of your work.'],
  ['iCloud when you want it','With Pro, optionally sync inventories through your private iCloud database across your own Apple devices. Imported master data stays local.'],
  ['Share Pro. Keep inventories private.','Apple Family Sharing shares the Pro entitlement with your family. It does not share inventories or your private iCloud database.']],
 'faq_label':'Good to know','faq_title':'Any questions?','faq_text':'The essentials to help you get started.','support_cta':'Get help & contact support',
 'faqs':[
  ['What’s included for free?','One active inventory with up to 100 different items, free or fixed counting, quantity calculations, master-data imports, completion, history, unlimited CSV exports and the Apple Watch single-item counter.'],
  ['What’s the difference between free and fixed inventories?','A free inventory captures the items you find. A fixed inventory starts with an imported checklist. Every required item must be counted or explicitly skipped before completion. Additional items are marked separately.'],
  ['Can I work with Excel and CSV?','Yes. Import product and manufacturer data from XLSX or CSV. Fixed checklists also support TSV. CSV exports are free and unlimited; enriched Excel reports require Pro. Export Numbers documents to XLSX or CSV first.'],
  ['Does StockScan work without internet?','Core inventory works offline. Purchases, restores and optional iCloud sync need a connection to Apple services. Watch counts are queued when the connection is interrupted.'],
  ['Which devices are supported?','StockScan runs on iPhone and iPad with iOS or iPadOS 18 and later. The paired Apple Watch companion requires watchOS 10 or later. Live Activities, Dynamic Island and Apple Intelligence also depend on device support and system availability.'],
  ['What happens if I cancel Pro?','Existing inventory data remains readable and exportable as CSV. Free limits apply again to new lists and items. Pro features such as XLSX and iCloud sync require an active entitlement. Previous buyers of the paid app keep permanent Pro access.']],
 'cta_title':'Your next inventory?<br>It starts with <em>one scan.</em>','cta_text':'Download StockScan for free. Create your first list. Start counting.',
 'footer_line':'For stock you want to keep in view.','compat':'iOS / iPadOS 18+ · watchOS 10+',
 'media_title':'Materials for<br>a <em>clear impression.</em>','media_intro':'Official StockScan materials: real app views, finished visuals and copy for websites, press and social media. In English and German.',
 'media_downloads':[
  ['The complete marketing kit','24 App Store visuals for iPhone and iPad, German and English banners, social posts, stories, copy and contact sheets.','Download marketing kit','StockScan-1.4.0-Marketing.zip'],
  ['The release visual','StockScan 1.4 as a 1600 × 900 PNG. For websites, newsletters and presentations.','Download PNG','release-banner-en.png'],
  ['Square social post','A finished 1080 × 1080 visual with a real app view.','Download PNG','square-en-1080x1080.png'],
  ['Stories & status','A 1080 × 1920 portrait visual for stories and status posts.','Download PNG','story-en-1080x1920.png'],
  ['Made for shared links','A 1200 × 630 social graphic for link previews and editorial posts.','Download JPG','social-en.jpg']],
 'media_copy_title':'Copy you can put to work.',
 'media_copy':[
  ['Short description','StockScan is the inventory app for iPhone, iPad and Apple Watch. Capture barcodes and quantities, count freely or follow a fixed checklist and export results as CSV for free. Pro adds tools including Excel reports and private iCloud sync.'],
  ['Release post','Your inventory. Clearly in view. StockScan 1.4 brings Capture, Lists and Data into one clear workflow. Import fixed checklists, review open items before completion and reuse your checklist next time. Start free: 1 active inventory, up to 100 items and unlimited CSV exports.'],
  ['Workshop post','Materials on the shelf. Quantities in view. Scan items, calculate packs right in the app and take your stock count with you as CSV. For storage, workshops and service vans, with core inventory that works offline.'],
  ['Pro post','For your regular stocktake: StockScan Pro adds unlimited lists and items, Fast Scan, enriched Excel reports, target-versus-actual comparisons and complete count lists on Apple Watch. Optional private iCloud sync keeps your own devices in step.']],
 'media_terms':'These materials may be used for reporting on StockScan and promoting the app. App views show fictional sample data. Please retain Pro labels and device availability qualifications. Trademarks remain the property of their respective owners.',
}}

def button(c, cls='', text=None):
 return f'<a class="button {cls}" href="{STORE}">{APPLE}<span>{text or c["store"]}</span></a>'

def picture(lang,key,device='iphone',eager=False,cls='phone'):
 pre='../' if lang=='en' else ''
 names={'01-inventory':C[lang]['captions'][0],'02-quantity':C[lang]['captions'][1],'03-review':C[lang]['captions'][2],'04-data':C[lang]['captions'][3],'05-export':C[lang]['captions'][4],'06-lists':C[lang]['captions'][5]}
 dimensions='width="660" height="1435"' if device=='iphone' else 'width="1000" height="1333"'
 priority='fetchpriority="high"' if eager else 'loading="lazy"'
 return f'<div class="{cls}"><img src="{pre}assets/screens/{device}-{lang}-{key}.webp" {dimensions} {priority} alt="StockScan: {esc(names[key])}"></div>'

def page(lang, filename, body, title=None, description=None):
 c=C[lang];pre='../' if lang=='en' else '';url=BASE+('en/' if lang=='en' else '')+(filename if filename!='index.html' else '')
 de=BASE+(filename if filename!='index.html' else '');en=BASE+'en/'+(filename if filename!='index.html' else '')
 title=title or c['title'];description=description or c['description']
 home='index.html' if filename!='index.html' else ''
 nav=''.join(f'<a href="{home}{target}">{label}</a>' for target,label in zip(['#features','#screenshots','#pro','support.html'],c['nav']))
 # Support links must remain page-relative, never prefixed with index.html.
 nav=nav.replace('index.htmlsupport.html','support.html')
 footer_links=''.join(f'<a href="{path}">{label}</a>' for path,label in [('media.html',c['media']),('support.html','Support'),('privacy.html',c['privacy']),('impressum.html',c['imprint'])])
 schema={'@context':'https://schema.org','@type':'SoftwareApplication','name':'StockScan','applicationCategory':'BusinessApplication','operatingSystem':'iOS 18, iPadOS 18, watchOS 10','url':BASE,'downloadUrl':STORE,'description':c['description'],'inLanguage':lang,'image':BASE+'img/icon.png'}
 return f'''<!doctype html>
<html lang="{lang}" class="no-js"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(description)}">
<meta name="theme-color" content="#103e31"><meta name="apple-itunes-app" content="app-id=6760256901">
<link rel="canonical" href="{url}"><link rel="alternate" hreflang="de" href="{de}"><link rel="alternate" hreflang="en" href="{en}"><link rel="alternate" hreflang="x-default" href="{de}">
<meta property="og:type" content="website"><meta property="og:site_name" content="StockScan"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:url" content="{url}"><meta property="og:locale" content="{'de_DE' if lang=='de' else 'en_US'}"><meta property="og:image" content="{BASE}assets/marketing/social-{lang}.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{esc(c['title'])}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="{pre}img/icon.png"><link rel="apple-touch-icon" href="{pre}img/icon.png"><link rel="stylesheet" href="{pre}assets/site.css"><script defer src="{pre}assets/site.js"></script>
<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False) if filename=='index.html' else json.dumps({'@context':'https://schema.org','@type':'WebPage','name':title,'url':url,'inLanguage':lang},ensure_ascii=False)}</script>
</head><body><a href="#main" class="skip">{c['skip']}</a>
<header class="site-header"><nav class="nav wrap" aria-label="{'Hauptnavigation' if lang=='de' else 'Main navigation'}"><a class="brand" href="index.html"><img src="{pre}img/icon.png" alt="" width="35" height="35">StockScan</a><div class="nav-links">{nav}</div><div class="nav-actions"><div class="languages" aria-label="{'Sprache' if lang=='de' else 'Language'}"><a href="{pre}{filename}" lang="de" hreflang="de" {'aria-current="page"' if lang=='de' else ''} aria-label="Deutsch">DE</a><span aria-hidden="true">/</span><a href="{'en/' if lang=='de' else ''}{filename}" lang="en" hreflang="en" {'aria-current="page"' if lang=='en' else ''} aria-label="English">EN</a></div>{button(c,'small',c['download'])}</div><div class="mobile-nav">{nav}</div></nav></header>
<main id="main">{body}</main>
<footer class="site-footer"><div class="wrap"><div class="footer-top"><a class="brand" href="index.html"><img src="{pre}img/icon.png" alt="" width="35" height="35">StockScan</a><div class="footer-links">{footer_links}</div></div><div class="footer-bottom"><p>© 2026 StockScan · Sascha Bommels</p><p>{c['footer_line']}</p><p>{c['compat']}</p></div></div></footer>
</body></html>'''

def faq_html(entries):
 return ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in entries)

def home(lang):
 c=C[lang];pre='../' if lang=='en' else ''
 steps=''.join(f'<article class="workflow-card"><div class="step-label"><span>{label}</span><b>0{i}</b></div><h3>{title}</h3><p>{text}</p>{picture(lang,key)}</article>' for i,(label,title,text,key) in enumerate(c['steps'],1))
 rows=''.join(f'<div class="detail-row"><b>0{i}</b><div><h3>{title}</h3><p>{text}</p></div></div>' for i,(title,text) in enumerate(c['new_rows'],1))
 features=''.join(f'<article class="feature"><h3>{title} {"<span class=tag>Pro</span>" if pro else ""}</h3><p>{text}</p></article>' for title,text,pro in c['features'])
 keys=['01-inventory','02-quantity','03-review','04-data','05-export','06-lists']
 gallery=''.join(f'<figure>{picture(lang,key)}<figcaption><span>0{i}</span>{caption}</figcaption></figure>' for i,(key,caption) in enumerate(zip(keys,c['captions']),1))
 plans=''
 for name in ['free','pro']:
  plans+=f'<article class="price-card {name}"><span class="kicker">{c[name+"_kicker"]}</span><h3>{c[name+"_name"]}</h3><p>{c[name+"_text"]}</p><ul>'+''.join(f'<li>{item}</li>' for item in c[name+'_items'])+f'</ul>{button(c,"light" if name=="pro" else "outline", c["pro_cta"] if name=="pro" else c["download"])}</article>'
 privacy=''.join(f'<div class="privacy-point"><h3>{title}</h3><p>{text}</p></div>' for title,text in c['privacy_points'])
 body=f'''
<section class="hero wrap" aria-labelledby="hero-title"><div class="hero-copy"><span class="eyebrow dot">{c['hero_label']}</span><h1 id="hero-title">{c['hero_title']}</h1><p class="lead">{c['hero_text']}</p><div class="hero-actions">{button(c)}<a class="text-link" href="#features">{c['hero_secondary']} <span aria-hidden="true">↗</span></a></div><p class="micro">{c['hero_small']}</p><div class="devices"><span>iPhone</span><span>iPad</span><span>Apple Watch</span></div></div><div class="hero-art"><div class="orbit" aria-hidden="true"></div><div class="orbit two" aria-hidden="true"></div><div class="hero-chip top"><strong>{c['chip_top']}</strong>{c['chip_sub']}</div>{picture(lang,'01-inventory',eager=True,cls='phone hero-phone')}<div class="hero-chip bottom"><span class="chip-check" aria-hidden="true">✓</span><div><strong>{c['chip_bottom']}</strong>{c['chip_bottom_sub']}</div></div><span class="art-note">{c['screen_note']}</span></div></section>
<div class="benefit-strip"><div class="wrap benefits">{''.join(f'<span><b aria-hidden="true">✓</b>{s}</span>' for s in c['benefits'])}</div></div>
<section id="features" class="section wrap"><div class="section-head"><div><span class="eyebrow">{c['workflow_label']}</span><h2>{c['workflow_title']}</h2></div><p>{c['workflow_intro']}</p></div><div class="workflow-grid">{steps}</div></section>
<section class="dark-section"><div class="section wrap new-layout"><div class="new-copy"><span class="tag">{c['new_label']}</span><h2>{c['new_title']}</h2><p>{c['new_text']}</p><div class="detail-list">{rows}</div></div><div class="new-art">{picture(lang,'03-review')}<div class="note">{c['new_note']}</div></div></div></section>
<section class="section wrap"><div class="workspace"><img class="workspace-photo" src="{pre}assets/workshop.webp" width="1536" height="1024" loading="lazy" alt="{'Werkstattregal mit grünen Kleinteilekästen und Materialkartons; illustratives KI-Motiv' if lang=='de' else 'Workshop shelves with green parts bins and material boxes; illustrative AI image'}"><div class="workspace-copy"><span class="eyebrow">{c['work_label']}</span><h2>{c['work_title']}</h2><p class="lead">{c['work_text']}</p><div class="pill-row">{''.join(f'<span class="pill">{s}</span>' for s in c['work_tags'])}</div></div></div><div class="feature-grid">{features}</div></section>
<section id="screenshots" class="gallery-section"><div class="section wrap"><span class="eyebrow">{c['gallery_label']}</span><h2>{c['gallery_title']}</h2><div class="gallery-head"><p>{c['gallery_intro']}</p><div class="gallery-nav"><button type="button" data-previous aria-label="{c['previous']}" aria-controls="app-gallery">←</button><button type="button" data-next aria-label="{c['next']}" aria-controls="app-gallery">→</button></div></div><div id="app-gallery" class="gallery" data-gallery tabindex="0" role="region" aria-label="{'App-Ansichten' if lang=='de' else 'App views'}">{gallery}</div><div class="ipad-row">{picture(lang,'06-lists',device='ipad',cls='ipad')}<div class="ipad-copy"><span class="eyebrow">{c['ipad_label']}</span><h3>{c['ipad_title']}</h3><p>{c['ipad_text']}</p><span class="tag">iPhone · iPad · Apple Watch</span></div></div></div></section>
<section id="pro" class="section wrap"><div class="pricing-head"><span class="eyebrow">{c['price_label']}</span><h2>{c['price_title']}</h2><p>{c['price_text']}</p></div><div class="pricing-grid">{plans}</div><p class="pricing-note">{c['price_note']} <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">EULA</a> · <a href="privacy.html">{c['privacy']}</a></p></section>
<section id="datenschutz" class="dark-section"><div class="section wrap privacy-grid"><div><span class="eyebrow">{c['privacy_label']}</span><h2>{c['privacy_title']}</h2><p>{c['privacy_text']}</p><a class="text-link" href="privacy.html">{c['privacy']} <span aria-hidden="true">↗</span></a></div><div class="privacy-points">{privacy}</div></div></section>
<section id="faq" class="section wrap faq-layout"><aside><span class="eyebrow">{c['faq_label']}</span><h2>{c['faq_title']}</h2><p>{c['faq_text']}</p><a class="text-link" href="support.html">{c['support_cta']} <span aria-hidden="true">↗</span></a></aside><div>{faq_html(c['faqs'])}</div></section>
<div class="wrap"><section class="cta"><h2>{c['cta_title']}</h2><p>{c['cta_text']}</p>{button(c)}</section></div>'''
 return page(lang,'index.html',body)

def media(lang):
 c=C[lang];pre='../' if lang=='en' else ''
 cards=''.join(f'<article class="download-card"><h2>{title}</h2><p>{description}</p><a class="text-link" download href="{pre}assets/marketing/{path}">{label} <span aria-hidden="true">↓</span></a></article>' for title,description,label,path in c['media_downloads'])
 copy=''.join(f'<article class="copy-card"><h3>{title}</h3><p>{text}</p></article>' for title,text in c['media_copy'])
 body=f'<div class="wrap"><div class="media-hero"><span class="eyebrow">StockScan · {c["media"]}</span><h1>{c["media_title"]}</h1><p class="lead">{c["media_intro"]}</p></div><div class="media-key"><img src="{pre}assets/marketing/release-banner-{lang}.png" width="1600" height="900" alt="{esc(c["title"])}"></div><div class="download-grid">{cards}</div><section class="section"><h2>{c["media_copy_title"]}</h2><div class="copy-grid">{copy}</div><p><a class="text-link" download href="{pre}assets/marketing/copy-{lang}.txt">{"Alle Texte herunterladen" if lang=="de" else "Download all copy"} ↓</a></p><p class="media-legal">{c["media_terms"]}</p></section></div>'
 return page(lang,'media.html',body,f'{c["media"]} – StockScan',c['media_intro'])

if __name__=='__main__':
 for lang in C:
  out=ROOT/('en' if lang=='en' else '')
  out.mkdir(exist_ok=True)
  (out/'index.html').write_text(home(lang))
  (out/'media.html').write_text(media(lang))
  (ROOT/'assets/marketing'/f'copy-{lang}.txt').write_text('\n\n'.join(title+'\n'+text for title,text in C[lang]['media_copy'])+'\n\n'+STORE+'\n')
 print('Built German and English home and media pages.')
