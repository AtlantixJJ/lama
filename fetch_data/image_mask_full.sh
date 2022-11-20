#DATA_DIR=../../data/celebahq/image
#OUT_DIR=../../data/celebahq/mask
#ipython bin/gen_mask_dataset.py \
#    $(pwd)/configs/data_gen/random_thick_256.yaml \
#    $DATA_DIR $OUT_DIR/random_thick_256/

#python3 bin/gen_mask_dataset.py \
#    $(pwd)/configs/data_gen/random_medium_256.yaml \
#    $DATA_DIR $OUT_DIR/random_medium_256/

DATA_DIR=../../data/ffhq/images256x256
OUT_DIR=../../data/ffhq/mask
ipython bin/gen_mask_dataset.py -- \
    $(pwd)/configs/data_gen/random_thick_256.yaml \
    $DATA_DIR $OUT_DIR/random_thick_256/ --ext png 