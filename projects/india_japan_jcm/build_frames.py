from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path('/home/user/india_japan_jcm_short')
W, H = 1080, 1920
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

scenes = [
    ('scene_01_climate_bridge.jpg', 'INDIA-JAPAN JCM', 'CREDIT KISE MILEGA?', 'Kya ek emission cut do baar count ho sakta hai?', ''),
    ('scene_02_timeline.jpg', 'THE MECHANISM', 'ARTICLE 6.2', 'Investment + clean technology + verified cuts', 'PIB · MoC 2025'),
    ('scene_03_clean_project.jpg', 'HOW A CREDIT STARTS', 'REFERENCE - PROJECT', 'A conservative baseline meets real project data', 'MoEFCC · Rules of Implementation'),
    ('scene_04_emission_baseline.jpg', 'BEFORE CREDIT', 'VERIFY BEFORE YOU TRADE', 'Joint Committee + third-party verification', 'MoEFCC · Rules of Implementation'),
    ('scene_05_verification_registry.jpg', 'THE ACCOUNTING GUARDRAIL', 'NO DOUBLE COUNTING', 'Two registries. Corresponding adjustments.', 'MoEFCC · Rules of Implementation'),
    ('scene_06_climate_question.jpg', 'THE BIG QUESTION', 'REAL PROJECTS. REAL DATA.', 'Climate finance or carbon accounting risk?', ''),
]

def font(size): return ImageFont.truetype(FONT, size)
def wrap(draw, text, fnt, max_width):
    words = text.split()
    lines=[]; cur=''
    for word in words:
        test=(cur+' '+word).strip()
        if draw.textbbox((0,0),test,font=fnt)[2] <= max_width or not cur:
            cur=test
        else:
            lines.append(cur); cur=word
    if cur: lines.append(cur)
    return lines

def draw_text_block(draw, xy, text, fnt, fill, max_width, spacing=8, stroke=0, stroke_fill=None):
    x,y=xy; lines=wrap(draw,text,fnt,max_width)
    draw.multiline_text((x,y),'\n'.join(lines),font=fnt,fill=fill,spacing=spacing,stroke_width=stroke,stroke_fill=stroke_fill)
    bbox=draw.multiline_textbbox((x,y),'\n'.join(lines),font=fnt,spacing=spacing,stroke_width=stroke)
    return bbox

for i,(img,kicker,headline,sub,source) in enumerate(scenes,1):
    base=Image.open(ROOT/img).convert('RGB')
    base=ImageOps.fit(base,(W,H),method=Image.Resampling.LANCZOS,centering=(0.5,0.5))
    canvas=base.convert('RGBA')
    shade=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(shade)
    d.rectangle((0,0,W,220),fill=(16,26,58,75))
    d.rectangle((0,930,W,H),fill=(16,26,58,215))
    canvas=Image.alpha_composite(canvas,shade)
    d=ImageDraw.Draw(canvas)
    white=(255,255,255,255); gold=(255,211,91,255); cyan=(227,250,255,255); indigo=(16,26,58,255)
    # brand and scene number
    d.text((76,68),'BENAQAAB INDIA',font=font(28),fill=white,stroke_width=1,stroke_fill=(16,26,58,140))
    no=f'{i:02d} / 06'; bb=d.textbbox((0,0),no,font=font(25)); d.text((1004-(bb[2]-bb[0]),70),no,font=font(25),fill=white,stroke_width=1,stroke_fill=(16,26,58,140))
    # bottom text stack
    d.rectangle((76,1094,110,1100),fill=(16,191,232,255))
    d.text((124,1078),kicker,font=font(27),fill=gold)
    draw_text_block(d,(76,1170),headline,font(72),white,940,spacing=8,stroke=1,stroke_fill=(16,26,58,110))
    draw_text_block(d,(76,1375),sub,font(37),cyan,900,spacing=7,stroke=1,stroke_fill=(16,26,58,110))
    if source:
        d.rounded_rectangle((68,1548,1012,1638),radius=7,fill=(16,26,58,190),outline=(240,173,36,255),width=3)
        draw_text_block(d,(88,1570),source,font(23),white,880,spacing=5)
    # illustrative-label pill
    label='AI ILLUSTRATIVE VISUAL'; bb=d.textbbox((0,0),label,font=font(17)); x=1000-(bb[2]-bb[0]+20)
    d.rounded_rectangle((x,1818,1000,1875),radius=4,fill=(16,26,58,195)); d.text((x+10,1831),label,font=font(17),fill=white)
    out=ROOT/f'render_frame_{i:02d}.jpg'
    canvas.convert('RGB').save(out,quality=94,optimize=True)
    print(out)
