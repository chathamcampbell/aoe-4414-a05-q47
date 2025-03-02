# conv_ops.py
#
# Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p
#  Determine the output shape and operation count of a convolution layer
# Parameters:
# c_in: input channel count 
# h_in: input height count
# w_in: inout width count
# n_filt: number of filters in the convolution layer
# h_filt: filter height count
# w_filt: filter width count
# s: stride of convolution filters
# p: amount of padding on each of the four input map sides
# # Output:
# A description of the script output
# c_out: output channel count
# h_out: output height count
# w_out: output width count
# adds: number of additions performed
# muls: number of multiplications performed
#divs: number of divisions performed
#
# Written by Chatham Campbell
# Other contributors: None
#

# import Python modules

import sys # argv
import math

#initialize script arguments
c_in = float('nan') 
h_in = float('nan') 
w_in = float('nan') 
n_filt = float('nan')
h_filt = float('nan')
w_filt = float('nan')
s = float('nan')
p = float('nan')

#parse script arguments
if len(sys.argv)==9:
  c_in = int(sys.argv[1])
  h_in = int(sys.argv[2])
  w_in = int(sys.argv[3])
  n_filt = int(sys.argv[4])
  h_filt = int(sys.argv[5])
  w_filt = int(sys.argv[6])
  s = int(sys.argv[7])
  p = int(sys.argv[8])
else:
  print(\
   'Usage: '\
   'python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p'
  )
  exit()

# write script below this line

c_out = n_filt
h_out = ((h_in+(2.0*p) - h_filt)/s)+1.0
w_out = ((w_in + (2.0*p)- w_filt)/s)+1.0

adds = n_filt*h_out*w_out*c_in*h_filt*w_filt
muls = n_filt* h_out*w_out*c_in*h_filt*w_filt
divs = 0


print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed
#python3 conv_ops.py 3 30 30 4 3 3 1 0