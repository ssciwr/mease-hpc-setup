INSTALL=/gpfs/bwfor/work/ws/hd_uk239-measelab

# miniconda

bash setup_conda.sh $INSTALL

# mease-lab-to-nwb & measelab env

bash setup_measelab.sh $INSTALL

# sorters

bash setup_combinato.sh $INSTALL

bash setup_hdsort.sh $INSTALL

bash setup_herdingspikes2.sh $INSTALL

bash setup_ironclust.sh $INSTALL

bash setup_kilosort.sh $INSTALL

bash setup_kilosort2.sh $INSTALL

bash setup_kilosort2_5.sh $INSTALL

bash setup_kilosort3.sh $INSTALL

bash setup_klusta.sh $INSTALL

bash setup_mountainsort4.sh $INSTALL

bash setup_spyking_circus.sh $INSTALL

bash setup_tridesclous.sh $INSTALL

bash setup_waveclus.sh $INSTALL

bash setup_yass.sh $INSTALL

# init script for users

cp init.sh $INSTALL/init.sh