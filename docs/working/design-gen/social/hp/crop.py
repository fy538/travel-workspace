import subprocess, sys, os, json
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
from measure import W
def crop(name, x, y, w, h, out):
    H=json.load(open('merged/heights.json'))[name[:2]]
    src=os.path.abspath(f'merged/{name}.dc.html')
    wrap=f'merged/shots/_wrap.html'
    open(wrap,'w').write(f'<html><body style="margin:0;overflow:hidden;width:{w}px;height:{h}px;position:relative;background:#F4F0E7"><iframe src="file://{src}" style="position:absolute;left:{-x}px;top:{-y}px;width:{W[name]}px;height:{H}px;border:0"></iframe></body></html>')
    subprocess.run([CH,'--headless=new','--force-device-scale-factor=1',f'--window-size={w},{h}','--virtual-time-budget=9000','--hide-scrollbars',f'--screenshot={out}',f'file://{os.path.abspath(wrap)}'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
if __name__=='__main__':
    name=sys.argv[1]; x,y,w,h=map(int,sys.argv[2:6]); crop(name,x,y,w,h,sys.argv[6])
