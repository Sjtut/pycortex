"""
======================================================
Custom toppings you can add to `quickflat.make_figure`
======================================================

"""
import cortex

# Create a random pycortex Volume
volume = cortex.Volume.random(subject='S1', xfmname='retinotopy')

# Plot a flatmap with the data projected onto the surface
# By default ROIs and their labels will be overlaid to the plot
# Also a colorbar will be added
_ = cortex.quickflat.make_figure(volume, with_curvature=True)
