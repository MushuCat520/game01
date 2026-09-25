# ============================================================
# 背景图片（自动等比缩放，超过裁剪，小的放大）
# ============================================================

image school_day = Transform("images/school_road.jpg", size=(1920, 1080), fit="cover")
image classroom = Transform("images/classroom.jpg", size=(1920, 1080), fit="cover")
image cafeteria = Transform("images/cafeteria.jpg", size=(1920, 1080), fit="cover")
image school_evening = Transform("images/school_evening.jpg", size=(1920, 1080), fit="cover")