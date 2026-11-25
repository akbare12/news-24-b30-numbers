import os
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024
OUT=os.path.join(os.environ.get('MAKEFUN_OUTPUT_DIR','out'),'entry.png')
BG=(250,246,236); INK=(22,22,22); RED=(178,34,34); NAVY=(24,48,96); GREY=(96,96,96); LINE=(200,192,176)
SERIF='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'; SANS='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; SANSB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def F(p,s):
    try: return ImageFont.truetype(p,s)
    except Exception: return ImageFont.load_default()
def wrap(d,t,f,mw):
    ls=[]; c=''
    for w in t.split():
        x=(c+' '+w).strip()
        if d.textlength(x,font=f)<=mw: c=x
        else: ls.append(c); c=w
    if c: ls.append(c)
    return ls
def chip(d,x,y,t,bg,fs=8):
    w=int(d.textlength(t,font=F(SANSB,fs)))+10; d.rounded_rectangle([x,y,x+w,y+13],2,fill=bg); d.text((x+5,y+2),t,font=F(SANSB,fs),fill='white'); return w
def stars(d,x,y,w,h,n=14):
    import random; r=random.Random(7)
    for _ in range(n):
        sx=x+r.randint(2,w-2); sy=y+r.randint(2,h//2); d.ellipse([sx,sy,sx+2,sy+2],fill=(220,225,240))
def scene(d,x,y,w,h,k):
    if k=='tower':
        d.rectangle([x,y,x+w,y+h],fill=(14,22,46)); stars(d,x,y,w,h)
        d.rectangle([x+w*.40,y+16,x+w*.58,y+h],fill=(38,58,108)); d.polygon([(x+w*.40,y+16),(x+w*.58,y+16),(x+w*.50,y+2)],fill=(86,116,178))
        for r in range(5):
            for c in range(3): d.rectangle([x+w*.43+c*w*.045,y+24+r*11,x+w*.43+c*w*.045+5,y+24+r*11+6],fill=(250,210,90))
        d.ellipse([x+w*.60,y+8,x+w*.86,y+34],fill=(255,120,30)); d.ellipse([x+w*.66,y+14,x+w*.80,y+28],fill=(255,190,60))
        d.rectangle([x+w*.66,y+40,x+w*.68,y+46],fill=(200,200,200)); d.rectangle([x+w*.60,y+44,x+w*.74,y+46],fill=(200,200,200))
        d.rectangle([x,y+h-8,x+w,y+h],fill=(30,30,40))
    elif k=='gate':
        d.rectangle([x,y,x+w,y+h],fill=(232,214,180)); d.rectangle([x,y+h*.55,x+w,y+h],fill=(150,32,32))
        d.rectangle([x+w*.30,y+h*.28,x+w*.70,y+h*.62],fill=(178,44,36)); d.polygon([(x+w*.22,y+h*.30),(x+w*.78,y+h*.30),(x+w*.70,y+h*.14),(x+w*.30,y+h*.14)],fill=(210,170,40))
        d.rectangle([x+w*.44,y+h*.62,x+w*.56,y+h*.86],fill=(60,30,30)); d.rectangle([x+w*.08,y+h*.62,x+w*.16,y+h*.86],fill=(60,30,30)); d.rectangle([x+w*.84,y+h*.62,x+w*.92,y+h*.86],fill=(60,30,30))
        d.rectangle([x+w*.62,y+h*.66,x+w*.94,y+h*.88],fill=(250,250,244)); d.rectangle([x+w*.62,y+h*.66,x+w*.94,y+h*.88],outline=(120,120,120))
        d.text((x+w*.65,y+h*.70),'PROBE',font=F(SANSB,11),fill=RED)
    elif k=='court':
        d.rectangle([x,y,x+w,y+h],fill=(214,222,232)); d.polygon([(x+w*.10,y+h*.34),(x+w*.50,y+h*.10),(x+w*.90,y+h*.34)],fill=(120,130,150))
        for c in range(4): d.rectangle([x+w*(.16+c*.19),y+h*.36,x+w*(.16+c*.19)+w*.07,y+h*.86],fill=(245,245,240))
        d.rectangle([x+w*.08,y+h*.86,x+w*.92,y+h*.94],fill=(90,96,110)); d.rectangle([x+w*.42,y+h*.60,x+w*.58,y+h*.86],fill=(60,60,70))
        d.ellipse([x+w*.74,y+h*.55,x+w*.94,y+h*.72],fill=(178,34,34)); d.text((x+w*.765,y+h*.60),'10/12',font=F(SANSB,10),fill='white')
    elif k=='drones':
        d.rectangle([x,y,x+w,y+h],fill=(16,20,40)); stars(d,x,y,w,h,10)
        for i,(dx,dy) in enumerate([(0.2,0.2),(0.5,0.12),(0.75,0.3),(0.35,0.38)]): d.ellipse([x+w*dx,y+h*dy,x+w*dx+5,y+h*dy+5],fill=(255,200,80)); d.line([x+w*dx-8,y+h*dy+2,x+w*dx,y+h*dy+2],fill=(255,200,80),width=1)
        d.rectangle([x+w*.10,y+h*.62,x+w*.30,y+h],fill=(40,44,60)); d.rectangle([x+w*.36,y+h*.55,x+w*.62,y+h],fill=(34,38,54)); d.rectangle([x+w*.68,y+h*.68,x+w*.90,y+h],fill=(44,48,66))
        d.polygon([(x+w*.42,y+h*.55),(x+w*.52,y+h*.42),(x+w*.58,y+h*.55)],fill=(255,140,40)); d.polygon([(x+w*.46,y+h*.62),(x+w*.52,y+h*.50),(x+w*.58,y+h*.62)],fill=(255,200,60))
    elif k=='trophy':
        d.rectangle([x,y,x+w,y+h],fill=(18,80,52)); d.rectangle([x,y,x+w*.10,y+h],fill=(0,120,60)); d.rectangle([x,y+h*.30,x+w,y+h*.38],fill=(252,209,22))
        d.ellipse([x+w*.42,y+h*.22,x+w*.58,y+h*.48],fill=(252,209,22)); d.rectangle([x+w*.47,y+h*.46,x+w*.53,y+h*.66],fill=(252,209,22)); d.rectangle([x+w*.38,y+h*.64,x+w*.62,y+h*.70],fill=(252,209,22))
        d.rectangle([x+w*.68,y+h*.55,x+w*.94,y+h*.62],fill=(200,30,40)); d.rectangle([x+w*.06,y+h*.55,x+w*.32,y+h*.62],fill=(0,120,60))
        d.text((x+w*.30,y+h*.74),'SENEGAL 1-0',font=F(SANSB,11),fill='white')
    elif k=='ship':
        d.rectangle([x,y,x+w,y+h*.62],fill=(170,205,230)); d.rectangle([x,y+h*.62,x+w,y+h],fill=(24,80,130))
        d.rectangle([x+w*.10,y+h*.55,x+w*.90,y+h*.72],fill=(40,44,52))
        for i,c in enumerate([(200,60,50),(40,120,200),(252,200,60),(60,160,80)]): d.rectangle([x+w*(.14+i*.18),y+h*.34,x+w*(.14+i*.18)+w*.15,y+h*.55],fill=c)
        d.rectangle([x+w*.80,y+h*.28,x+w*.88,y+h*.55],fill=(240,240,235)); d.polygon([(x+w*.94,y+h*.60),(x+w*.99,y+h*.50),(x+w*.99,y+h*.62)],fill=(255,120,30))
        d.ellipse([x+w*.44,y+h*.18,x+w*.56,y+h*.30],fill=(255,140,40))
    elif k=='chart':
        d.rectangle([x,y,x+w,y+h],fill=(245,247,250)); d.line([x+6,y+h-10,x+w-4,y+h-10],fill=GREY,width=1); d.line([x+6,y+6,x+6,y+h-10],fill=GREY,width=1)
        d.line([x+6,y+h*.42,x+w-4,y+h*.42],fill=RED,width=2); d.text((x+8,y+h*.48),'50,000',font=F(SANSB,9),fill=RED)
        pts=[(x+8,y+h*.80),(x+w*.25,y+h*.72),(x+w*.45,y+h*.76),(x+w*.62,y+h*.55),(x+w*.78,y+h*.42),(x+w*.95,y+h*.18)]
        d.line(pts,fill=(20,140,70),width=3); d.ellipse([x+w*.93,y+h*.14,x+w*.97,y+h*.22],fill=(20,140,70)); d.text((x+w*.55,y+h*.06),'50,018',font=F(SANSB,11),fill=(20,140,70))
    elif k=='server':
        d.rectangle([x,y,x+w,y+h],fill=(24,24,32))
        for c in range(3):
            d.rectangle([x+w*(.08+c*.30),y+6,x+w*(.08+c*.30)+w*.24,y+h-6],fill=(52,56,68))
            for r in range(4): d.rectangle([x+w*(.11+c*.30),y+10+r*12,x+w*(.11+c*.30)+w*.18,y+10+r*12+6],fill=(200,60,50) if r%2 else (60,180,90))
        d.rectangle([x,y+h*.70,x+w,y+h*.92],fill=(178,34,34)); d.text((x+w*.22,y+h*.74),'CODE RED',font=F(SANSB,12),fill='white')
    elif k=='heli':
        d.rectangle([x,y,x+w,y+h*.70],fill=(190,215,235)); d.polygon([(x,y+h),(x+w*.30,y+h*.45),(x+w*.55,y+h),(x+w*.30,y+h)],fill=(120,140,120)); d.polygon([(x+w*.45,y+h),(x+w*.75,y+h*.40),(x+w,y+h)],fill=(90,115,95))
        d.ellipse([x+w*.30,y+h*.28,x+w*.55,y+h*.44],fill=(70,80,95)); d.rectangle([x+w*.55,y+h*.34,x+w*.78,y+h*.40],fill=(70,80,95)); d.rectangle([x+w*.76,y+h*.30,x+w*.80,y+h*.44],fill=(70,80,95))
        d.line([x+w*.18,y+h*.24,x+w*.68,y+h*.24],fill=(50,55,65),width=2); d.ellipse([x+w*.40,y+h*.44,x+w*.46,y+h*.50],fill=(50,55,65))
    elif k=='store':
        d.rectangle([x,y,x+w,y+h],fill=(240,235,225)); d.rectangle([x,y,x+w,y+h*.22],fill=(178,34,34))
        for i in range(5): d.polygon([(x+i*w*.20,y+h*.22),(x+(i+1)*w*.20,y+h*.22),(x+(i+.5)*w*.20,y+h*.34)],fill=(255,255,255) if i%2 else (178,34,34))
        d.rectangle([x+w*.10,y+h*.40,x+w*.90,y+h*.92],fill=(200,195,185)); d.rectangle([x+w*.42,y+h*.55,x+w*.58,y+h*.92],fill=(90,90,100))
        d.text((x+w*.14,y+h*.44),'MARKET',font=F(SANSB,10),fill=INK); d.rectangle([x+w*.68,y+h*.66,x+w*.88,y+h*.80],fill=(40,120,200))
    elif k=='desert':
        d.rectangle([x,y,x+w,y+h*.60],fill=(240,220,170)); d.rectangle([x,y+h*.60,x+w,y+h],fill=(214,178,110))
        d.ellipse([x+w*.70,y+h*.08,x+w*.86,y+h*.24],fill=(255,220,120)); d.polygon([(x,y+h*.62),(x+w*.40,y+h*.42),(x+w*.80,y+h*.62)],fill=(226,196,130))
        d.line([x+w*.10,y+h*.86,x+w*.90,y+h*.78],fill=(120,90,60),width=3)
        for i in range(3): d.rectangle([x+w*(.18+i*.22),y+h*.70,x+w*(.18+i*.22)+w*.12,y+h*.78],fill=(90,70,50))
        d.text((x+w*.60,y+h*.16),'60 KM',font=F(SANSB,10),fill=(150,60,20))
    elif k=='truck':
        d.rectangle([x,y,x+w,y+h],fill=(225,225,220)); d.rectangle([x,y+h*.72,x+w,y+h],fill=(90,90,95))
        d.rectangle([x+w*.08,y+h*.42,x+w*.48,y+h*.72],fill=(60,90,140)); d.rectangle([x+w*.48,y+h*.50,x+w*.66,y+h*.72],fill=(200,200,195))
        d.ellipse([x+w*.16,y+h*.68,x+w*.22,y+h*.76],fill=INK); d.ellipse([x+w*.52,y+h*.68,x+w*.58,y+h*.76],fill=INK)
        d.polygon([(x+w*.70,y+h*.42),(x+w*.80,y+h*.26),(x+w*.88,y+h*.42)],fill=(255,140,40)); d.ellipse([x+w*.74,y+h*.30,x+w*.88,y+h*.46],fill=(255,200,60))
    elif k=='rocket':
        d.rectangle([x,y,x+w,y+h],fill=(12,18,44)); stars(d,x,y,w,h,12)
        d.rectangle([x+w*.44,y+h*.18,x+w*.56,y+h*.62],fill=(235,235,230)); d.polygon([(x+w*.44,y+h*.18),(x+w*.56,y+h*.18),(x+w*.50,y+h*.04)],fill=(200,40,40))
        d.rectangle([x+w*.38,y+h*.44,x+w*.44,y+h*.56],fill=(200,40,40)); d.rectangle([x+w*.56,y+h*.44,x+w*.62,y+h*.56],fill=(200,40,40))
        d.polygon([(x+w*.46,y+h*.62),(x+w*.54,y+h*.62),(x+w*.50,y+h*.86)],fill=(255,180,60)); d.ellipse([x+w*.70,y+h*.14,x+w*.92,y+h*.30],fill=(180,190,210))
        d.text((x+w*.06,y+h*.80),'TIANGONG',font=F(SANSB,9),fill='white')
HERO=[(1,'RIYADH','MIDDLE EAST','CONFIRMED','#1a7a3a','Houthi drone hits Riyadh\u2019s tallest tower again, 11 hurt','A Houthi drone hits the PIF tower, Riyadh\u2019s tallest, for the second time in a week. At least 11 are hurt: 2 Saudis, 2 Indians, 3 Nepalis and 4 Egyptians.','tower','Reuters \u00b7 AP'),(2,'SHANGHAI','ASIA','OFFICIAL','#1d4fa3','China probes Shanghai party chief Chen Jining','Shanghai party chief Chen Jining, 62, is probed for \u201cserious violations\u201d. He is the fourth Politburo member to fall under investigation this year.','gate','CCDI'),(3,'NEW YORK','US / TECH','CONFIRMED','#1a7a3a','Huawei guilty on 10 of 12 counts','A US jury finds Huawei guilty on 10 of 12 counts, including trade-secret theft and bank fraud. It is cleared of racketeering; sentencing is Sep 2027.','court','US court \u00b7 Reuters')]
CARDS=[(4,'ZAPORIZHZHIA','EUROPE / WAR','REPORTED','#5a6b7d','Russian attacks kill 9 across Ukraine in a day','Strikes kill 9, wound 81 in a day. Of 96 drones, 73 are shot down.','drones','Kyiv officials'),(5,'CAS','AFRICA / SPORT','OFFICIAL','#1d4fa3','CAS hands Senegal back the AFCON title','CAS hands Senegal the title back; Morocco forfeit 3\u20130, Senegal win 1\u20130.','trophy','CAS'),(6,'HORMUZ','MIDDLE EAST','REPORTED','#5a6b7d','IRGC attacks container ship in Hormuz','IRGC attack hits a container ship at 18:58 UTC. Navigation is disabled.','ship','UKMTO'),(7,'NEW YORK','WORLD / MARKETS','CONFIRMED','#1a7a3a','Dow closes above 50,000 for the first time','Dow closes at 50,018, first above 50,000. Taiex jumps a record +8.99%.','chart','Market close'),(8,'REDMOND','WORLD / TECH','REPORTED','#5a6b7d','Microsoft declares \u2018Code Red\u2019 after historic outage','Microsoft declares \u2018Code Red\u2019 after a 24-hour outage. Recovery in 1 hour.','server','Reuters'),(9,'ESKISEHIR','EUROPE','REPORTED','#5a6b7d','Turkish military helicopter crash kills 5','A Turkish military AS-532 helicopter crashes in Eskisehir, killing 5.','heli','Turkish officials'),(10,'CARTAGENA','AMERICAS','REPORTED','#5a6b7d','Supermarket hostages: 25 held in Cartagena','Gunmen hold 25 hostages in Cartagena. Five elderly women are freed.','store','Colombian officials'),(11,'ADEN','MIDDLE EAST','REPORTED','#5a6b7d','Houthis advance within 60 km of Aden','Houthi forces advance to within 60 km of Aden. Reported at 16:51 UTC.','desert','Wires'),(12,'LAHJ','MIDDLE EAST','REPORTED','#5a6b7d','Saudi strikes kill 25, wound 6 in Yemen','Saudi strikes in Wadi Maabaq, Lahj, kill 25 and wound 6.','truck','Yemeni officials'),(13,'JIUQUAN','WORLD / SPACE','OFFICIAL','#1d4fa3','China names first foreign astronaut for Tiangong','Shenzhou-24 crew named; Pakistan\u2019s Ali is the first foreigner on Tiangong.','rocket','CMSA')]
ALSO=[(14,'Ankara','Haftar visits Turkey for first time','REP','#5a6b7d'),(15,'London','UK sanctions Houthis + 4 officials','OFF','#1d4fa3'),(16,'Villavicencio','Car bomb injures 23','REP','#5a6b7d'),(17,'Gaza','Israel kills Hamas security chief','REP','#5a6b7d'),(18,'Baghdad','Iraq takes control of Kurdish oilfields','OFF','#1d4fa3'),(19,'Gaza','Meningitis alert: 272 cases in Oct','OFF','#1d4fa3'),(20,'DR Congo','Missing Cessna 208, rebels claim shootdown','CLM','#c25e00'),(21,'Hanoi','Hot-pot blast kills \u22656','REP','#5a6b7d'),(22,'Gulf of Finland','Ukraine hits Russian ship Sparta II','REP','#5a6b7d'),(23,'Kuala Lumpur','Malaysia to return migrants to Myanmar','OFF','#1d4fa3'),(24,'Ulleungdo','S. Korea shelter order as jets enter ADIZ','OFF','#1d4fa3'),(25,'Dhaka','Hasina plans return 16 Dec','REP','#5a6b7d'),(26,'The Hague','14 nations back ICJ Myanmar ruling','REP','#5a6b7d'),(27,'Jakarta','Indonesia nominates 2 VP candidates','OFF','#1d4fa3'),(28,'Beijing','China sentences official Ma to death','OFF','#1d4fa3'),(29,'Brussels','NATO vows defence vs space threat','OFF','#1d4fa3'),(30,'Mexico City','US drone aided Fri 20 Nov Chapo capture','REP','#5a6b7d'),(31,'San Salvador','Bukele names 3 soldiers killed in Haiti','OFF','#1d4fa3'),(32,'Ottawa','Pentagon: only 41.9% of air fleet ready','REP','#5a6b7d'),(33,'Washington','US adds Megaspeed to blacklist','OFF','#1d4fa3'),(34,'Kyiv','Zelensky urges talks with Russia, US, EU','REP','#5a6b7d'),(35,'Ras Al Khaimah','UAE bus-truck crash kills 13','REP','#5a6b7d'),(36,'London','England record 5,258 heat deaths','OFF','#1d4fa3'),(37,'Kourou','Ariane 6 lofts 36 Amazon satellites','OFF','#1d4fa3'),(38,'Cikande','Factory-fire toll rises to 26','REP','#5a6b7d')]
UTC=[('02:15','NATO vows space defence'),('08:16','Hanoi hot-pot blast'),('10:42','Saudi strikes Yemen'),('14:27','Riyadh tower hit'),('16:51','Houthis 60 km from Aden'),('18:58','Hormuz ship attack'),('20:41','Huawei guilty')]
NUMS=[('11','hurt in Riyadh'),('9','killed in Ukraine'),('50,018','Dow, first close'),('+8.99%','Taiex record'),('25','killed / missing, Yemen'),('26','Cikande fire toll'),('10/12','Huawei counts'),('96','drones at Ukraine')]
CONT=[('-168,66 -165,60 -158,58 -152,60 -140,60 -135,58 -130,54 -125,49 -124,42 -120,34 -114,29 -110,24 -105,20 -97,16 -94,17 -90,14 -86,12 -83,9 -79,9 -81,13 -84,16 -87,21 -90,21 -97,26 -93,30 -89,30 -84,30 -81,26 -80,32 -76,35 -74,40 -70,42 -68,45 -65,44 -60,47 -55,52 -60,55 -65,58 -68,58 -72,62 -78,62 -85,66 -92,66 -95,69 -110,68 -125,70 -140,70 -155,71 -165,68'),('-58,64 -52,60 -43,60 -40,64 -32,68 -22,70 -20,74 -25,78 -35,80 -55,80 -58,76 -60,70'),('-79,9 -77,4 -80,-3 -81,-6 -77,-12 -72,-18 -70,-23 -70,-30 -72,-37 -73,-44 -74,-52 -68,-55 -65,-50 -62,-42 -58,-35 -52,-32 -48,-28 -41,-23 -39,-17 -35,-9 -35,-6 -40,-3 -44,-2 -50,0 -53,4 -58,6 -62,9 -68,11 -72,12 -76,10'),('-6,35 -10,31 -15,27 -17,21 -17,15 -15,11 -13,8 -8,5 -4,5 0,6 6,4 9,4 9,-1 12,-5 13,-10 12,-17 14,-22 16,-28 19,-34 26,-34 32,-29 35,-24 40,-16 40,-10 42,-4 46,-1 51,2 51,11 44,11 40,15 38,18 37,22 35,28 32,31 30,32 22,33 11,34 10,37 5,37 -1,35'),('-10,36 -9,38 -9,43 -2,44 -1,46 -4,48 -1,50 2,51 5,53 8,55 8,57 10,59 5,60 5,62 10,64 12,66 18,69 25,71 30,70 35,68 40,68 45,68 55,69 65,69 75,72 85,74 95,76 105,77 115,73 125,72 135,72 145,72 155,70 162,66 170,66 178,65 178,62 170,60 162,60 158,56 155,52 150,59 142,55 142,50 140,45 138,40 135,35 132,33 130,35 127,35 126,38 124,40 122,38 120,32 122,28 120,24 118,25 110,21 108,18 105,10 104,9 103,7 100,8 98,10 98,14 97,16 95,16 93,18 91,22 89,22 88,22 86,20 85,19 83,17 80,15 80,10 77,8 76,10 75,13 73,16 72,20 70,23 68,23 66,25 62,25 58,25 57,26 56,27 54,27 52,28 50,29 49,30 48,30 47,30 44,29 43,27 41,22 40,20 39,21 38,24 35,28 34,28 36,31 36,36 33,36 30,36 27,37 26,38 23,36 22,37 19,40 16,40 15,44 12,44 10,44 8,44 6,43 3,42 0,39 -2,37 -6,36'),('113,-22 114,-28 115,-33 118,-35 124,-33 129,-32 132,-32 135,-35 138,-35 140,-38 145,-38 150,-37 153,-32 153,-27 150,-23 146,-19 142,-15 142,-11 137,-12 135,-15 132,-12 130,-13 126,-14 122,-17 118,-20')]
PINS=[(1,'Riyadh',24.7,46.7,-12,-12),(2,'Shanghai',31.2,121.5,0,-14),(3,'New York',40.7,-74.0,-22,-12),(4,'Zaporizhzhia',47.8,35.2,10,-14),(5,'Dakar',14.7,-17.4,0,12),(6,'Hormuz',26.6,56.3,20,14),(7,'New York',40.7,-74.0,22,10),(8,'Redmond',47.7,-122.1,0,-14),(9,'Eskisehir',39.8,30.5,-18,12),(10,'Cartagena',10.4,-75.5,0,12),(11,'Aden',12.8,45.0,-14,10),(12,'Lahj',13.0,44.9,14,-16),(13,'Jiuquan',39.7,98.5,0,-14)]
LEG=[(1,'Riyadh','Middle East','#b23a2e'),(2,'Shanghai','Asia','#c98a1b'),(3,'New York','Americas','#2e6b4f'),(4,'Zaporizhzhia','Europe','#2e4a8a'),(5,'Dakar','Africa','#7a4a8a'),(6,'Hormuz','Middle East','#b23a2e'),(7,'New York','Americas','#2e6b4f'),(8,'Redmond','World / Space','#5a6b7d'),(9,'Eskisehir','Europe','#2e4a8a'),(10,'Cartagena','Americas','#2e6b4f'),(11,'Aden','Middle East','#b23a2e'),(12,'Lahj','Middle East','#b23a2e'),(13,'Jiuquan','World / Space','#5a6b7d')]
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
d.text((24,6),'THE WORLD ON ONE DAY',font=F(SANSB,12),fill=RED); d.text((1000,6),'38 STORIES \u00b7 6 REGIONS \u00b7 13 FIELDS',font=F(SANSB,12),fill=INK,anchor='ra')
d.text((24,22),'Tuesday 24 November 2026',font=F(SERIF,30),fill=INK)
d.text((24,60),'Houthi drone hits Riyadh\u2019s tallest tower \u00b7 Shanghai party chief probed \u00b7 Huawei guilty on 10 of 12 counts',font=F(SERIF,12),fill=RED)
REG=[('EUROPE 9',9,'#2e4a8a'),('MIDDLE EAST 8',8,'#b23a2e'),('ASIA 8',8,'#c98a1b'),('AFRICA 2',2,'#7a4a8a'),('AMERICAS 7',7,'#2e6b4f'),('WORLD / SPACE 4',4,'#5a6b7d')]
rx=24
for t,n,c in REG:
    w=int(976*n/38); d.rectangle([rx,78,rx+w-2,96],fill=c); d.text((rx+w/2,82),t,font=F(SANSB,9),fill='white',anchor='ma'); rx+=w
d.text((24,102),'THE DAY IN UTC',font=F(SANSB,10),fill=RED)
for i,(t,ev) in enumerate(UTC):
    x=24+i*140; d.text((x,116),t,font=F(SANSB,11),fill=RED); [d.text((x,130),l,font=F(SANS,9),fill=INK) for l in wrap(d,ev,F(SANS,9),134)]
d.line([24,152,1000,152],fill=LINE,width=1)
d.text((24,158),'THE DAY IN NUMBERS',font=F(SANSB,10),fill=RED)
for i,(v,lab) in enumerate(NUMS):
    x=24+i*122; d.text((x,172),v,font=F(SANSB,19),fill=NAVY); [d.text((x,194),l,font=F(SANS,8),fill=GREY) for l in wrap(d,lab,F(SANS,8),116)]
d.line([24,212,1000,212],fill=LINE,width=1)
for i,(n,loc,reg,ch,cc,hl,dk,sk,src) in enumerate(HERO):
    x=24+i*326; w=318
    d.rectangle([x,220,x+w,392],outline=LINE,width=1); scene(d,x,220,w,80,sk)
    d.text((x+8,304),f'{n} {loc} \u00b7 {reg}',font=F(SANSB,10),fill=INK); chip(d,x+w-62,304,ch,cc)
    for j,l in enumerate(wrap(d,hl,F(SANSB,13),w-16)[:2]): d.text((x+8,318+j*15),l,font=F(SANSB,13),fill=INK)
    for j,l in enumerate(wrap(d,dk,F(SANS,10),w-16)[:3]): d.text((x+8,348+j*11),l,font=F(SANS,10),fill=(60,60,60))
    d.text((x+8,382),'('+src+')',font=F(SANS,8),fill=GREY)
for r in range(2):
    for c in range(5):
        n,loc,reg,ch,cc,hl,dk,sk,src=CARDS[r*5+c]; x=24+c*196; y=398+r*120; w=190
        d.rectangle([x,y,x+w,y+116],outline=LINE,width=1); scene(d,x,y,w,42,sk)
        d.text((x+6,y+46),f'{n} {loc} \u00b7 {reg}',font=F(SANSB,8),fill=INK)
        for j,l in enumerate(wrap(d,hl,F(SANSB,10),w-12)[:2]): d.text((x+6,y+58+j*12),l,font=F(SANSB,10),fill=INK)
        for j,l in enumerate(wrap(d,dk,F(SANS,9),w-12)[:2]): d.text((x+6,y+84+j*11),l,font=F(SANS,9),fill=(60,60,60))
        cw=chip(d,x+6,y+104,ch,cc,7); d.text((x+6+cw+4,y+106),src,font=F(SANS,7),fill=GREY)
d.text((24,640),'WHERE IT HAPPENED \u00b7 13 PLACES',font=F(SANSB,10),fill=RED)
MX,MY,MW,MH=24,656,430,170
d.rectangle([MX,MY,MX+MW,MY+MH],fill=(198,222,238),outline=LINE)
def LL(lon,lat): return (MX+(lon+170)/360*MW,MY+(84-lat)/142*MH)
for poly in CONT:
    pts=[LL(float(a),float(b)) for a,b in (p.split(',') for p in poly.split())]; d.polygon(pts,fill=(196,204,158),outline=(140,150,110))
for n,name,lat,lon,dx,dy in PINS:
    px,py=LL(lon,lat); qx,qy=px+dx,py+dy; d.line([px,py,qx,qy],fill=(110,110,110),width=1); d.ellipse([px-2,py-2,px+2,py+2],fill=RED)
    d.ellipse([qx-8,qy-8,qx+8,qy+8],fill=RED,outline='white',width=1); d.text((qx,qy),str(n),font=F(SANSB,8),fill='white',anchor='mm')
for i,(n,name,reg,c) in enumerate(LEG):
    x=470+(i//7)*275; y=656+(i%7)*16; d.ellipse([x,y+2,x+8,y+10],fill=c); d.text((x+12,y),f'{n} \u00b7 {name} \u2014 {reg}',font=F(SANS,10),fill=INK)
d.text((24,830),'ALSO ON TUESDAY 24 NOVEMBER \u2014 25 MORE STORIES',font=F(SANSB,10),fill=RED)
for i,(n,city,txt,cc,bg) in enumerate(ALSO):
    x=24+(i//9)*330; y=844+(i%9)*12; nx=d.textlength(str(n),font=F(SANSB,9)); d.text((x,y),str(n),font=F(SANSB,9),fill=RED)
    cw=chip(d,x+nx+4,y,cc,bg,7); cx=x+nx+4+cw+3; c2=d.textlength(city+': ',font=F(SANSB,9)); d.text((cx,y),city+': ',font=F(SANSB,9),fill=INK); d.text((cx+c2,y),txt,font=F(SANS,9),fill=(50,50,50))
d.rectangle([24,952,1000,1000],outline=RED,width=1)
dc=['Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC.','LEFT OUT (not 24 Nov): Hormuz mine claims (Mon 23 Nov) \u00b7 Nvidia brings back Huang (Mon 23 Nov) \u00b7 EU sanctions package 22 (Mon 23 Nov) \u00b7 COP31 ends no deal (Sun 22 Nov) \u00b7 corvette Merkury sinks (Sat 22 Nov) \u00b7 El Chapo Isidro arrested (Fri 20 Nov) \u00b7 Cikande fire starts (Sat 21 Nov) \u00b7 Trump hush-money appeal ruling (Mon 23 Nov) \u00b7 F1 Las Vegas GP (Sat 21 Nov) \u00b7 ATP Finals (Sun 22 Nov).','NOT YET: Shenzhou-24 launch (Wed 25 Nov 00:18 UTC) \u00b7 MPR session picks VP (11 Dec) \u00b7 Huawei sentencing (Sep 2027) \u00b7 Hasina returns (16 Dec).']
y=956
for t in dc:
    for l in wrap(d,t,F(SANS,9),960): d.text((30,y),l,font=F(SANS,9),fill=INK); y+=11
d.text((24,1004),'Sources: Reuters \u00b7 AP \u00b7 UKMTO \u00b7 CAS \u00b7 CCDI \u00b7 CMSA \u00b7 UKHSA \u00b7 wires.',font=F(SANS,8),fill=GREY)
d.text((24,1013),'CONFIRMED = 2+ outlets \u00b7 OFFICIAL = on record \u00b7 REPORTED = one outlet \u00b7 CLAIM = one side\u2019s claim. Scenes are drawn illustrations, not photographs.',font=F(SANS,8),fill=GREY)
os.makedirs(os.path.dirname(OUT),exist_ok=True); im.save(OUT); print('saved',OUT,os.path.getsize(OUT))
