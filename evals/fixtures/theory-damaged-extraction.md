# Convergence Under Delayed Gradients

## Problem setting

Let the objective be convex and L-smooth. Assumption A1 bounds gradient delay by D. Assumption A2 requires unbiased stochastic gradients with variance at most sigma squared.

## Main result

Theorem 1 states that Algorithm 1 reaches an epsilon-stationary point after a number of iterations depending on L, D, sigma, and epsilon. The theorem only applies under A1 and A2.

## Proof outline

Lemma 1 bounds the error introduced by delayed gradients. Lemma 2 controls the stochastic variance term. The proof of Theorem 1 combines the two lemmas with a telescoping argument.

## Extraction warning

The displayed rate equation on page 4 is corrupted in the extracted text: several exponents and denominator terms are missing. The exact iteration complexity cannot be recovered from this material.

## Discussion

The paper includes a small synthetic experiment as an illustration, but it does not test whether A1 holds in real distributed systems.
