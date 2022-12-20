# NMF
This directory publishes the sample implmentation of Euclidean-, I-divergence-, and IS-divergence-based NMF.

# Description
The implementation visualizes the result of applying NMF to a matrix using an arbitrary number of bases.

# Requirement
- docker compose: v2.13.0

# Usage
When
You can use the following command to run the demo.
```
git clone https://github.com/beginaid/NMF
cd MMF
docker compose up -d --build
```
All of the following options are managed on docker-compose.yml:
- L: Rows of observation matrix
- M: Rows of basis matrix
- N: Columns of observation matrix
- n_ineration: Maximum number of updates
- divergence: "EU", "I", or "IS"
  - EU: Euclidean distance
  - I: I-divergence
  - IS: Itakura-Saito divergence

After the nmf container is up, a directory named "results" is created.
The directory contains a graph describing the decreasing process of divergence and a heatmap visualizing the pre- and post-approximation matrices.
When you can see these outputs, delete the resources created using the following command.
```
docker compose down
```
