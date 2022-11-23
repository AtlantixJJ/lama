import os

data_dir = "../../data/celebahq/id_inpaint/"
dirs = os.listdir(data_dir)
dirs.sort()
for d in dirs:
    print(d)
    os.system(f"python3 bin/gen_mask_dataset.py \
        $(pwd)/configs/data_gen/random_thick_512.yaml \
        ../../data/celebahq/id_inpaint/{d}/reference_image \
        ../../data/celebahq/id_inpaint/{d}/reference_mask --ext png")