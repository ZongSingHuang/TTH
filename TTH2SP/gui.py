import tkinter as tk
from functools import partial

import pandas as pd
import pymem


class GuiApp:
    def __init__(self, master=None):
        # ============== 建立視窗 ==============
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(height=200, width=200)
        frame1 = tk.Frame(toplevel1)
        frame1.configure(height=600, width=1100)

        # ============== 參數 ==============
        self.config = {
            "base": 0x000F9C78,
            "game": "TTH2SP.exe",
            "table": pd.read_excel("database.xlsx"),
        }

        # ============== 選擇角色 ==============
        self.lab_msg1 = tk.Label(frame1, name="lab_msg1")
        self.lab_msg1.configure(text="角色")
        self.lab_msg1.place(anchor="nw", x=100, y=50)
        self.rad_JiangXiaoYu = tk.Radiobutton(frame1, name="rad_jiangxiaoyu")
        self.var_role = tk.StringVar(value="江小魚")
        self.rad_JiangXiaoYu.configure(
            text="江小魚", value="江小魚", variable=self.var_role
        )
        self.rad_JiangXiaoYu.place(anchor="nw", x=100, y=100)
        self.rad_HuaWuQue = tk.Radiobutton(frame1, name="rad_huawuque")
        self.rad_HuaWuQue.configure(
            text="花無缺", value="花無缺", variable=self.var_role
        )
        self.rad_HuaWuQue.place(anchor="nw", x=100, y=75)

        # ============== 錢 ==============
        self.btn_money = tk.Button(
            frame1,
            name="btn_money",
            command=partial(self.cheating, "錢", "錢", 99999),
        )

        self.btn_money.configure(foreground="#ff0000", text="金錢 99999")
        self.btn_money.place(anchor="nw", x=100, y=200)

        # ============== 藥草 ==============
        self.btn_herb = tk.Button(
            frame1,
            name="btn_herb",
            command=partial(self.cheating, "藥草", None, 99),
        )
        self.btn_herb.configure(text="藥草 99")
        self.btn_herb.place(anchor="nw", x=100, y=250)

        # ============== 秘笈 ==============
        self.btn_skill = tk.Button(frame1, name="btn_skill")
        self.btn_skill.configure(
            foreground="#ff0000",
            text="秘笈 6",
            command=partial(self.cheating, "秘笈", None, 6),
        )
        self.btn_skill.place(anchor="nw", x=300, y=200)

        # ============== 道具 ==============
        self.btn_tool = tk.Button(frame1, name="btn_tool")
        self.btn_tool.configure(
            foreground="#ff0000",
            text="道具 6",
            command=partial(self.cheating, "道具", None, 6),
        )
        self.btn_tool.place(anchor="nw", x=200, y=200)

        # ============== 藥品 ==============
        self.btn_medicine = tk.Button(
            frame1,
            name="btn_medicine",
            command=partial(self.cheating, "藥品", None, 99),
        )
        self.btn_medicine.configure(text="藥品 99")
        self.btn_medicine.place(anchor="nw", x=200, y=250)

        # ============== 毒藥 ==============
        self.btn_poison = tk.Button(
            frame1,
            name="btn_poison",
            command=partial(self.cheating, "毒藥", None, 99),
        )
        self.btn_poison.configure(text="毒藥 99")
        self.btn_poison.place(anchor="nw", x=300, y=250)

        # ============== 武器 ==============
        self.btn_weapon = tk.Button(
            frame1,
            name="btn_weapon",
            command=partial(self.cheating, "武器", None, 3),
        )
        self.btn_weapon.configure(foreground="#ff0000", text="武器 3")
        self.btn_weapon.place(anchor="nw", x=100, y=300)

        # ============== 衣服 ==============
        self.btn_armor = tk.Button(
            frame1,
            name="btn_armor",
            command=partial(self.cheating, "衣服", None, 3),
        )
        self.btn_armor.configure(foreground="#ff0000", text="衣服 3")
        self.btn_armor.place(anchor="nw", x=200, y=300)

        # ============== 靴子 ==============
        self.btn_boots = tk.Button(
            frame1,
            name="btn_boots",
            command=partial(self.cheating, "靴子", None, 3),
        )
        self.btn_boots.configure(foreground="#ff0000", text="靴子 3")
        self.btn_boots.place(anchor="nw", x=300, y=300)

        # ============== 血量 ==============
        self.btn_hp = tk.Button(
            frame1,
            name="btn_hp",
            command=partial(self.cheating, None, "生命", 9999),
        )
        self.btn_hp.configure(text="血量 9999")
        self.btn_hp.place(anchor="nw", x=200, y=350)

        # ============== 內力 ==============
        self.btn_mp = tk.Button(
            frame1,
            name="btn_mp",
            command=partial(self.cheating, None, "內力", 9999),
        )
        self.btn_mp.configure(text="內力 9999")
        self.btn_mp.place(anchor="nw", x=300, y=350)

        # ============== 等級 ==============
        self.btn_lv = tk.Button(
            frame1,
            name="btn_lv",
            command=partial(self.cheating, None, "等級", 99),
        )
        self.btn_lv.configure(text="等級 99")
        self.btn_lv.place(anchor="nw", x=100, y=350)

        # ============== 攻擊 ==============
        self.btn_str = tk.Button(
            frame1,
            name="btn_str",
            command=partial(self.cheating, None, "攻擊", 999),
        )
        self.btn_str.configure(text="攻擊 999")
        self.btn_str.place(anchor="nw", x=100, y=400)

        # ============== 防禦 ==============
        self.btn_def = tk.Button(
            frame1,
            name="btn_def",
            command=partial(self.cheating, None, "防禦", 999),
        )
        self.btn_def.configure(text="防禦 999")
        self.btn_def.place(anchor="nw", x=200, y=400)

        # ============== 反應 ==============
        self.btn_dex = tk.Button(
            frame1,
            name="btn_dex",
            command=partial(self.cheating, None, "反應", 999),
        )
        self.btn_dex.configure(text="反應 999")
        self.btn_dex.place(anchor="nw", x=300, y=400)

        # ============== 速度 ==============
        self.btn_agi = tk.Button(
            frame1,
            name="btn_agi",
            command=partial(self.cheating, None, "速度", 999),
        )
        self.btn_agi.configure(text="速度 999")
        self.btn_agi.place(anchor="nw", x=100, y=450)

        # ============== 智力 ==============
        self.btn_int = tk.Button(
            frame1,
            name="btn_int",
            command=partial(self.cheating, None, "智力", 999),
        )
        self.btn_int.configure(foreground="#ff0000", text="智力 999")
        self.btn_int.place(anchor="nw", x=200, y=450)

        # ============== 精元點數 ==============
        self.btn_pt = tk.Button(frame1, name="btn_pt")
        self.btn_pt.configure(
            foreground="#ff0000",
            text="精元點數 9999",
            command=partial(self.cheating, None, "精元點數", 9999),
        )
        self.btn_pt.place(anchor="nw", x=300, y=450)

        # ============== 其他 ==============
        self.lab_msg2 = tk.Label(frame1, name="lab_msg2")
        self.lab_msg2.configure(text="套用到所有角色")
        self.lab_msg2.place(anchor="nw", x=100, y=150)
        self.lab_msg3 = tk.Label(frame1, name="lab_msg3")
        self.lab_msg3.configure(text="客製化")
        self.lab_msg3.place(anchor="nw", x=500, y=150)
        self.lb_cat = tk.Listbox(frame1, name="lb_cat")
        self.lb_cat.place(anchor="nw", x=500, y=200)
        self.lb_item = tk.Listbox(frame1, name="lb_item")
        self.lb_item.place(anchor="nw", x=700, y=200)
        self.ent_read = tk.Entry(frame1, name="ent_read")
        self.ent_read.configure(state="readonly", width=10)
        self.ent_read.place(anchor="nw", x=900, y=200)
        self.btn_write = tk.Button(frame1, name="btn_write")
        self.btn_write.configure(text="修改")
        self.btn_write.place(anchor="nw", x=900, y=300)
        self.ent_write = tk.Entry(frame1, name="ent_write")
        self.ent_write.configure(width=10)
        self.ent_write.place(anchor="nw", x=900, y=250)
        self.lab_msg4 = tk.Label(frame1, name="lab_msg4")
        self.lab_msg4.configure(text="類別")
        self.lab_msg4.place(anchor="nw", x=500, y=175)
        self.lab_msg5 = tk.Label(frame1, name="lab_msg5")
        self.lab_msg5.configure(text="項目")
        self.lab_msg5.place(anchor="nw", x=700, y=175)
        self.lab_msg6 = tk.Label(frame1, name="lab_msg6")
        self.lab_msg6.configure(text="當前")
        self.lab_msg6.place(anchor="nw", x=900, y=175)
        self.lab_msg7 = tk.Label(frame1, name="lab_msg7")
        self.lab_msg7.configure(text="欲寫入")
        self.lab_msg7.place(anchor="nw", x=900, y=225)
        self.lab_result = tk.Label(frame1, name="lab_result")
        self.var_result = tk.StringVar()
        self.lab_result.configure(textvariable=self.var_result)
        self.lab_result.place(anchor="nw", x=950, y=300)
        frame1.pack(side="top")

        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()

    # 與遊戲連線
    def connect(self) -> tuple:
        try:
            mem = pymem.Pymem(self.config["game"])
            module = pymem.process.module_from_name(
                mem.process_handle, self.config["game"]
            ).lpBaseOfDll
            return (mem, module)
        except Exception:
            return (None, None)

    # 數據庫清洗
    def read_db(self, cat: str | None, item: str | None) -> pd.DataFrame:
        # 複製
        table = self.config["table"].copy()

        # 因為 str.contains無法辨別 NaN，故空值填補為空字串
        table.fillna("", inplace=True)

        # 考慮特定 act
        is_act = table["act"] == 1
        table = table.loc[is_act].copy()

        # 考慮特定 cat
        if cat:
            is_cat = table["cat"].str.contains(cat)
            table = table.loc[is_cat].copy()

        # 考慮特定 item
        if item:
            is_item = table["item"].str.contains(item)
            table = table.loc[is_item].copy()

        # hex to dec
        table[self.var_role.get()] = table[self.var_role.get()].apply(int, base=16)
        table["offset"] = table["offset"].apply(int, base=16)
        return table

    # 取得記憶體位址
    def get_addr(self, mem, base, offsets):
        addr = mem.read_int(base)
        for idx, offset in enumerate(offsets):
            if idx != len(offsets) - 1:
                addr = mem.read_int(addr + int(offset))
        addr = addr + int(offsets[-1])
        return addr

    # 作弊
    def cheating(self, cat: str | None, item: str | None, val: int) -> None:
        # 連線
        (mem, module) = self.connect()

        # 若連線成功，則嘗試作弊
        if module:
            # 根據條件，從數據庫搜尋符合的資料
            table = self.read_db(cat=cat, item=item)
            # 逐一修改遊戲參數
            for idx, row in table.iterrows():
                # 偏移量
                offsets = row[[self.var_role.get(), "offset"]].tolist()
                # 記憶體位址 = 基址 + 偏移量
                addr = self.get_addr(
                    mem=mem, base=module + self.config["base"], offsets=offsets
                )
                # 修改遊戲參數
                try:
                    mem.write_int(addr, val)
                except Exception:
                    # 如果是角色屬性寫入失敗，原因是目前劇情進度尚未獲得該角色的使用權
                    # 在花無缺早期路線中，無法修改燕南天和憐星!
                    print(f"{row['cat']}-{row['item']} 寫入失敗!")


if __name__ == "__main__":
    app = GuiApp()
    app.run()
