import pandas as pd
import pymem

import HuaWuQue

table_HWQ = HuaWuQue.init()
table_HWQ = pd.DataFrame(table_HWQ)


def get_pt(base, offsets):
    addr = mem.read_int(base)
    for offset in offsets:
        if offset != offsets[-1]:
            addr = mem.read_int(addr + offset)
    addr = addr + offsets[-1]
    return addr


base = 0x000F9C78
mem = pymem.Pymem("TTH2SP.exe")
module = pymem.process.module_from_name(mem.process_handle, "TTH2SP.exe").lpBaseOfDll
for cat, group in table_HWQ.groupby("cat"):
    group.reset_index(inplace=True)
    print(f"【{cat}】")
    try:
        mem.read_int(get_pt(module + base, offsets=group.loc[0, "offset"]))
    except pymem.exception.MemoryReadError:
        print("尚未取得使用權")
        print("=" * 20)
        continue

    for idx, row in group.iterrows():
        if not row["activate"]:
            continue

        val = mem.read_int(get_pt(module + base, offsets=row["offset"]))
        print(f"{row['item']}: {val}")
    print("=" * 20)
# mem.write_int(get_pt(module + 0x000F9C78, offsets=offsets), 1234)
