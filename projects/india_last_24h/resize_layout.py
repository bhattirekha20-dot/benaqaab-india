from pathlib import Path
p=Path(__file__).parent
f=p/'build_frames.py';s=f.read_text().replace('ImageFont, ImageOps','ImageFont, ImageOps, ImageFilter')
a=s.index('def bottom_panel(c):');b=s.index('def add_title',a)
s=s[:a]+'''def bottom_panel(c):
    ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
    for y in range(1330,H):
        alpha=int(220*min(1,(y-1330)/350))
        d.line((0,y,W,y),fill=(8,14,26,alpha))
    return Image.alpha_composite(c,ov)
'''+s[b:]
a=s.index('def source_card(');b=s.index('def data_card(',a)
s=s[:a]+'''def source_card(c,img_path,top=(70,290),max_size=(940,610),caption=''):
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
'''+s[b:]
# Align the static reference copy with the larger image layout as well.
s=s.replace('(70,1090,106,1097)','(70,1450,106,1457)').replace('(120,1068)','(120,1430)').replace('(70,1150)','(70,1490)').replace('headline,F(65)','headline,F(52)').replace('(70,1360)','(70,1630)').replace('sub,F(34)','sub,F(28)').replace('(60,1550,1020,1637)','(60,1770,1020,1845)').replace('(82,1575)','(82,1790)')
f.write_text(s)
f=p/'build_comp.py';s=f.read_text().replace('.copy{bottom:17%}', '.copy{bottom:6%;text-shadow:0 2px 6px #000}h1{font-size:clamp(22px,4.5vw,32px)}.sub{font-size:13px}.caption{bottom:3%}').replace('transition:opacity .55s ease,transform 1s cubic-bezier(.2,.8,.2,1)','transition:transform 1s cubic-bezier(.2,.8,.2,1)')
f.write_text(s)
