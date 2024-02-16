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

# idx = 0
# # ================== 錢 ==================
# for _, row in table_HWQ.iterrows():
#     if row["cat"] != "錢":
#         continue
#     print(f"【{row['item']}】")
#     if not row["activate"]:
#         print(f"{row['item']}: 已關閉")
#         continue
#     mem.write_int(get_pt(module + base, offsets=row["offset"]), idx + 1)
#     print(f"{row['item']}: {idx + 1}")
#     print("=" * 20)
#     idx += 1

# # ================== 秘笈 ==================
# for _, row in table_HWQ.iterrows():
#     if row["cat"] != "秘笈":
#         continue
#     print(f"【{row['item']}】")
#     if not row["activate"]:
#         print(f"{row['item']}: 已關閉")
#         continue
#     mem.write_int(get_pt(module + base, offsets=row["offset"]), idx + 1)
#     print(f"{row['item']}: {idx + 1}")
#     print("=" * 20)
#     idx += 1

# # ================== 藥草 ==================
# for _, row in table_HWQ.iterrows():
#     if row["cat"] != "藥草":
#         continue
#     print(f"【{row['item']}】")
#     if not row["activate"]:
#         print(f"{row['item']}: 已關閉")
#         continue
#     mem.write_int(get_pt(module + base, offsets=row["offset"]), idx + 1)
#     print(f"{row['item']}: {idx + 1}")
#     print("=" * 20)
#     idx += 1

# # ================== 刀 ==================
# for _, row in table_HWQ.iterrows():
#     if row["cat"] != "刀":
#         continue
#     print(f"【{row['item']}】")
#     if not row["activate"]:
#         print(f"{row['item']}: 已關閉")
#         continue
#     mem.write_int(get_pt(module + base, offsets=row["offset"]), idx + 1)
#     print(f"{row['item']}: {idx + 1}")
#     print("=" * 20)
#     idx += 1

# # ================== 劍 ==================
# for _, row in table_HWQ.iterrows():
#     if row["cat"] != "劍":
#         continue
#     print(f"【{row['item']}】")
#     if not row["activate"]:
#         print(f"{row['item']}: 已關閉")
#         continue
#     mem.write_int(get_pt(module + base, offsets=row["offset"]), idx + 1)
#     print(f"{row['item']}: {idx + 1}")
#     print("=" * 20)
#     idx += 1

# # ================== 鞭 ==================
# for _, row in table_HWQ.iterrows():
#     if row["cat"] != "鞭":
#         continue
#     print(f"【{row['item']}】")
#     if not row["activate"]:
#         print(f"{row['item']}: 已關閉")
#         continue
#     mem.write_int(get_pt(module + base, offsets=row["offset"]), idx + 1)
#     print(f"{row['item']}: {idx + 1}")
#     print("=" * 20)
#     idx += 1

# # ================== 甲 ==================
# for _, row in table_HWQ.iterrows():
#     if row["cat"] != "甲":
#         continue
#     print(f"【{row['item']}】")
#     if not row["activate"]:
#         print(f"{row['item']}: 已關閉")
#         continue
#     mem.write_int(get_pt(module + base, offsets=row["offset"]), idx + 1)
#     print(f"{row['item']}: {idx + 1}")
#     print("=" * 20)
#     idx += 1

# # ================== 靴 ==================
# for _, row in table_HWQ.iterrows():
#     if row["cat"] != "靴":
#         continue
#     print(f"【{row['item']}】")
#     if not row["activate"]:
#         print(f"{row['item']}: 已關閉")
#         continue
#     mem.write_int(get_pt(module + base, offsets=row["offset"]), idx + 1)
#     print(f"{row['item']}: {idx + 1}")
#     print("=" * 20)
#     idx += 1

# # ================== 弓 ==================
# for _, row in table_HWQ.iterrows():
#     if row["cat"] != "弓":
#         continue
#     print(f"【{row['item']}】")
#     if not row["activate"]:
#         print(f"{row['item']}: 已關閉")
#         continue
#     mem.write_int(get_pt(module + base, offsets=row["offset"]), idx + 1)
#     print(f"{row['item']}: {idx + 1}")
#     print("=" * 20)
#     idx += 1

# # ================== 醫療 ==================
# for _, row in table_HWQ.iterrows():
#     if row["cat"] != "醫療":
#         continue
#     print(f"【{row['item']}】")
#     if not row["activate"]:
#         print(f"{row['item']}: 已關閉")
#         continue
#     mem.write_int(get_pt(module + base, offsets=row["offset"]), idx + 1)
#     print(f"{row['item']}: {idx + 1}")
#     print("=" * 20)
#     idx += 1

# # ================== 暗器 ==================
# for _, row in table_HWQ.iterrows():
#     if row["cat"] != "暗器":
#         continue
#     print(f"【{row['item']}】")
#     if not row["activate"]:
#         print(f"{row['item']}: 已關閉")
#         continue
#     mem.write_int(get_pt(module + base, offsets=row["offset"]), idx + 1)
#     print(f"{row['item']}: {idx + 1}")
#     print("=" * 20)
#     idx += 1

# # ================== 道具 ==================
# for _, row in table_HWQ.iterrows():
#     if row["cat"] != "道具":
#         continue
#     print(f"【{row['item']}】")
#     if not row["activate"]:
#         print(f"{row['item']}: 已關閉")
#         continue
#     mem.write_int(get_pt(module + base, offsets=row["offset"]), idx + 1)
#     print(f"{row['item']}: {idx + 1}")
#     print("=" * 20)
#     idx += 1

# 道具(含錢, 藥草, 裝備等)，範圍在 [0x40, 0x0]~[0x40, 0x8E8]
tmp = list()
for idx, val in enumerate(range(0, 2284, 4)):
    offset = [0x40, 0x0 + val]
    mem.write_int(get_pt(module + base, offsets=offset), idx + 1)
    tmp.append({"addr": hex(0x0 + val), "amt": idx + 1})
pd.DataFrame(tmp).to_excel("123.xlsx")
