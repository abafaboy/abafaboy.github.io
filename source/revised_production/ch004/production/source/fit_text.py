import os,math,re
from functools import lru_cache
from PIL import Image,ImageDraw,ImageFont
from fontTools.ttLib import TTFont
FONT=os.environ.get('ANIME_ACE_FONT');D=ImageDraw.Draw(Image.new('RGB',(1,1)))
@lru_cache(None)
def font_bundle(size):
 return ImageFont.truetype(FONT,round(size*2)),ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',round(size*2)),TTFont(FONT).getBestCmap()

def fit(text,w,h,size=31):
 font,fallback,cmap=font_bundle(size);words=text.split();pitch=size*1.35
 def width(s):
  s=re.sub(r"\bi(?=[’'….,!? ]|$)",'I',s.lower())
  return sum(D.textlength(c,font=font if ord(c) in cmap else fallback) for c in s)/2
 hh=(D.textbbox((0,0),'H',font=font)[3]-D.textbbox((0,0),'H',font=font)[1])/2
 for n in range(1,min(10,len(words))+1):
  total=(n-1)*pitch+hh
  if total+40>h:continue
  caps=[]
  for j in range(n):
   gy=-total/2+j*pitch;yy=max(abs(gy),abs(gy+hh))+13
   caps.append((w/2-14)*math.sqrt(max(0,1-(yy/(h/2))**2))*2)
  @lru_cache(None)
  def solve(k,j):
   if j==n:return (0,()) if k==len(words) else None
   choices=[]
   for e in range(k+1,len(words)-(n-j-1)+1):
    line=' '.join(words[k:e]);ww=width(line)
    if ww>caps[j]:break
    rest=solve(e,j+1)
    if rest:
     score=rest[0]+((caps[j]-ww)/max(1,caps[j]))**2
     choices.append((score,(line,)+rest[1]))
   return min(choices,key=lambda z:z[0]) if choices else None
  out=solve(0,0)
  if out:return list(out[1])
 raise ValueError((text,w,h,size,'No legal ellipse line partition'))
