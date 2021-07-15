INSTALL=/gpfs/bwfor/work/ws/hd_uk239-measelab

bash setup_conda.sh $INSTALL

bash setup_kilosort2_5.sh $INSTALL

bash setup_measelab.sh $INSTALL

cp init.sh $INSTALL/init.sh