from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter

ROOT=Path('/home/user/india_last_24h_short'); W,H=1080,1920
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; REG='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def F(n,bold=True): return ImageFont.truetype(FONT if bold else REG,n)
def wrap(draw,text,font,maxw):
    words=text.split(); lines=[]; cur=''
    for w in words:
        test=(cur+' '+w).strip()
        if not cur or draw.textbbox((0,0),test,font=font)[2] <= maxw: cur=test
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return '\n'.join(lines)
def textblock(draw,xy,text,font,fill,maxw,spacing=8,stroke=0,stroke_fill=None):
    s=wrap(draw,text,font,maxw); draw.multiline_text(xy,s,font=font,fill=fill,spacing=spacing,stroke_width=stroke,stroke_fill=stroke_fill); return draw.multiline_textbbox(xy,s,font=font,spacing=spacing,stroke_width=stroke)
def fit_img(path,size): return ImageOps.contain(Image.open(path).convert('RGB'),size,Image.Resampling.LANCZOS).convert('RGBA')
def make_base(path=None,color=(16,26,58,255)):
    if path: return ImageOps.fit(Image.open(ROOT/path).convert('RGB'),(W,H),Image.Resampling.LANCZOS,centering=(.5,.5)).convert('RGBA')
    return Image.new('RGBA',(W,H),color)
def common(c,no,label='NEWS DESK · 7 OCT 2026'):
    ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov); d.rectangle((0,0,W,210),fill=(16,26,58,120)); c=Image.alpha_composite(c,ov); d=ImageDraw.Draw(c)
    # Permanent channel branding: use the user's Benaqaab OS logo on every frame.
    logo=Image.open(ROOT/'source_images'/'benaqaab_os_logo.png').convert('RGBA')
    c.alpha_composite(logo,(55,30)); d=ImageDraw.Draw(c)
    d.text((70,112),label,font=F(19),fill=(255,211,91,255))
    # Scene counters are preview/debug metadata only and are intentionally not shown in the video.
    return c
def bottom_panel(c):
    ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
    for y in range(1330,H):
        alpha=int(220*min(1,(y-1330)/350))
        d.line((0,y,W,y),fill=(8,14,26,alpha))
    return Image.alpha_composite(c,ov)
def add_title(c,kicker,headline,sub,source='',official=False,visual_label=None):
    d=ImageDraw.Draw(c); gold=(255,211,91,255); white=(255,255,255,255); cyan=(227,250,255,255)
    d.rectangle((70,1450,106,1457),fill=(16,191,232,255)); d.text((120,1430),kicker,font=F(25),fill=gold)
    textblock(d,(70,1490),headline,F(52),white,940,spacing=7,stroke=1,stroke_fill=(16,26,58,160)); textblock(d,(70,1630),sub,F(28),cyan,930,spacing=7,stroke=1,stroke_fill=(16,26,58,160))
    if source:
        d.rounded_rectangle((60,1770,1020,1845),radius=8,fill=(16,26,58,200),outline=(240,173,36,255),width=3); d.text((82,1790),source,font=F(22),fill=white)
    tag=visual_label or ('OFFICIAL SOURCE IMAGE' if official else 'AI ILLUSTRATIVE VISUAL'); bb=d.textbbox((0,0),tag,font=F(17)); x=1008-(bb[2]-bb[0]+22); d.rounded_rectangle((x,1815,1008,1872),radius=5,fill=(16,26,58,205)); d.text((x+11,1830),tag,font=F(17),fill=white); return c
