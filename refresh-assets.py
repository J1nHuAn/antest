from pathlib import Path
import base64, json
root = Path(__file__).resolve().parent
keys = ['puppy','cat','bear','panther','koala','fox','sheep','turtle']
images = {}
for key in keys:
    data = (root/'assets'/'animals'/(key+'.png')).read_bytes()
    images[key] = 'data:image/png;base64,' + base64.b64encode(data).decode('ascii')
(root/'assets'/'animals.js').write_text(
    '/* Auto-generated PNG data; refresh after replacing the original images. */\n'
    + 'window.GUANJI_ANIMALS=' + json.dumps(images,separators=(',',':')) + ';\n',
    encoding='utf-8')
print('Animal images updated. Reopen or refresh index.html.')
