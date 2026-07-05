# ==============================================================================
# 剧本入口
# 剧情线：外向邀请认真加入 → 原成员反应 → 日常 → 矛盾 → 和解
# ==============================================================================

label start:

    scene black with dissolve
    # 第1章：外向邀请认真加入乐队
    call memories_band_begin from _call_memories_band_begin

    # 第2章：原成员对新人加入的反应
    call meet from _call_meet

    # 第3章：日常1 & 首次排练
    call daily_01 from _call_daily_01

    # 第4章：日常2（书店买书 → 逛商场 → 咖啡厅）
    call bookstore from _call_bookstore

    # 第5章：矛盾（转折）
    call turn_boom from _call_turn_boom

    # 第6章：和解（包饺子/寿司🍣）
    # TODO: 需要补充

    return
