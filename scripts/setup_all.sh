INSTALL=/gpfs/bwfor/work/ws/hd_uk239-measelab

bash setup_conda.sh $INSTALL

bash setup_measelab.sh $INSTALL

bash setup_kilosort.sh $INSTALL

bash setup_kilosort2.sh $INSTALL

bash setup_kilosort2_5.sh $INSTALL

bash setup_kilosort3.sh $INSTALL

bash setup_spyking_circus.sh $INSTALL

bash setup_herdingspikes2.sh $INSTALL

cp init.sh $INSTALL/init.sh