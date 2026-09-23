import zlib,struct,json,os,subprocess,sys
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
W={"00 - Index":1560,"01 - Parts":1720,"02 - Persona A - The New Yorker":3530,"03 - Persona B - Back from Europe":1360,"04 - Persona C - New User":2240,"05 - Wedge - Trip Forming":1360,"06 - Places - From Friends":920,"07 - Ledger and Decisions":3380}
os.makedirs('merged/shots',exist_ok=True)
procs=[]
for n,w in W.items():
    procs.append(subprocess.Popen([CH,'--headless=new','--force-device-scale-factor=1',f'--window-size={w},7000','--virtual-time-budget=8000','--hide-scrollbars',f'--screenshot=merged/shots/{n[:2]}.png',f'file://{os.getcwd()}/merged/{n}.dc.html'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL))
for p in procs: p.wait()
def rows(path):
    d=open(path,'rb').read(); p=8; idat=b''
    while p<len(d):
        l=struct.unpack('>I',d[p:p+4])[0]; t=d[p+4:p+8]; c=d[p+8:p+8+l]
        if t==b'IHDR': w,h,bd,ct=struct.unpack('>IIBB',c[:10])
        if t==b'IDAT': idat+=c
        p+=12+l
    raw=zlib.decompress(idat); bpp={2:3,6:4}[ct]; stride=w*bpp; prev=bytearray(stride); out=[]; q=0
    for y in range(h):
        f=raw[q]; line=bytearray(raw[q+1:q+1+stride]); q+=1+stride
        for i in range(stride):
            a=line[i-bpp] if i>=bpp else 0; b=prev[i]; cc=prev[i-bpp] if i>=bpp else 0
            if f==1: line[i]=(line[i]+a)&255
            elif f==2: line[i]=(line[i]+b)&255
            elif f==3: line[i]=(line[i]+(a+b)//2)&255
            elif f==4:
                pa=abs(b-cc);pb=abs(a-cc);pc=abs(a+b-2*cc)
                pr=a if pa<=pb and pa<=pc else (b if pb<=pc else cc); line[i]=(line[i]+pr)&255
        out.append(bytes(line)); prev=line
    return w,h,bpp,out
H=json.load(open('merged/heights.json')) if os.path.exists('merged/heights.json') else {}
for n in W:
    k=n[:2]; w,h,bpp,R=rows(f'merged/shots/{k}.png'); bg=R[h-1][:bpp]
    last=max(y for y in range(h) if any(R[y][x*bpp:x*bpp+bpp]!=bg for x in range(0,w,3)))
    H[k]=last+30; print(k,'ink ends',last)
json.dump(H,open('merged/heights.json','w'),indent=1)
