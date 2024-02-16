import time

import HuaWuQue
import pandas as pd
import pymem

table_HWQ = HuaWuQue.init_property()
table_HWQ = pd.DataFrame(table_HWQ)


def get_pt(base, offsets):
    addr = mem.read_int(base)
    for idx, offset in enumerate(offsets):
        if idx != len(offsets) - 1:
            addr = mem.read_int(addr + offset)
    addr = addr + offsets[-1]
    return addr


base = 0x000F9C78
mem = pymem.Pymem("TTH2SP.exe")
module = pymem.process.module_from_name(mem.process_handle, "TTH2SP.exe").lpBaseOfDll

# # ================== 屬性 ==================
# for cat, group in table_HWQ.groupby("cat"):
#     group.reset_index(inplace=True)
#     print(f"【{cat}】")
#     try:
#         mem.read_int(get_pt(module + base, offsets=group.loc[0, "offset"]))
#     except pymem.exception.MemoryReadError:
#         is_cat = table_HWQ["cat"] == cat
#         table_HWQ.loc[is_cat, "activate"] = 0
#         print("尚未取得使用權")
#         print("=" * 20)
#         continue

#     for idx, row in group.iterrows():
#         if not row["activate"]:
#             print(f"{row['item']}: 已關閉")
#             continue

#         val = mem.read_int(get_pt(module + base, offsets=row["offset"]))
#         print(f"{row['item']}: {val}")
#     print("=" * 20)

# ================== 秘笈 ==================
idx = 0
for _, row in table_HWQ.iterrows():
    if row["cat"] != "秘笈":
        continue
    print(f"【{row['item']}】")
    if not row["activate"]:
        print(f"{row['item']}: 已關閉")
        continue
    mem.write_int(get_pt(module + base, offsets=row["offset"]), idx + 1)
    print(f"{row['item']}: {idx + 1}")
    print("=" * 20)
    idx += 1

# ================== 藥草 ==================
idx = 0
for _, row in table_HWQ.iterrows():
    if row["cat"] != "藥草":
        continue
    print(f"【{row['item']}】")
    if not row["activate"]:
        print(f"{row['item']}: 已關閉")
        continue
    mem.write_int(get_pt(module + base, offsets=row["offset"]), idx + 1)
    print(f"{row['item']}: {idx + 1}")
    print("=" * 20)
    idx += 1

# ================== 刀 ==================
idx = 0
for _, row in table_HWQ.iterrows():
    if row["cat"] != "刀":
        continue
    print(f"【{row['item']}】")
    if not row["activate"]:
        print(f"{row['item']}: 已關閉")
        continue
    mem.write_int(get_pt(module + base, offsets=row["offset"]), idx + 1)
    print(f"{row['item']}: {idx + 1}")
    print("=" * 20)
    idx += 1

# for idx, val in enumerate(range(0, 128, 4)):
#     offset = [0x40, 0x4 + val]
#     mem.write_int(get_pt(module + base, offsets=offset), idx + 1)
