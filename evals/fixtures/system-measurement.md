# EdgeCache: A Production Measurement Study

## Abstract

We evaluate an edge-cache scheduler deployed in 12 clusters from one cloud provider. The paper reports a 31.7% reduction in p99 request latency and a 9.4% reduction in network traffic relative to the previous scheduler.

## Measurement setup

- Observation window: 8 weeks in 2025.
- Region: one geographic region.
- Traffic: a 1% sampled production trace; maintenance windows and two outage days were excluded.
- Comparison: four weeks before deployment versus four weeks after deployment.
- There was no randomized assignment and the workload mix changed during week 6.

## Results

Table 2 reports p99 latency decreasing from 120 ms to 82 ms. Table 3 reports network traffic decreasing from 10.6 PB to 9.6 PB. The authors attribute both changes to EdgeCache.

## Limitations

The study covers one provider, one region, and a short time window. The authors did not separately estimate the effect of the workload change in week 6.
