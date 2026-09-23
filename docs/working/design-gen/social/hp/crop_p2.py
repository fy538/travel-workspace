import subprocess, os, json, sys
from measure import CH
from measure_p2 import W
H=json.load(open('places/heights.json'))
def crop(name,x,y,w,h,out):
    src=os.path.abspath(f'places/{name}.dc.html'); wrap='places/shots/_wrap.html'
    open(wrap,'w').write(f'<html><body style="margin:0;overflow:hidden;width:{w}px;height:{h}px;position:relative;background:#F4F0E7"><iframe src="file://{src}" style="position:absolute;left:{-x}px;top:{-y}px;width:{W[name]}px;height:{H[name[:2]]}px;border:0"></iframe></body></html>')
    subprocess.run([CH,'--headless=new','--force-device-scale-factor=1',f'--window-size={w},{h}','--virtual-time-budget=9000','--hide-scrollbars',f'--screenshot={out}',f'file://{os.path.abspath(wrap)}'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
if __name__=='__main__':
    n=sys.argv[1]; k=n[:2]; Wn=W[n]; h=H[k]; y=0; i=0
    while y<h:
        crop(n,0,y,Wn,min(1400,h-y),f'places/shots/{k}_{i}.png'); y+=1400; i+=1
    print('crops',i)
