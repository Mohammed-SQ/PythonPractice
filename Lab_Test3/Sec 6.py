def extract_files(text):
    parts = text.split()
    doc_list = []
    img_list = []

    for name in parts:
        if name.endswith(".pdf") or name.endswith(".docx"):
            doc_list.append(name)
        elif name.endswith(".png") or name.endswith(".jpg"):
            img_list.append(name)

    if len(doc_list) == 0:
        doc_list = ["None"]
    if len(img_list) == 0:
        img_list = ["None"]

    return doc_list, img_list

line = input("Enter all file names (separated by spaces): ")
files = line.split() # *Fatima201.docx lab10tasks.pdf butterfly.png mountain.jpg

for x in files[:]:
    if x.startswith("*"):
        files.remove(x)

updated = ""
for i in range(len(files)):
    if i == 0:
        updated = files[i]
    else:
        updated = updated + " " + files[i]
docs, imgs = extract_files(updated)

print("\nDocuments List:", docs)
print("Images List:", imgs)

if docs == ["None"]:
    print("Document count: 0")
else:
    print("Document count:", len(docs))

if imgs == ["None"]:
    print("Image count: 0")
else:
    print("Image count:", len(imgs))
