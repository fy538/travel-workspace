import zlib,struct,json,os,subprocess,sys
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
W={"00 - Index":1560,"01 - Parts":1720,"02 - Persona A - The New Yorker":2620,"03 - Persona B - Back from Europe":1820,"04 - Persona C - New User":2700,"05 - Wedge - Trip Forming":1360,"06 - Places - From Friends":1820,"07 - Ledger and Decisions":3380,"08 - Seam with Life":2480,"09 - Forms":1560,"10 - States":2620,"11 - Return and Continuity":2200,"12 - Why This, Chat, and Degraded States":1820}
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
def ink_end(png):
    w,h,bpp,R=rows(png); bg=R[h-1][:bpp]
    return max(y for y in range(h) if any(R[y][x*bpp:x*bpp+bpp]!=bg for x in range(0,w,3)))
def shoot(src, out, w, h):
    subprocess.run([CH,'--headless=new','--force-device-scale-factor=1',f'--window-size={w},{h}','--virtual-time-budget=9000','--hide-scrollbars',f'--screenshot={out}',f'file://{os.path.abspath(src)}'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
if __name__=='__main__':
    names=sys.argv[1:]
    H=json.load(open('merged/heights.json'))
    for n in names: H[n[:2]]=0
    json.dump(H,open('merged/heights.json','w'),indent=1)
    [subprocess.run(['python3',g],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL) for g in ('gen_merge.py','gen_artifact.py','gen_states.py','gen_return.py')]
    procs=[]
    for n in names:
        procs.append(subprocess.Popen([CH,'--headless=new','--force-device-scale-factor=1',f'--window-size={W[n]},12000','--virtual-time-budget=9000','--hide-scrollbars',f'--screenshot=merged/shots/{n[:2]}.png',f'file://{os.getcwd()}/merged/{n}.dc.html'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL))
    for p in procs: p.wait()
    for n in names:
        e=ink_end(f'merged/shots/{n[:2]}.png'); H[n[:2]]=e+30; print(n[:2],'ink ends',e)
    json.dump(H,open('merged/heights.json','w'),indent=1)
    [subprocess.run(['python3',g],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL) for g in ('gen_merge.py','gen_artifact.py','gen_states.py','gen_return.py')]
    procs=[subprocess.Popen([CH,'--headless=new','--force-device-scale-factor=1',f'--window-size={W[n]},{H[n[:2]]}','--virtual-time-budget=9000','--hide-scrollbars',f'--screenshot=merged/shots/{n[:2]}.png',f'file://{os.getcwd()}/merged/{n}.dc.html'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL) for n in names]
    for p in procs: p.wait()
    print('final', {n[:2]:H[n[:2]] for n in names})
