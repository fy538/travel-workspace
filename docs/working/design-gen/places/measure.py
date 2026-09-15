"""Board height from the document itself: faster and safer than a tall screenshot (boards over ~12k px break the pixel scan)."""
import subprocess, re, os
CH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
def height(path, W):
    p = os.path.abspath(path)
    probe = open(p).read() + '<script>window.addEventListener("load",function(){var b=document.querySelector("[data-board]")||document.body;document.title="H="+Math.ceil(b.getBoundingClientRect().height)});setTimeout(function(){var b=document.querySelector("[data-board]")||document.body;document.title="H="+Math.ceil(b.getBoundingClientRect().height)},2500)</script>'
    t = p + '.probe.html'; open(t, 'w').write(probe)
    r = subprocess.run([CH, '--headless=new', '--disable-gpu', '--hide-scrollbars', f'--window-size={W},1200', '--virtual-time-budget=8000', '--dump-dom', f'file://{t}'], capture_output=True, text=True, timeout=300)
    os.remove(t)
    m = re.search(r'<title>H=(\d+)</title>', r.stdout)
    return int(m.group(1)) if m else None
