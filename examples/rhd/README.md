# RHD concatenation and spike sorting script

## Notes

- Use larger than default kilosort batch size
  - Concatenated recordings are quite long
    - e.g. 86 x 15min rhd files -> 280GB recording
  - Kilosort batch size affects GPU ram requirements in two different ways
    - inverts a `nbatch` x `nbatch` matrix of differences: gpu ram required _decreases_ with batch size
      - possible error if batch size too small: `Error using gpuArray.zeros Maximum variable size allowed on the device is exceeded`
      - max number of batches is around 65k (on any gpu as array index is of type int32)
    - main processing of a batch: gpu ram required _increases_ with batch size
      - possible error if batch size too larger: `out of memory`
  - Default kilosort batch size runs into the first problem with this dataset
  - Larger batch size fixes this but then runs into the second problem on K80 gpus with 12GB ram
- Ask for a specific GPU
  - need more gpu ram than the smaller GPUs have
- Raw traces need to be rescaled from uint16 to int16
  - Spikeinterface rhd extractor gives uint16
  - Kilosort assumes it will get int16
- Use Kilosort 2 only due to tetrode geometry (https://github.com/MouseLand/Kilosort/issues/350)
