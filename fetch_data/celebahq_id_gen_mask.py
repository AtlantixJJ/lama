import os

data_dir = "../../data/celebahq/export/"
dirs = os.listdir(data_dir)
dirs.sort()
for d in dirs:
    print(d)
    os.system(f"python3 bin/gen_mask_dataset.py \
        $(pwd)/configs/data_gen/random_thick_512.yaml \
        ../../data/celebahq/export/{d}/train_image \
        ../../data/celebahq/export/{d}/train_image_mask --ext png")
    os.system(f"python3 bin/gen_mask_dataset.py \
        $(pwd)/configs/data_gen/random_thick_512.yaml \
        ../../data/celebahq/export/{d}/test_image \
        ../../data/celebahq/export/{d}/test_image_mask --ext png")