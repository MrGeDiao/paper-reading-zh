# MiniBench: A Small Evaluation Suite

## Claims

The paper makes three main claims: MiniBench measures robust reasoning, its score predicts real deployment quality, and Model A is more reliable than Model B.

## Construction

MiniBench contains 600 examples created by four annotators. The paper reports 0.78 pairwise agreement. It does not describe annotator recruitment, compensation, or whether examples overlap with public training corpora.

## Results

Table 1 reports Model A scoring 74 and Model B scoring 69 on MiniBench. Table 2 reports a correlation of 0.42 between MiniBench scores and one internal deployment rating across eight models. No confidence interval or significance test is reported. The paper contains no intervention or causal analysis.

## Limitations

The deployment rating is not publicly defined. There is no external replication and no experiment showing that a five-point MiniBench difference changes real deployment outcomes.
