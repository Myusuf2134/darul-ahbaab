import json, re

path = "Content/يَا إِمَامَ الرُّسْلِ يَا سَنَدِي"
raw = open(path, encoding="utf-8").read().strip()
blocks = [b.strip().split("\n") for b in re.split(r"\n\s*\n", raw) if b.strip()]

couplets = []
for b in blocks:
    if len(b) < 3:
        continue
    ar = [s.strip() for s in b[0].split("/")]
    tr = [s.strip() for s in b[1].split("/")]
    tl = " ".join(b[2:]).strip()
    parts = [p.strip() for p in tl.split(" — ")] if " — " in tl else [tl, ""]
    couplets.append({"arabic": ar, "transliteration": tr,
                     "translation": parts[:2] + [""] * (2 - len(parts[:2])),
                     "isRefrain": False})

entry = {"title": "يَا إِمَامَ الرُّسْلِ يَا سَنَدِي",
         "englishTitle": "O Leader of the Messengers, O My Support",
         "couplets": couplets}
blob = json.dumps(entry, ensure_ascii=False)
print(f"parsed {len(couplets)} couplets")

for f in ["admin.html", "live.html"]:
    s = open(f, encoding="utf-8").read()
    i = s.rindex("}];")
    open(f, "w", encoding="utf-8").write(s[:i+1] + "," + blob + s[i+1:])
    print("updated", f)
