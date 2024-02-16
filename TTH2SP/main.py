import pandas as pd
import pymem


def get_pt(base, offsets):
    addr = mem.read_int(base)
    for idx, offset in enumerate(offsets):
        if idx != len(offsets) - 1:
            addr = mem.read_int(addr + int(offset))
    addr = addr + int(offsets[-1])
    return addr


base = 0x000F9C78
game = "TTH2SP.exe"
role = "江小魚"

match game:
    case "TTH2SP.exe":
        base = 0x000F9C78
        table = pd.read_excel("database.xlsx", sheet_name=game)
    case _:
        base = None


if base and not table.empty:
    is_role = table["role"] == role
    is_act = table["act"] == 1
    table = table.loc[is_role & is_act].copy()
    table["offset1"] = table["offset1"].apply(int, base=16)
    table["offset2"] = table["offset2"].apply(int, base=16)
    mem = pymem.Pymem(game)
    module = pymem.process.module_from_name(mem.process_handle, game).lpBaseOfDll

    # 道具(含錢, 藥草, 裝備等)，範圍在 [0x40(花無缺)or0x44(江小魚), 0x0]~[0x40(花無缺)or0x44(江小魚), 0x8E8]
    tmp = list()
    for idx, val in enumerate(range(0, 2284, 4)):
        offset = [0x44, 0x0 + val]
        mem.write_int(get_pt(module + base, offsets=offset), idx + 1)
        tmp.append({"addr": hex(0x0 + val), "amt": idx + 1})
    pd.DataFrame(tmp).to_excel("123.xlsx")

#     # ================== 屬性 ==================
#     for cat, group in table.groupby("cat"):
#         if cat not in [
#             "花無缺",
#             "江小魚",
#             "張菁",
#             "鐵心蘭",
#             "荷露",
#             "黑蜘蛛",
#             "軒轅三光",
#             "燕南天",
#             "憐星",
#         ]:
#             continue
#         group.reset_index(inplace=True)
#         print(f"【{cat}】")
#         try:
#             offsets = group.loc[0, ["offset1", "offset2"]].tolist()
#             mem.read_int(get_pt(module + base, offsets=offsets))
#         except pymem.exception.MemoryReadError:
#             is_cat = table["cat"] == cat
#             table.loc[is_cat, "activate"] = 0
#             print("尚未取得使用權")
#             print("=" * 20)
#             continue

#         for idx, row in group.iterrows():
#             if not row["act"]:
#                 print(f"{row['item']}: 已關閉")
#                 continue
#             offsets = row[["offset1", "offset2"]].tolist()
#             val = mem.read_int(get_pt(module + base, offsets=offsets))
#             print(f"{row['item']}: {val}")
#         print("=" * 20)

#     idx = 0
#     # ================== 錢 ==================
#     for _, row in table.iterrows():
#         if row["cat"] != "錢":
#             continue
#         print(f"【{row['item']}】")
#         offsets = row[["offset1", "offset2"]].tolist()
#         mem.write_int(get_pt(module + base, offsets=offsets), idx + 1)
#         print(f"{row['item']}: {idx + 1}")
#         print("=" * 20)
#         idx += 1

#     # ================== 武器 ==================
#     for _, row in table.iterrows():
#         if row["cat"] != "武器":
#             continue
#         print(f"【{row['item']}】")
#         offsets = row[["offset1", "offset2"]].tolist()
#         mem.write_int(get_pt(module + base, offsets=offsets), idx + 1)
#         print(f"{row['item']}: {idx + 1}")
#         print("=" * 20)
#         idx += 1

#     # ================== 甲 ==================
#     for _, row in table.iterrows():
#         if row["cat"] != "甲":
#             continue
#         print(f"【{row['item']}】")
#         offsets = row[["offset1", "offset2"]].tolist()
#         mem.write_int(get_pt(module + base, offsets=offsets), idx + 1)
#         print(f"{row['item']}: {idx + 1}")
#         print("=" * 20)
#         idx += 1

#     # ================== 靴 ==================
#     for _, row in table.iterrows():
#         if row["cat"] != "靴":
#             continue
#         print(f"【{row['item']}】")
#         offsets = row[["offset1", "offset2"]].tolist()
#         mem.write_int(get_pt(module + base, offsets=offsets), idx + 1)
#         print(f"{row['item']}: {idx + 1}")
#         print("=" * 20)
#         idx += 1

#     # ================== 藥草 ==================
#     for _, row in table.iterrows():
#         if row["cat"] != "藥草":
#             continue
#         print(f"【{row['item']}】")
#         offsets = row[["offset1", "offset2"]].tolist()
#         mem.write_int(get_pt(module + base, offsets=offsets), idx + 1)
#         print(f"{row['item']}: {idx + 1}")
#         print("=" * 20)
#         idx += 1

#     # ================== 醫療 ==================
#     for _, row in table.iterrows():
#         if row["cat"] != "醫療":
#             continue
#         print(f"【{row['item']}】")
#         offsets = row[["offset1", "offset2"]].tolist()
#         mem.write_int(get_pt(module + base, offsets=offsets), idx + 1)
#         print(f"{row['item']}: {idx + 1}")
#         print("=" * 20)
#         idx += 1

#     # ================== 戰鬥 ==================
#     for _, row in table.iterrows():
#         if row["cat"] != "戰鬥":
#             continue
#         print(f"【{row['item']}】")
#         offsets = row[["offset1", "offset2"]].tolist()
#         mem.write_int(get_pt(module + base, offsets=offsets), idx + 1)
#         print(f"{row['item']}: {idx + 1}")
#         print("=" * 20)
#         idx += 1

#     # ================== 暗器 ==================
#     for _, row in table.iterrows():
#         if row["cat"] != "暗器":
#             continue
#         print(f"【{row['item']}】")
#         offsets = row[["offset1", "offset2"]].tolist()
#         mem.write_int(get_pt(module + base, offsets=offsets), idx + 1)
#         print(f"{row['item']}: {idx + 1}")
#         print("=" * 20)
#         idx += 1

#     # ================== 道具 ==================
#     for _, row in table.iterrows():
#         if row["cat"] != "道具":
#             continue
#         print(f"【{row['item']}】")
#         offsets = row[["offset1", "offset2"]].tolist()
#         mem.write_int(get_pt(module + base, offsets=offsets), idx + 1)
#         print(f"{row['item']}: {idx + 1}")
#         print("=" * 20)
#         idx += 1

#     # ================== 秘笈 ==================
#     for _, row in table.iterrows():
#         if row["cat"] != "秘笈":
#             continue
#         print(f"【{row['item']}】")
#         offsets = row[["offset1", "offset2"]].tolist()
#         mem.write_int(get_pt(module + base, offsets=offsets), idx + 1)
#         print(f"{row['item']}: {idx + 1}")
#         print("=" * 20)
#         idx += 1
