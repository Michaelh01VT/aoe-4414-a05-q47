# conv_ops.py
#
# Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p
# This script calculates the output shape and operation count of a convolution layer.
# Parameters:
# c_in: input channel count
# h_in: input height count
# w_in: input width count
# n_filt: number of filters in the convolution layer
# h_filt: filter height count
# w_filt: filter width count
# s: stride of convolution filters
# p: amount of padding on each of the four input map sides
# Output:
# The script prints the following values:
# - Output channel count
# - Output height count
# - Output width count
# - Number of additions performed
# - Number of multiplications performed
# - Number of divisions performed
#
# Written by Michael Hoffman
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

import sys

# Parse script arguments
if len(sys.argv) != 9:
    print('Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p')
    sys.exit(1)

c_in = int(sys.argv[1])
h_in = int(sys.argv[2])
w_in = int(sys.argv[3])
n_filt = int(sys.argv[4])
h_filt = int(sys.argv[5])
w_filt = int(sys.argv[6])
s = int(sys.argv[7])
p = int(sys.argv[8])

# Calculate output dimensions
h_out = (h_in - h_filt + 2 * p) // s + 1
w_out = (w_in - w_filt + 2 * p) // s + 1
c_out = n_filt

# Calculate the number of operations
muls = c_in * n_filt * h_out * w_out * h_filt * w_filt
adds = muls - c_in * n_filt * h_out * w_out
divs = 0

# Print the results
print(int(c_out))  # output channel count
print(int(h_out))  # output height count
print(int(w_out))  # output width count
print(int(adds))   # number of additions performed
print(int(muls))   # number of multiplications performed
print(int(divs))   # number of divisions performed
