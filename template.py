from time import time
t = time()

import os
home_dir =  os.path.expanduser('~')
directory_path = home_dir + "/qgis_files/styles/"
print directory_path





print "complete!"
print "Time elapsed: " + str(time() - t) + " s."
