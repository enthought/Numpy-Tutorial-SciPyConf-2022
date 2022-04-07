"""
© 2001-2021, Enthought, Inc.
All Rights Reserved. Use only permitted under license. Copying, sharing, redistributing or other unauthorized use strictly prohibited.
All trademarks and registered trademarks are the property of their respective owners.
Enthought, Inc.
200 W Cesar Chavez Suite 202
Austin, TX 78701
www.enthought.com


Filter Image
------------

Read in the "dc_metro" image and use an averaging filter
to "smooth" the image.  Use a "5 point stencil" where
you average the current pixel with its neighboring pixels::

              0 0 0 0 0 0 0
              0 0 0 x 0 0 0
              0 0 x x x 0 0
              0 0 0 x 0 0 0
              0 0 0 0 0 0 0

Plot the image, the smoothed image, and the difference between the
two.

Bonus
~~~~~

Re-filter the image by passing the result image through the filter again. Do
this 50 times and plot the resulting image.

See :ref:`filter-image-solution`.
"""

import matplotlib.pyplot as plt

img = plt.imread('dc_metro.png')

plt.imshow(img, cmap=plt.cm.hot)
plt.show()
