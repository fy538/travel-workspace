import zlib, struct, subprocess, os
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
def rows(p):
    d=open(p,'rb').read(); pos=8; idat=b''; w=h=0
    while pos < len(d):
        n=struct.unpack('>I', d[pos:pos+4])[0]; t=d[pos+4:pos+8]; c=d[pos+8:pos+8+n]
        if t==b'IHDR': w,h,bd,ct=struct.unpack('>IIBB', c[:10])
        if t==b'IDAT': idat+=c
        pos+=12+n
    bpp = 4 if ct==6 else 3
    raw=zlib.decompress(idat); stride=w*bpp+1; out=[]; prev=bytearray(w*bpp)
    for y in range(h):
        f=raw[y*stride]; line=bytearray(raw[y*stride+1:(y+1)*stride])
        if f==1:
            for i in range(bpp, w*bpp): line[i]=(line[i]+line[i-bpp])&255
        elif f==2:
            for i in range(w*bpp): line[i]=(line[i]+prev[i])&255
        elif f==3:
            for i in range(w*bpp): line[i]=(line[i]+((line[i-bpp] if i>=bpp else 0)+prev[i])//2)&255
        elif f==4:
            for i in range(w*bpp):
                a=line[i-bpp] if i>=bpp else 0; b=prev[i]; c=prev[i-bpp] if i>=bpp else 0
                p=a+b-c; pa=abs(p-a); pb=abs(p-b); pc=abs(p-c)
                line[i]=(line[i]+(a if pa<=pb and pa<=pc else b if pb<=pc else c))&255
        out.append(bytes(line)); prev=line
    return w,h,bpp,out
def ink_end(p):
    w,h,bpp,R=rows(p); bg=R[2][:bpp]
    for y in range(h-6,0,-1):
        if any(R[y][x*bpp:(x+1)*bpp]!=bg for x in range(0,w,5)): return y
    return h
def shot(src, w, h, out):
    subprocess.run([CH,'--headless=new','--force-device-scale-factor=1',f'--window-size={w},{h}','--virtual-time-budget=12000','--hide-scrollbars',f'--screenshot={out}',f'file://{os.path.abspath(src)}'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
def crop(src, W, H, x, y, w, h, out):
    wrap=os.path.join(os.path.dirname(src), '_wrap.html')
    open(wrap,'w').write(f'<html><body style="margin:0;overflow:hidden;width:{w}px;height:{h}px;position:relative;background:#F4F0E7"><iframe src="file://{os.path.abspath(src)}" style="position:absolute;left:{-x}px;top:{-y}px;width:{W}px;height:{H}px;border:0"></iframe></body></html>')
    subprocess.run([CH,'--headless=new','--force-device-scale-factor=1',f'--window-size={w},{h}','--virtual-time-budget=12000','--hide-scrollbars',f'--screenshot={out}',f'file://{os.path.abspath(wrap)}'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
