massiv = [4, 9, 7, 12, 8, 15, 10]

# 3-ə bölünməyən ədədləri tap
not_divisible_by_3 = [eded for eded in massiv if eded % 3 != 0]

# Ədədi ortanı hesabla
if not_divisible_by_3:
    ededi_orta = sum(not_divisible_by_3) / len(not_divisible_by_3)
else:
    ededi_orta = 0

# Nəticəni çap et
print("3-ə bölünməyən ədədlər:", not_divisible_by_3)
print("Onların ədədi ortası:", ededi_orta)