import matplotlib.path as mpath
import matplotlib.patches as mpatches
from matplotlib import pyplot as plt

Path = mpath.Path
fig, ax = plt.subplots()

plt.xlim(0,10)
plt.ylim(0,8)
ponto1 = lambda pi,px,pf: mpatches.PathPatch(Path([pi, px, pf],[Path.MOVETO, Path.CURVE3, Path.CURVE3]),fc="none", transform=ax.transData)
ponto2 = lambda pi,px,px2,pf: mpatches.PathPatch(Path([pi, px, px2,pf],[Path.MOVETO, Path.CURVE4,  Path.CURVE4,Path.CURVE4]),fc="none", transform=ax.transData)

ax.add_patch(ponto2((0.783,0.512), (0.734, 1.789), (2.538, 0.8), (2.6, 1.789),))
plt.show()