import pandas as pd
import pymem


# 與遊戲連線
def connect(config: dict) -> tuple:
    try:
        mem = pymem.Pymem(config["game"])
        module = pymem.process.module_from_name(
            mem.process_handle, config["game"]
        ).lpBaseOfDll
        return (mem, module)
    except Exception:
        return (None, None)


# 取得記憶體位址
def get_addr(mem, base, offsets):
    addr = mem.read_int(base)
    for idx, offset in enumerate(offsets):
        if idx != len(offsets) - 1:
            addr = mem.read_int(addr + int(offset))
    addr = addr + int(offsets[-1])
    return addr


# 參數
config = {
    "base": 0x000CEB84,
    "game": "TTHDVD.exe",
    "table": pd.read_excel("database.xlsx"),
}

# 連線
(mem, module) = connect(config=config)

# 若連線成功，則嘗試作弊
# 道具(含錢, 藥草, 裝備等)，範圍在 [0x40(花無缺)or0x44(江小魚), 0x0]~[0x40(花無缺)or0x44(江小魚), 0x8E8]
if module:
    # 初始化
    tmp = list()
    # 逐一修改遊戲參數
    for idx, val in enumerate(range(0, 1804, 4)):
        # 偏移量
        offsets = [0x0 + val]
        # 記憶體位址 = 基址 + 偏移量
        addr = get_addr(mem=mem, base=module + config["base"], offsets=offsets)
        # 修改遊戲參數
        try:
            mem.write_int(addr, idx + 1)
        except Exception:
            # 如果是角色屬性寫入失敗，原因是目前劇情進度尚未獲得該角色的使用權
            # 在花無缺早期路線中，無法修改燕南天和憐星!
            print(f"{idx}-{val} 寫入失敗!")
        tmp.append({"addr": hex(0x0 + val), "amt": idx + 1})
    pd.DataFrame(tmp).to_excel("123.xlsx")
