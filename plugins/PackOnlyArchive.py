import struct
from pygelib import Archive

#
# PackOnly (.pd) as found in Cross Channel
#
# overrides "writeindex" to include padding (is this necessary?)
#
# unpack, repack, and data modification tested -- replacing 
# script and graphics works fine. Not quite binary compatible,
# because the original packer doesn't put things 100% in order
# (confirmed 2006/07/10)
# 
#
class PackOnlyArchive(Archive):
    name = "PackOnly (Cross Channel)"
    sig = "PackOnly"
    header_fmt = "<8s56xQ"
    entry_fmt = "<128sQQ"

    def writeindex(self, filelist):
        start = 64 + 8 + 144 * 16384

        for n in filelist:
            name = n
            length = os.stat(n).st_size
            self.file.write(struct.pack("<128sQQ", name, start, length))
            start = start + length

        self.file.write(struct.pack("%ix" % (144 * (16384 - len(filelist)))))



#
# PackPlus (.pd) as found in Cross Channel
#
# overrides "writeindex" to include padding (is this necessary?)
#
# unpack, repack, and data modification tested -- replacing 
# script and graphics works fine. Not quite binary compatible,
# because the original packer doesn't put things 100% in order
# (confirmed 2006/07/10)
# 
#
class PackPlusArchive(PackOnlyArchive):
    name = "PackPlus (Cross Channel)"
    sig = "PackPlus"

    def xorit(self, data):
        arr = array('B', data)
        for i in xrange(len(arr)) :
            arr[i] ^= 0xFF
        return arr.tostring()

    decrypt = xorit
    encrypt = xorit

