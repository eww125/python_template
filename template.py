from time import time
t = time()

import os
home_dir =  os.path.expanduser('~')
cwd = os.getcwd()





print "complete!"
print "Time elapsed: " + str(time() - t) + " s."
