# TicketRoute: A Support-Ticket Classification Benchmark

Synthetic paper fixture, not a real publication. All names, data descriptions, and results below are invented for regression testing. This file contains the entire test material; it does not include an actual dataset, evaluator, or code repository.

## Contribution and data

TicketRoute defines a benchmark for assigning an English support ticket to one of three categories: billing, account, or technical. Its contribution is the dataset and evaluation protocol, not a new classifier. The described dataset contains 640 manually labeled tickets from one fictional service. Tickets from the same conversation stay in the same split: 480 development examples and 160 test examples. The test labels are held out from model developers.

## Input and output protocol

Each input is a JSON object with `ticket_id` and `text`. A system must return `ticket_id` and exactly one `category` string from the three allowed categories. The evaluator joins predictions to inputs by `ticket_id`, checks the output schema, and computes macro-F1 across the three categories. Invalid or missing predictions are counted as incorrect; the paper does not specify how the evaluator handles duplicate IDs or zero-denominator class scores. Development data may be used to select prompts and thresholds; test labels must not be used for tuning.

## Results

Table 1 reports test macro-F1 of 0.625 for a rule baseline and 0.740 for a small classifier under this protocol. These scores measure classification on this test split. The paper provides no latency, cost, confidence intervals, or production outcome measurements.

## Release and deployment gaps

The paper does not provide a dataset license, version hash, evaluator implementation, or official repository URL. It does not specify the small classifier's hyperparameters. It does not evaluate Chinese tickets, multilingual inputs, multi-label tickets, or categories outside the three-category taxonomy. Deployment on a different language or service requires separately checking data rights, label mapping, output handling, and performance on representative examples; the reported test scores alone do not establish deployment quality.
