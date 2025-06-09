img_uncompressed = 3840 * 2160 * 17
img_compressed = 1280 * 720 * 5

pack_uncompressed = 120 * img_uncompressed
pack_compressed = 120 * img_compressed

difference = pack_uncompressed - pack_compressed

answer = difference / 2 ** 13

print(int(answer))