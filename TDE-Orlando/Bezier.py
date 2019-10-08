from matplotlib import pyplot  as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches

def Bezier(p0:tuple,p1:tuple,ima:tuple):
    Path = mpath.Path

    fig, ax = plt.subplots()
    pp1 = mpatches.PathPatch(
        Path([p0, ima, p1],
             [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
        fc="none", transform=ax.transData)
    ax.add_patch(pp1)
