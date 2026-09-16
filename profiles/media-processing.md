# Profile — Media / Video / Audio Processing

适用于视频、音频、图像批处理和生成/剪辑管线。

## Stage 2

定义输入/输出格式、质量目标、时间轴/帧语义、保真要求、允许改变的内容、失败恢复和产物可追溯性。

## Stage 4

- codec/container/profile
- frame rate/resolution/color/audio policy
- media metadata
- processing graph / ownership
- temporary/working copy strategy
- deterministic/reproducible steps
- storage/lifecycle
- hardware acceleration (if any)
- timeout/retry/cancel/resume
- artifact hash/provenance

## Stage 7

- format validation
- A/V sync
- duration/timeline integrity
- visual/audio quality checks
- source vs output invariant
- representative fixture set
- performance/throughput
- failure recovery/no partial corruption