def source_card(c,img_path,top=(70,290),max_size=(940,610),caption=''):
    # Full, uncropped source image at maximum size, with image-derived backdrop.
    original=Image.open(ROOT/'source_images'/img_path).convert('RGB')
    back=ImageOps.fit(original,(W,H),Image.Resampling.LANCZOS).filter(ImageFilter.GaussianBlur(36)).convert('RGBA')
    back=Image.alpha_composite(back,Image.new('RGBA',(W,H),(0,0,0,115)))
    # Retain the permanent brand header already composited by common().
    back.paste(c.crop((0,0,W,160)),(0,0))
    im=ImageOps.contain(original,(1040,1200),Image.Resampling.LANCZOS).convert('RGBA')
    back.alpha_composite(im,((W-im.width)//2,180+(1200-im.height)//2))
    # Credit lives in the animated source line, not a duplicate image caption.
    return back
def data_card(c,top,title,rows,accent=(240,173,36,255)):
    x,y=top; w,h=940,600; d=ImageDraw.Draw(c); d.rounded_rectangle((x-10,y-10,x+w+10,y+h+10),radius=14,fill=(16,26,58,238),outline=accent,width=4); d.text((x+28,y+30),title,font=F(27),fill=(255,211,91,255)); yy=y+105
    for idx,row in enumerate(rows):
        d.rounded_rectangle((x+26,yy-10,x+w-26,yy+76),radius=8,fill=(255,255,255,235) if idx%2==0 else (227,250,255,235)); d.text((x+50,yy+12),row,font=F(31),fill=(16,26,58,255)); yy+=112
    return c

def save(c,n): c.convert('RGB').save(ROOT/f'render_frame_{n:02d}.jpg',quality=94)

# 1 — opening question
c=bottom_panel(common(make_base('scene_01_newsroom_hook.jpg'),1)); save(add_title(c,'INDIA LAST 24 HOURS','SABSE IMPORTANT KYA BADLA?','Vote row · ₹10,000 crore · earthquake · cricket','Verified snapshot · as of 7 October 2026'),1)
# 2 — public protest image, setup
c=common(make_base(None,(235,241,246,255)),2); c=source_card(c,'rahul_gandhi_protest_public.jpg',(70,280),(940,620),'Credit: Congress via The Indian Express · 6 Oct 2026'); c=bottom_panel(c); save(add_title(c,'DEMOCRACY · ECI ROW','WHAT HAPPENED?','Political parties marched; SIR and voter-roll objections remain ongoing','Public source image · The Indian Express report',visual_label='PUBLIC SOURCE IMAGE'),2)
# 3 — public ECI security image, official version
c=common(make_base(None,(235,241,246,255)),3); c=source_card(c,'eci_security_public.jpg',(70,290),(940,600),'Public image · ECI office security · 6 Oct 2026'); c=bottom_panel(c); save(add_title(c,'ECI OFFICIAL VERSION','PROTOCOL DISPUTE','ECI says no request before 4 PM; later a 240-MP delegation sought a meeting','ECI statement via PIB · 6 Oct 2026 · 9:44 PM',visual_label='PUBLIC SOURCE IMAGE'),3)
# 4 and 5 — two official PIB SME visuals
c=common(make_base(None,(224,241,252,255)),4); c=source_card(c,'sme_growth_fund_pib.jpg',(70,300),(940,600),'Official PIB infographic · 6 Oct 2026'); c=bottom_panel(c); save(add_title(c,'ECONOMY','₹10,000 CRORE SME FUND','Cabinet-approved growth equity plan for high-potential SMEs','Official PIB Cabinet factsheet',official=True),4)
c=common(make_base(None,(224,241,252,255)),5); c=source_card(c,'sme_growth_fund_pib_2.jpg',(70,300),(940,500),'Official PIB infographic · purpose of the fund'); c=bottom_panel(c); save(add_title(c,'SME FUND · PURPOSE','WHAT IS IT FOR?','Scale, technology, manufacturing and employment — not money already paid to every company','Official PIB factsheet · 6 Oct 2026',official=True),5)
# 6 — ITLA official PIB visual
c=common(make_base(None,(221,239,250,255)),6); c=source_card(c,'itla_pib.jpg',(70,285),(940,620),'Official PIB factsheet · 6 Oct 2026'); c=bottom_panel(c); save(add_title(c,'INFRASTRUCTURE','NEW TRANSPORT AUTHORITY','10-year-plus master plan · ₹500 crore-plus project appraisal','ITLA · official PIB factsheet',official=True),6)
# 7 — official Air Chief image
c=common(make_base(None,(27,72,108,255)),7); c=source_card(c,'air_chief_pib_2.jpeg',(250,265),(580,600),'Official PIB image · Ministry of Defence'); c=bottom_panel(c); save(add_title(c,'DEFENCE UPDATE','NEW AIR CHIEF · 31 OCT','Air Marshal Ashutosh Dixit will be the 29th Chief of the Air Staff','PIB Defence release · 6 Oct 2026',official=True),7)
# 8 and 9 — two official DRI images
c=common(make_base(None,(243,233,202,255)),8); c=source_card(c,'dri_gold_pib.jpg',(320,260),(440,600),'Official PIB image · DRI'); c=bottom_panel(c); save(add_title(c,'ENFORCEMENT','8.3 KG GOLD SEIZED','Foreign-origin gold valued at approximately ₹12.37 crore','DRI / Ministry of Finance via PIB · 6 Oct 2026',official=True),8)
c=common(make_base(None,(243,233,202,255)),9); c=source_card(c,'dri_gold_pib_2.jpg',(290,270),(500,600),'Official PIB image · DRI'); c=bottom_panel(c); save(add_title(c,'ENFORCEMENT','4 ARRESTED · PROBE ON','The DRI release says investigation into the network continues','Official DRI release via PIB · 6 Oct 2026',official=True),9)
# 10 — NCS public data
c=common(make_base('scene_07_quake_weather.jpg'),10); c=data_card(c,(70,255),'PUBLIC DATA · NCS',['REVIEWED MAGNITUDE 4.9 · CHAMOLI','6 OCT 2026 · 22:23:13 IST','NCS OFFICIAL EARTHQUAKE FEED']); c=bottom_panel(c); save(add_title(c,'EARTHQUAKE ALERT','M4.9 CHAMOLI','NCS recorded the event at 10:23 PM; no damage claim is added without official confirmation','NCS public feed · check local advisories',visual_label='PUBLIC DATA + AI VISUAL'),10)
# 11 — IMD public data
c=common(make_base('scene_10_weather.jpg'),11); c=data_card(c,(70,255),'PUBLIC DATA · IMD',['J&K · HIMACHAL · UTTARAKHAND','RAIN · THUNDERSTORM · GUSTY WINDS','CHECK DISTRICT-WISE WARNINGS']); c=bottom_panel(c); save(add_title(c,'WEATHER UPDATE','NORTHWEST ALERTS','IMD forecast covers parts of J&K, Himachal, Uttarakhand and nearby northwest areas','IMD bulletin · 6 Oct 2026',visual_label='PUBLIC DATA + AI VISUAL'),11)
# 12 and 13 — two official BCCI visuals
c=common(make_base(None,(31,42,73,255)),12); c=source_card(c,'bcci_match_highlights.jpg',(70,270),(940,520),'Official BCCI highlight thumbnail · 6 Oct 2026'); c=bottom_panel(c); save(add_title(c,'SPORTS','INDIA BEAT WI BY 8 WICKETS','India chased 171, reaching 172/2 in 14.4 overs at Lucknow','BCCI official scorecard + highlights · 6 Oct 2026',visual_label='PUBLIC SOURCE IMAGE + DATA'),12)
c=common(make_base(None,(31,42,73,255)),13); c=source_card(c,'bcci_super_sixes.jpg',(70,270),(940,520),'Official BCCI video thumbnail · Super Sixes'); c=bottom_panel(c); save(add_title(c,'OFFICIAL MATCH VIDEO','HIGHLIGHTS SOURCE ADDED','BCCI match highlights are linked in the source notes and description','Official BCCI video page · 6 Oct 2026',visual_label='PUBLIC VIDEO THUMBNAIL'),13)
# 14 — channel punchline
c=bottom_panel(common(make_base('scene_09_closing.jpg'),14,'THE LAST WORD')); save(add_title(c,'BENAQAAB INDIA','SHOR NAHI, SOURCE KE SAATH','Khabar tez ho sakti hai. Sach ki speed source se aati hai.','Follow for verified India explainers and roundups'),14)
# Preview backgrounds: rebuild clean visual layers without baked copy. The HTML
# preview animates the headline/subtitle exactly once over these backgrounds.
def save_preview(c,n):
    c.convert('RGB').save(ROOT/f'preview_bg_{n:02d}.jpg',quality=94)
def soft_bottom(c,start=900):
    # Keep the image visible beneath the text; darken progressively for legibility.
    ov=Image.new('RGBA',(W,H),(16,26,58,0)); od=ImageDraw.Draw(ov)
    for yy in range(start,H):
        a=int(35 + 190*((yy-start)/max(1,H-start)))
        od.line((0,yy,W,yy),fill=(16,26,58,a))
    return Image.alpha_composite(c,ov)
# Full-frame AI visuals remain visible, with a readable gradient under animated copy.
save_preview(soft_bottom(common(make_base('scene_01_newsroom_hook.jpg'),1),850),1)
save_preview(bottom_panel(source_card(common(make_base(None,(235,241,246,255)),2),'rahul_gandhi_protest_public.jpg',(70,280),(940,620),'Credit: Congress via The Indian Express · 6 Oct 2026')),2)
save_preview(bottom_panel(source_card(common(make_base(None,(235,241,246,255)),3),'eci_security_public.jpg',(70,290),(940,600),'Public image · ECI office security · 6 Oct 2026')),3)
save_preview(bottom_panel(source_card(common(make_base(None,(224,241,252,255)),4),'sme_growth_fund_pib.jpg',(70,300),(940,600),'Official PIB infographic · 6 Oct 2026')),4)
save_preview(bottom_panel(source_card(common(make_base(None,(224,241,252,255)),5),'sme_growth_fund_pib_2.jpg',(70,300),(940,500),'Official PIB infographic · purpose of the fund')),5)
save_preview(bottom_panel(source_card(common(make_base(None,(221,239,250,255)),6),'itla_pib.jpg',(70,285),(940,620),'Official PIB factsheet · 6 Oct 2026')),6)
save_preview(bottom_panel(source_card(common(make_base(None,(27,72,108,255)),7),'air_chief_pib_2.jpeg',(250,265),(580,600),'Official PIB image · Ministry of Defence')),7)
save_preview(bottom_panel(source_card(common(make_base(None,(243,233,202,255)),8),'dri_gold_pib.jpg',(320,260),(440,600),'Official PIB image · DRI')),8)
save_preview(bottom_panel(source_card(common(make_base(None,(243,233,202,255)),9),'dri_gold_pib_2.jpg',(290,270),(500,600),'Official PIB image · DRI')),9)
# Public earthquake/weather cards remain on their correct labelled background; no DRI
# or unrelated source image can bleed into these scenes.
p=common(make_base('scene_07_quake_weather.jpg'),10); p=data_card(p,(70,255),'PUBLIC DATA · NCS',['REVIEWED MAGNITUDE 4.9 · CHAMOLI','6 OCT 2026 · 22:23:13 IST','NCS OFFICIAL EARTHQUAKE FEED']); save_preview(bottom_panel(p),10)
p=common(make_base('scene_10_weather.jpg'),11); p=data_card(p,(70,255),'PUBLIC DATA · IMD',['J&K · HIMACHAL · UTTARAKHAND','RAIN · THUNDERSTORM · GUSTY WINDS','CHECK DISTRICT-WISE WARNINGS']); save_preview(bottom_panel(p),11)
save_preview(bottom_panel(source_card(common(make_base(None,(31,42,73,255)),12),'bcci_match_highlights.jpg',(70,270),(940,520),'Official BCCI highlight thumbnail · 6 Oct 2026')),12)
save_preview(bottom_panel(source_card(common(make_base(None,(31,42,73,255)),13),'bcci_super_sixes.jpg',(70,270),(940,520),'Official BCCI video thumbnail · Super Sixes')),13)
save_preview(soft_bottom(common(make_base('scene_09_closing.jpg'),14,'THE LAST WORD'),850),14)
print('14 frames and 14 clean animation backgrounds written')
