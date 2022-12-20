# NMF
This directory publishes the sample implmentation of Euclidean-, I-divergence-, and IS-divergence-based NMF.

# Description
The implementation visualizes the result of applying NMF to a matrix using an arbitrary number of bases.

# Usage
When
You can use the following command to run the demo.
```
docker build -t nmf .
docker run --rm -t nmf -v results:/usr/src/app/results [options]
```
All of the following options are required:
- L: Rows of observation matrix
- M: Rows of basis matrix
- N: Columns of observation matrix
- n_ineration: Maximum number of updates
- divergence: "EU", "I", or "IS"
  - EU: Euclidean distance
  - I: I-divergence
  - IS: Itakura-Saito divergence

# Sample
```
docker build -t nmf .
docker run --rm -t nmf --L 10 --M 5 --N 10 --n_iteration 100 --divergence EU
```

# Requirement
- docker: 20.10.21
