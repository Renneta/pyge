from pygelib import Archive

#
# PackDat3 (.cab) as found in Onnakayo
#
class PackDat3Archive(Archive):
    name = "PackDat3"
    desc = "Onnakayo"
    sig = "PackDat3"
    header_fmt = "<8si"
    entry_fmt = "<256sii4x" # 268 total, 2nd i and 4x are the same?


