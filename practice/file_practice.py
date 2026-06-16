# with open('test1.txt', 'r') as rf:
#     with open('test1_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

with open('logo.png', 'rb') as rf:
    with open('logo_copy.png', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)



    